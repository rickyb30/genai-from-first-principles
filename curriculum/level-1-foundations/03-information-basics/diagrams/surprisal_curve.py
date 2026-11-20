"""Plot surprisal, -log2(p), against probability p, marking the three weather outcomes.

Run:  python surprisal_curve.py

Expected output:
    wrote surprisal_curve.png
"""

import sys
from pathlib import Path

ROOT = next(p for p in Path(__file__).resolve().parents if (p / "shared").is_dir())
sys.path.insert(0, str(ROOT))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

from shared.diagram_kit import FONT, PALETTE, TEXT  # noqa: E402

# (name, probability, where to put the label)
POINTS = [("sunny", 0.5, (0.55, 2.2)), ("cloudy", 0.3, (0.38, 3.1)), ("rain", 0.2, (0.22, 4.1)),
          ("a 1-in-100 event", 0.01, (0.07, 7.0))]

p = np.linspace(0.005, 1.0, 400)
fig, ax = plt.subplots(figsize=(8, 4.6))
ax.plot(p, -np.log2(p), color=PALETTE["default"][1], lw=2.5)

for name, prob, label_at in POINTS:
    bits = -np.log2(prob)
    ax.plot([prob], [bits], "o", ms=8, color=PALETTE["action"][1])
    ax.annotate(f"{name}\np = {prob:g}: {bits:.2f} bits", xy=(prob, bits), xytext=label_at,
                fontsize=10, family=FONT, color=TEXT,
                arrowprops=dict(arrowstyle="-", color=TEXT, lw=0.8))

ax.annotate("certain (p = 1): 0 bits", xy=(1.0, 0.0), xytext=(0.72, 1.0), fontsize=10,
            family=FONT, color=TEXT, arrowprops=dict(arrowstyle="-|>", color=TEXT, lw=1.2))

ax.set_xlim(0, 1.05)
ax.set_ylim(-0.2, 8)
ax.set_xlabel("probability the model gave the outcome, p", fontsize=11, family=FONT, color=TEXT)
ax.set_ylabel("surprisal, -log2(p), in bits", fontsize=11, family=FONT, color=TEXT)
ax.set_title("Rare outcomes are surprising: surprisal = -log2(p)", fontsize=13,
             fontweight="bold", family=FONT, color=TEXT)
for spine in ("top", "right"):
    ax.spines[spine].set_visible(False)
ax.grid(alpha=0.25)

out = Path(__file__).with_suffix(".png")
fig.savefig(out, dpi=200, facecolor="white", bbox_inches="tight", metadata={"Software": None})
print("wrote", out.name)
