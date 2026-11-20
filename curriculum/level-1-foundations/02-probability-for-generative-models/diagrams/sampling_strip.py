"""Draw sampling from a categorical distribution as a strip from 0 to 1.

Each outcome gets a slice of the strip as wide as its probability. A uniform random number u
lands somewhere on the strip, and the slice it lands in is the sample.

Run:  python sampling_strip.py

Expected output:
    wrote sampling_strip.png
"""

import sys
from pathlib import Path

ROOT = next(p for p in Path(__file__).resolve().parents if (p / "shared").is_dir())
sys.path.insert(0, str(ROOT))

import matplotlib.pyplot as plt  # noqa: E402

from shared.diagram_kit import FONT, PALETTE, TEXT  # noqa: E402

SLICES = [("sunny", 0.0, 0.5, "default", ""), ("cloudy", 0.5, 0.3, "external", "//"),
          ("rain", 0.8, 0.2, "data", "..")]
DRAWS = [0.10, 0.62, 0.93]

fig, ax = plt.subplots(figsize=(9, 2.8))
for name, start, width, kind, hatch in SLICES:
    fill, edge = PALETTE[kind]
    ax.barh(0, width, left=start, height=0.6, color=fill, edgecolor=edge, linewidth=2, hatch=hatch)
    ax.text(start + width / 2, 0, f"{name}\np = {width:.1f}", ha="center", va="center",
            fontsize=11, fontweight="bold", color=TEXT, family=FONT,
            bbox=dict(facecolor=fill, edgecolor="none", pad=2))

for u in DRAWS:
    ax.annotate(f"u = {u:.2f}", xy=(u, 0.32), xytext=(u, 0.85), ha="center", fontsize=10,
                family=FONT, color=TEXT,
                arrowprops=dict(arrowstyle="-|>", color=PALETTE["action"][1], lw=1.8))

ax.set_xlim(-0.02, 1.02)
ax.set_ylim(-0.6, 1.1)
ax.set_yticks([])
ax.set_xticks([0, 0.5, 0.8, 1.0])
ax.set_xticklabels(["0", "0.5", "0.8", "1"], fontsize=10, family=FONT)
ax.set_xlabel("cumulative probability", fontsize=10, family=FONT, color=TEXT)
for spine in ("top", "right", "left"):
    ax.spines[spine].set_visible(False)
ax.set_title("Sampling: where does a uniform random number land?", fontsize=13,
             fontweight="bold", family=FONT, color=TEXT, pad=10)

out = Path(__file__).with_suffix(".png")
fig.savefig(out, dpi=200, facecolor="white", bbox_inches="tight", metadata={"Software": None})
print("wrote", out.name)
