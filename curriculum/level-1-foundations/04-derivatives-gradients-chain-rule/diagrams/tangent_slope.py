"""Plot L(w) = (2w - 6)^2 with its tangent line at w = 1 (slope -16) and the minimum at w = 3.

Run:  python tangent_slope.py

Expected output:
    wrote tangent_slope.png
"""

import sys
from pathlib import Path

ROOT = next(p for p in Path(__file__).resolve().parents if (p / "shared").is_dir())
sys.path.insert(0, str(ROOT))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

from shared.diagram_kit import FONT, PALETTE, TEXT  # noqa: E402


def loss(w):
    return (2 * w - 6) ** 2


w = np.linspace(-0.2, 5.2, 300)
w0, slope = 1.0, -16.0
fig, ax = plt.subplots(figsize=(8, 4.6))
ax.plot(w, loss(w), color=PALETTE["default"][1], lw=2.5, label="L(w) = (2w - 6)²")

tangent_w = np.linspace(0.2, 1.8, 50)
ax.plot(tangent_w, loss(w0) + slope * (tangent_w - w0), color=PALETTE["action"][1], lw=2,
        ls="--", label="tangent at w = 1, slope -16")
ax.plot([w0], [loss(w0)], "o", ms=9, color=PALETTE["action"][1])
ax.annotate("w = 1, L = 16\nslope dL/dw = -16:\ngoing right lowers L", xy=(w0, loss(w0)),
            xytext=(1.5, 24), fontsize=10, family=FONT, color=TEXT,
            arrowprops=dict(arrowstyle="-", color=TEXT, lw=0.8))

ax.plot([3.0], [0.0], "o", ms=9, color=PALETTE["data"][1])
ax.annotate("minimum: w = 3, slope 0", xy=(3.0, 0.0), xytext=(2.05, 8), fontsize=10,
            family=FONT, color=TEXT, arrowprops=dict(arrowstyle="-", color=TEXT, lw=0.8))

ax.set_xlim(-0.2, 5.2)
ax.set_ylim(-2, 40)
ax.set_xlabel("parameter w", fontsize=11, family=FONT, color=TEXT)
ax.set_ylabel("loss L(w)", fontsize=11, family=FONT, color=TEXT)
ax.set_title("A derivative is the slope of the tangent line", fontsize=13, fontweight="bold",
             family=FONT, color=TEXT)
ax.legend(prop={"family": FONT, "size": 10}, frameon=False, loc="upper right")
for spine in ("top", "right"):
    ax.spines[spine].set_visible(False)
ax.grid(alpha=0.25)

out = Path(__file__).with_suffix(".png")
fig.savefig(out, dpi=200, facecolor="white", bbox_inches="tight", metadata={"Software": None})
print("wrote", out.name)
