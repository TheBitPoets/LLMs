"""Generate bytes with our trained tiny LM; report invalid UTF-8 honestly."""
import argparse
import hashlib
import json
from pathlib import Path
import torch
from .train import load_model
from .tiny_lm import attach_lora


def generate(checkpoint, prompt, count=80, temperature=0.0, adapter=None):
    if not 1 <= count <= 4096 or not 0 <= temperature <= 5:
        raise ValueError("count must be 1..4096 and temperature 0..5")
    torch.set_num_threads(1)
    torch.manual_seed(7)
    model = load_model(checkpoint)
    if adapter:
        data = torch.load(adapter, map_location="cpu", weights_only=True)
        if data["base_sha256"] != hashlib.sha256(Path(checkpoint).read_bytes()).hexdigest():
            raise ValueError("adapter belongs to a different base checkpoint")
        attach_lora(model, rank=data["rank"])
        with torch.no_grad():
            model.head.A.copy_(data["A"])
            model.head.B.copy_(data["B"])
        model.head.scale = data["scale"]
    model.eval()
    prefix = list(prompt.encode("utf-8")) or [0]
    output = bytearray()
    with torch.inference_mode():
        for _ in range(count):
            logits = model(torch.tensor([prefix[-model.config.context:]]))[0, -1]
            token = (int(logits.argmax()) if temperature == 0 else
                     int(torch.multinomial((logits/temperature).softmax(-1), 1)))
            prefix.append(token)
            output.append(token)
    try:
        continuation, valid = output.decode("utf-8"), True
    except UnicodeDecodeError:
        continuation, valid = output.decode("utf-8", errors="replace"), False
    return {"prompt": prompt, "continuation": continuation, "bytes_hex": output.hex(),
            "valid_utf8": valid, "temperature": temperature, "seed": 7,
            "checkpoint_sha256": hashlib.sha256(Path(checkpoint).read_bytes()).hexdigest(),
            "adapter_sha256": hashlib.sha256(Path(adapter).read_bytes()).hexdigest() if adapter else None,
            "policy": "last 64 bytes, positions reset per window; no EOS or instruction tuning"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint", type=Path, default=Path("output/engineering/tiny-byte-lm.pt"))
    parser.add_argument("--adapter", type=Path)
    parser.add_argument("--prompt", default="Ada studia")
    parser.add_argument("--count", type=int, default=80)
    parser.add_argument("--temperature", type=float, default=0)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = generate(args.checkpoint, args.prompt, args.count, args.temperature, args.adapter)
    text = json.dumps(report, ensure_ascii=False, indent=2)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(text)
