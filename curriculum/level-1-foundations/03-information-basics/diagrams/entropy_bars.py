"""Draw three distributions over the weather, from certain to uniform, with their entropies.

Run:  python entropy_bars.py

Expected output:
    wrote entropy_bars.png
"""

import sys
from pathlib import Path

ROOT = next(p for p in Path(__file__).resolve().parents if (p / "shared").is_dir())
sys.path.insert(0, str(ROOT))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

from shared.diagram_kit import FONT, PALETTE, TEXT  # noqa: E402

OUTCOMES = ["sunny", "cloudy", "rain"]
DISTRIBUTIONS = [
    ("Certain", [1.0, 0.0, 0.0]),
    ("Brindlewick's weather", [0.5, 0.3, 0.2]),
    ("Uniform", [1 / 3, 1 / 3, 1 / 3]),
]
STYLES = [("default", ""), ("external", "//"), ("data", "..")]


def entropy(p: list[float]) -> float:
    return float(sum(-x * np.log2(x) for x in p if x > 0))


fig, axes = plt.subplots(1, 3, figsize=(10, 3.6), sharey=True)
for ax, (title, dist) in zip(axes, DISTRIBUTIONS):
    for i, (prob, (kind, hatch)) in enumerate(zip(dist, STYLES)):
        fill, edge = PALETTE[kind]
        ax.bar(i, prob, color=fill, edgecolor=edge, linewidth=2, hatch=hatch, width=0.7)
        ax.text(i, prob + 0.03, f"{prob:.2f}", ha="center", fontsize=10, family=FONT, color=TEXT)
    ax.set_xticks(range(3))
    ax.set_xticklabels(OUTCOMES, fontsize=10, family=FONT)
    ax.set_ylim(0, 1.15)
    ax.set_title(f"{title}\nentropy = {entropy(dist):.3f} bits", fontsize=11,
                 fontweight="bold", family=FONT, color=TEXT)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
axes[0].set_ylabel("probability", fontsize=11, family=FONT, color=TEXT)
fig.suptitle("More spread-out distributions have higher entropy", fontsize=13,
             fontweight="bold", family=FONT, color=TEXT, y=1.06)

out = Path(__file__).with_suffix(".png")
fig.savefig(out, dpi=200, facecolor="white", bbox_inches="tight", metadata={"Software": None})
print("wrote", out.name)
