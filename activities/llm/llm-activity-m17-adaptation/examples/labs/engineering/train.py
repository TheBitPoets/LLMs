"""Reproduce pretraining and LoRA on a tiny synthetic corpus, on CPU."""
from dataclasses import asdict
import argparse
import copy
import hashlib
import json
import math
from pathlib import Path
import platform
import time
import torch
from torch.nn import functional as F
from .tiny_lm import TinyLM, Config, attach_lora

DATA = Path(__file__).parent / "fixtures/text"


def tensor(path):
    return torch.tensor(list(path.read_bytes()), dtype=torch.long)


def loss_on(model, data):
    model.eval()
    total, count = 0.0, 0
    with torch.no_grad():
        for start in range(0, len(data)-1, model.config.context):
            length = min(model.config.context, len(data)-1-start)
            x, y = data[start:start+length][None], data[start+1:start+length+1]
            total += F.cross_entropy(model(x)[0], y, reduction="sum").item()
            count += length
    return total/count


def train_steps(model, data, valid, steps=160, lr=0.003, seed=7):
    if steps < 1 or len(data) <= model.config.context:
        raise ValueError("positive steps and enough training bytes required")
    optimizer = torch.optim.AdamW([p for p in model.parameters() if p.requires_grad], lr=lr)
    random = torch.Generator().manual_seed(seed)
    history, best, best_loss = [], copy.deepcopy(model.state_dict()), loss_on(model, valid)
    for step in range(1, steps+1):
        model.train()
        starts = torch.randint(len(data)-model.config.context, (8,), generator=random)
        x = torch.stack([data[i:i+model.config.context] for i in starts])
        y = torch.stack([data[i+1:i+model.config.context+1] for i in starts])
        loss = F.cross_entropy(model(x).flatten(0, 1), y.flatten())
        optimizer.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        optimizer.step()
        if step == 1 or step % 20 == 0 or step == steps:
            validation = loss_on(model, valid)
            history.append({"step": step, "train_nats_per_byte": loss.item(),
                            "validation_nats_per_byte": validation})
            if validation < best_loss:
                best, best_loss = copy.deepcopy(model.state_dict()), validation
    model.load_state_dict(best)
    return history


def unigram_loss(train, test):
    probabilities = (torch.bincount(train, minlength=256).double()+1) / (len(train)+256)
    return -probabilities[test[1:]].log().mean().item()


def experiment(output, steps=160, adapter_steps=120):
    output.mkdir(parents=True, exist_ok=True)
    torch.set_num_threads(1)
    torch.manual_seed(7)
    torch.use_deterministic_algorithms(True)
    splits = {p.stem: tensor(p) for p in sorted(DATA.glob("*.txt"))}
    documents = {p.stem: set(p.read_text().splitlines()) for p in DATA.glob("*.txt")}
    for prefix in ["base", "adapt"]:
        a, b, c = [documents[f"{prefix}-{name}"] for name in ["train", "valid", "test"]]
        if a & b or a & c or b & c:
            raise ValueError("document-level split leakage")
    model = TinyLM()
    start = time.perf_counter()
    initial = loss_on(model, splits["base-valid"])
    history = train_steps(model, splits["base-train"], splits["base-valid"], steps)
    base_test = loss_on(model, splits["base-test"])
    checkpoint = output / "tiny-byte-lm.pt"
    torch.save({"config": asdict(model.config), "state_dict": model.state_dict()}, checkpoint)
    before = loss_on(model, splits["adapt-test"])
    base_weights = {name: value.detach().clone() for name, value in model.named_parameters()}
    adapted = attach_lora(copy.deepcopy(model))
    adapter_history = train_steps(adapted, splits["adapt-train"], splits["adapt-valid"],
                                  adapter_steps, lr=0.02)
    base_unchanged = all(torch.equal(value, dict(adapted.named_parameters())[
        "head.base.weight" if name == "head.weight" else name]) for name, value in base_weights.items())
    if not base_unchanged:
        raise AssertionError("LoRA changed frozen base parameters")
    adapter_path = output / "head-lora.pt"
    torch.save({"A": adapted.head.A.detach(), "B": adapted.head.B.detach(),
                "rank": adapted.head.A.size(0), "scale": adapted.head.scale,
                "base_sha256": hashlib.sha256(checkpoint.read_bytes()).hexdigest()}, adapter_path)
    report = {
        "mode": "measured-cpu-synthetic-corpus", "seed": 7, "torch": torch.__version__,
        "python": platform.python_version(), "machine": platform.machine(), "threads": 1,
        "config": asdict(model.config), "parameter_count": sum(p.numel() for p in model.parameters()),
        "training": {"steps": steps, "adapter_steps": adapter_steps, "batch": 8,
                     "learning_rate": 0.003, "adapter_learning_rate": 0.02,
                     "optimizer": "AdamW", "weight_decay": 0.01, "clip_norm": 1.0,
                     "checkpoint_selection": "minimum validation loss at evaluation checkpoints",
                     "evaluation": "all next-byte targets except first byte; context reset every 64 positions"},
        "corpus_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in DATA.glob("*.txt")},
        "initial_validation_nats_per_byte": initial, "history": history,
        "base_test_nats_per_byte": base_test, "base_test_bits_per_byte": base_test/math.log(2),
        "unigram_test_nats_per_byte": unigram_loss(splits["base-train"], splits["base-test"]),
        "adapter_target": "output projection only", "adapter_history": adapter_history,
        "adapter_trainable_parameters": sum(p.numel() for p in adapted.parameters() if p.requires_grad),
        "adapt_test_before": before, "adapt_test_after": loss_on(adapted, splits["adapt-test"]),
        "base_test_after_adapter": loss_on(adapted, splits["base-test"]),
        "frozen_base_unchanged": base_unchanged, "elapsed_seconds": time.perf_counter()-start,
        "artifacts_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in [checkpoint, adapter_path]},
        "limits": "tiny byte LM; templated synthetic distribution, not natural-language competence or a frontier model",
    }
    (output / "training-report.json").write_text(json.dumps(report, indent=2)+"\n")
    return report


def load_model(path):
    data = torch.load(path, map_location="cpu", weights_only=True)
    model = TinyLM(Config(**data["config"]))
    model.load_state_dict(data["state_dict"])
    return model.eval()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("output/engineering"))
    parser.add_argument("--steps", type=int, default=160)
    parser.add_argument("--adapter-steps", type=int, default=120)
    args = parser.parse_args()
    result = experiment(args.output, args.steps, args.adapter_steps)
    print(json.dumps({k: result[k] for k in ["base_test_nats_per_byte", "unigram_test_nats_per_byte",
        "adapt_test_before", "adapt_test_after", "frozen_base_unchanged", "elapsed_seconds"]}, indent=2))
