"""Compare explicit attention with a library kernel, and full-prefix with KV decode."""
import argparse
import json
import math
from pathlib import Path
import statistics
import time
import hashlib
import platform
import torch
from torch.nn import functional as F
from .train import load_model


def reference_attention(q, k, v):
    scores = q @ k.transpose(-2, -1) / math.sqrt(q.shape[-1])
    mask = torch.ones(scores.shape[-2:], dtype=torch.bool, device=q.device).tril()
    return scores.masked_fill(~mask, float("-inf")).softmax(-1) @ v


def tiled_attention(q, k, v, tile=16):
    """Inference microkernel with online softmax; no full score matrix stored.

    PyTorch tensor operations, educational CPU kernel, not custom CUDA.
    """
    if q.shape != k.shape or k.shape != v.shape or tile < 1:
        raise ValueError("equal [B,H,T,D] tensors and positive tile required")
    time_steps, width = q.shape[-2:]
    result = torch.empty_like(q)
    for start in range(0, time_steps, tile):
        query = q[..., start:start+tile, :]
        m = torch.full_like(query[..., :1], float("-inf"))
        denominator = torch.zeros_like(m)
        accumulator = torch.zeros_like(query)
        for key_start in range(0, start + query.shape[-2], tile):
            key, value = k[..., key_start:key_start+tile, :], v[..., key_start:key_start+tile, :]
            scores = query @ key.transpose(-2, -1) / math.sqrt(width)
            mask = torch.arange(key_start, key_start+key.shape[-2], device=q.device)[None, :] <= torch.arange(
                start, start+query.shape[-2], device=q.device)[:, None]
            scores = scores.masked_fill(~mask, float("-inf"))
            next_m = torch.maximum(m, scores.amax(-1, keepdim=True))
            rescale = (m-next_m).exp()
            weights = (scores-next_m).exp()
            accumulator = accumulator * rescale + weights @ value
            denominator = denominator * rescale + weights.sum(-1, keepdim=True)
            m = next_m
        result[..., start:start+query.shape[-2], :] = accumulator/denominator
    return result


def median_time(function, repetitions=7, samples=None):
    for _ in range(2):
        function()
    values = []
    for _ in range(repetitions):
        start = time.perf_counter()
        function()
        values.append(time.perf_counter()-start)
    if samples is not None:
        samples.extend(values)
    return statistics.median(values)


def benchmark(checkpoint, output):
    torch.set_num_threads(1)
    torch.manual_seed(7)
    model = load_model(checkpoint)
    ids = torch.randint(0, 256, (1, 48))
    q, k, v = [torch.randn(1, 4, 64, 12) for _ in range(3)]
    timing_samples = {}
    def measure(name, function):
        timing_samples[name] = []
        return median_time(function, samples=timing_samples[name])
    with torch.inference_mode():
        reference = reference_attention(q, k, v)
        tiled = tiled_attention(q, k, v)
        fused = F.scaled_dot_product_attention(q, k, v, is_causal=True)
        full_logits = model(ids)
        def cached():
            cache, logits = None, []
            for t in range(ids.size(1)):
                value, cache = model(ids[:, t:t+1], cache=cache, return_cache=True)
                logits.append(value)
            return torch.cat(logits, 1), cache
        cached_logits, cache = cached()
        def repeated_prefix():
            for t in range(ids.size(1)):
                model(ids[:, :t+1])
        torch.testing.assert_close(tiled, reference, atol=2e-6, rtol=2e-5)
        torch.testing.assert_close(fused, reference, atol=2e-6, rtol=2e-5)
        torch.testing.assert_close(cached_logits, full_logits, atol=2e-5, rtol=2e-5)
        report = {"mode": "measured-cpu", "torch": torch.__version__, "threads": 1,
            "python": platform.python_version(), "machine": platform.machine(),
            "checkpoint_sha256": hashlib.sha256(checkpoint.read_bytes()).hexdigest(),
            "seed": 7, "dtype": str(q.dtype), "warmup": 2, "repetitions": 7,
            "attention_shape": list(q.shape), "cache_bytes": sum(t.numel()*t.element_size() for pair in cache for t in pair),
            "max_error_tiled": (tiled-reference).abs().max().item(),
            "max_error_library_kernel": (fused-reference).abs().max().item(),
            "max_error_cached_logits": (cached_logits-full_logits).abs().max().item(),
            "attention_reference_seconds": measure("attention_reference", lambda: reference_attention(q, k, v)),
            "attention_tiled_seconds": measure("attention_tiled", lambda: tiled_attention(q, k, v)),
            "attention_library_seconds": measure("attention_library", lambda: F.scaled_dot_product_attention(q,k,v,is_causal=True)),
            "prefill_seconds": measure("prefill", lambda: model(ids)),
            "decode_full_prefix_seconds": measure("decode_full_prefix", repeated_prefix),
            "decode_with_cache_seconds": measure("decode_with_cache", cached),
            "timing_samples_seconds": timing_samples,
            "limits": "small CPU tensors; no GPU timing, no assumed acceleration; tiled kernel is Python/PyTorch"}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2)+"\n")
    return report


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint", type=Path, default=Path("output/engineering/tiny-byte-lm.pt"))
    parser.add_argument("--output", type=Path, default=Path("output/engineering/inference-report.json"))
    args=parser.parse_args()
    print(json.dumps(benchmark(args.checkpoint,args.output),indent=2))
