"""Draw four word vectors in the water-travel plane, and the angle between two of them.

"ferry", "boat", "river" and "train" all have 0 for the "books" feature, so they lie flat in
the 2-D plane of "water" and "travel" and can be drawn exactly. The arc marks the angle
between "ferry" and "river": its cosine, 0.8, is their cosine similarity.

Run:  python angle_between_words.py

Expected output:
    wrote angle_between_words.png
"""

import math
import sys
from pathlib import Path

ROOT = next(p for p in Path(__file__).resolve().parents if (p / "shared").is_dir())
sys.path.insert(0, str(ROOT))

import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Arc  # noqa: E402

from shared.diagram_kit import FONT, PALETTE, TEXT  # noqa: E402

VECTORS = {"ferry": (4, 3), "boat": (3, 4), "river": (5, 0), "train": (0, 5)}
STYLES = {"ferry": ("action", "-"), "boat": ("default", "--"), "river": ("data", "-"),
          "train": ("external", ":")}
LABEL_OFFSET = {"ferry": (0.15, -0.1), "boat": (-0.2, 0.15), "river": (0.1, 0.25),
                "train": (0.15, 0.1)}

fig, ax = plt.subplots(figsize=(6, 6))
for word, (x, y) in VECTORS.items():
    kind, style = STYLES[word]
    colour = PALETTE[kind][1]
    ax.annotate("", xy=(x, y), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color=colour, lw=2.4, linestyle=style,
                                mutation_scale=18))
    dx, dy = LABEL_OFFSET[word]
    ax.text(x + dx, y + dy, f"{word} ({x}, {y})", fontsize=11, fontweight="bold",
            color=TEXT, family=FONT)

angle = math.degrees(math.atan2(3, 4))  # angle of "ferry" above the "water" axis
ax.add_patch(Arc((0, 0), 2.6, 2.6, theta1=0, theta2=angle, color=PALETTE["action"][1], lw=1.8))
ax.text(1.5, 0.45, f"{angle:.1f}°\ncos = 0.8", fontsize=10, color=TEXT, family=FONT)

ax.set_xlim(-0.4, 6.4)
ax.set_ylim(-0.4, 6.0)
ax.set_aspect("equal")
ax.set_xlabel("water", fontsize=11, family=FONT, color=TEXT)
ax.set_ylabel("travel", fontsize=11, family=FONT, color=TEXT)
ax.grid(True, color="#DDDDDD", linewidth=0.8)
ax.set_title("Similar words point in similar directions", fontsize=13, fontweight="bold",
             family=FONT, color=TEXT, pad=12)
for spine in ("top", "right"):
    ax.spines[spine].set_visible(False)

out = Path(__file__).with_suffix(".png")
fig.savefig(out, dpi=200, facecolor="white", bbox_inches="tight", metadata={"Software": None})
print("wrote", out.name)
