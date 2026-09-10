#!/usr/bin/env python3
"""Build original figures from the checked-in CPU measurements."""
import json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
report = json.loads((ROOT / "output/engineering/training-report.json").read_text())
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "svg.fonttype": "none", "svg.hashsalt": "llms-engineering"})
fig, axes = plt.subplots(2, 1, figsize=(9, 8), layout="constrained")
fig.suptitle("Apprendere un compito, misurare le regressioni", fontsize=19, weight="bold")
history = report["history"]
axes[0].plot([r["step"] for r in history], [r["train_nats_per_byte"] for r in history],
             "o-", label="Training: batch corrente", color="#2463a6")
axes[0].plot([r["step"] for r in history], [r["validation_nats_per_byte"] for r in history],
             "s--", label="Validation: split separato", color="#a94b09")
axes[0].set(xlabel="Passo di ottimizzazione", ylabel="Loss (nat/byte)", title="Transformer base: corpus sintetico a template")
axes[0].legend(frameon=False)
values = [[report["base_test_nats_per_byte"], report["adapt_test_before"]],
          [report["base_test_after_adapter"], report["adapt_test_after"]]]
for offset, values_one, color, label in [(-0.18, values[0], "#2463a6", "Base"),
                                       (0.18, values[1], "#a94b09", "Base + LoRA")]:
    bars = axes[1].bar([offset, 1+offset], values_one, width=.34, color=color, label=label)
    axes[1].bar_label(bars, fmt="%.3f", padding=4)
axes[1].set(xticks=[0,1], xticklabels=["Dominio originale", "Nuovo dominio"], ylabel="Test loss (nat/byte)",
            title="LoRA: migliora il target, peggiora il dominio originale", ylim=(0,7.7))
axes[1].legend(frameon=False)
for ax in axes:
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", alpha=.2)
    ax.set_axisbelow(True)
fig.supxlabel("CPU x86_64, PyTorch 2.8.0, seed 7. Valori misurati; meno loss è meglio.\nFonte: output/engineering/training-report.json. Nessuna misura di competenza generale.", fontsize=10)
target = ROOT / "visuals/static/engineering-training.svg"
fig.savefig(target, metadata={"Date": None})
target.write_text("\n".join(line.rstrip() for line in target.read_text().splitlines())+"\n")
fig.savefig(target.parent / "rendered/engineering-training.png", dpi=180)
plt.close(fig)
print(target.relative_to(ROOT))
