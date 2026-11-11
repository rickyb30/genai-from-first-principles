"""diagram_kit — draw workflow and architecture diagrams as PNG files.

A tiny layer over matplotlib so that every diagram in the catalog:
  * is generated from Python source kept next to the lesson (reviewable in diffs),
  * renders offline and deterministically,
  * uses one consistent, colour-blind-safe palette (Okabe & Ito, 2008),
  * has a white background so it reads well in light and dark page themes.

Usage:
    from shared.diagram_kit import Diagram
    d = Diagram(title="Agent loop")
    d.box("think", 0, 0, "Reason")
    d.box("act", 3, 0, "Act", kind="action")
    d.arrow("think", "act", label="tool call")
    d.save("agent_loop.png")
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # headless: no window, works in CI
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

# Okabe–Ito colour-blind-safe palette, lightened for fills.
PALETTE = {
    "default": ("#DCEBF7", "#0072B2"),  # fill, edge (blue)
    "action": ("#FBE3CC", "#D55E00"),   # vermillion
    "data": ("#D5EFE6", "#009E73"),     # bluish green
    "human": ("#FDF1C7", "#B8860B"),    # yellow (darkened edge for contrast)
    "external": ("#EEEEEE", "#555555"), # grey: things outside the system
    "risk": ("#F6D6E6", "#CC79A7"),     # reddish purple
}
TEXT = "#1A1A1A"
FONT = "DejaVu Sans"  # ships with matplotlib, so output is identical everywhere
CHAR_WIDTH = 0.125  # approximate width of one bold 11 pt character, in diagram units


@dataclass
class _Box:
    x: float
    y: float
    w: float
    h: float

    def edge_point(self, tx: float, ty: float) -> tuple[float, float]:
        """Point where the line from this box's centre towards (tx, ty) leaves the box."""
        dx, dy = tx - self.x, ty - self.y
        if dx == 0 and dy == 0:
            return self.x, self.y
        sx = (self.w / 2) / abs(dx) if dx else float("inf")
        sy = (self.h / 2) / abs(dy) if dy else float("inf")
        s = min(sx, sy)
        return self.x + dx * s, self.y + dy * s


def _mix(a: str, b: str, t: float) -> str:
    """Blend two hex colours: t=0 gives a, t=1 gives b."""
    ca = [int(a[i:i + 2], 16) for i in (1, 3, 5)]
    cb = [int(b[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(x + (y - x) * t):02X}" for x, y in zip(ca, cb))


class Diagram:
    def __init__(self, title: str | None = None, box_size: tuple[float, float] = (2.0, 1.0)):
        self.title = title
        self.box_w, self.box_h = box_size
        self.boxes: dict[str, _Box] = {}
        self.regions: list[tuple[float, float, float, float]] = []
        self.notes: list[tuple[float, float]] = []
        self.fig, self.ax = plt.subplots()
        self.ax.set_axis_off()
        self.ax.set_aspect("equal")

    def box(self, key, x, y, label, kind="default", w=None, h=None, subtitle=None):
        # Widen automatically so the longest label line always fits inside the box.
        longest = max(len(line) for line in label.split("\n"))
        w = max(w or self.box_w, longest * CHAR_WIDTH + 0.45)
        h = h or self.box_h
        fill, edge = PALETTE[kind]
        self.ax.add_patch(FancyBboxPatch(
            (x - w / 2, y - h / 2), w, h,
            boxstyle="round,pad=0.02,rounding_size=0.12",
            facecolor=fill, edgecolor=edge, linewidth=2, zorder=2))
        if subtitle:
            self.ax.text(x, y + h * 0.13, label, ha="center", va="center", fontsize=11,
                         fontweight="bold", color=TEXT, family=FONT, zorder=3)
            self.ax.text(x, y - h * 0.22, subtitle, ha="center", va="center", fontsize=8.5,
                         color="#444444", family=FONT, zorder=3)
        else:
            self.ax.text(x, y, label, ha="center", va="center", fontsize=11,
                         fontweight="bold", color=TEXT, family=FONT, zorder=3)
        self.boxes[key] = _Box(x, y, w, h)

    def arrow(self, src, dst, label=None, curve=0.0, dashed=False):
        a, b = self.boxes[src], self.boxes[dst]
        start = a.edge_point(b.x, b.y)
        end = b.edge_point(a.x, a.y)
        self.ax.add_patch(FancyArrowPatch(
            start, end, arrowstyle="-|>", mutation_scale=16, linewidth=1.6,
            color="#333333", linestyle="--" if dashed else "-",
            connectionstyle=f"arc3,rad={curve}", zorder=1))
        if label:
            mx, my = (start[0] + end[0]) / 2, (start[1] + end[1]) / 2
            # For an arc3 curve, the Bezier midpoint sits at chord-midpoint + rad/2 * (dy, -dx).
            nx, ny = (end[1] - start[1]) * curve * 0.5, -(end[0] - start[0]) * curve * 0.5
            ha = "center"
            vertical = abs(end[1] - start[1]) > abs(end[0] - start[0])
            if vertical and nx != 0:
                # Put the label beside a curved vertical arrow, on its outer side, so that
                # labels of opposite arrows never overlap.
                ha = "left" if nx > 0 else "right"
                nx += 0.12 if nx > 0 else -0.12
            self.ax.text(mx + nx, my + ny, label, ha=ha, va="center", fontsize=8.5,
                         color=TEXT, family=FONT, zorder=4,
                         bbox=dict(facecolor="white", edgecolor="none", pad=1.5))

    def group(self, label, keys, pad=0.35, kind="external"):
        """Dashed boundary around several boxes (e.g. a trust boundary or a level band)."""
        bs = [self.boxes[k] for k in keys]
        x0 = min(b.x - b.w / 2 for b in bs) - pad
        x1 = max(b.x + b.w / 2 for b in bs) + pad
        y0 = min(b.y - b.h / 2 for b in bs) - pad
        y1 = max(b.y + b.h / 2 for b in bs) + pad + 0.25
        _, edge = PALETTE[kind]
        self.ax.add_patch(FancyBboxPatch(
            (x0, y0), x1 - x0, y1 - y0, boxstyle="round,pad=0,rounding_size=0.15",
            facecolor="none", edgecolor=edge, linewidth=1.3, linestyle=(0, (5, 4)), zorder=0))
        self.ax.text(x0 + 0.12, y1 - 0.15, label, ha="left", va="top", fontsize=9,
                     color=edge, family=FONT, style="italic")

    def region(self, label, x0, y0, x1, y1, kind="default", depth=0, note=None):
        """A filled, labelled area drawn behind boxes. Nest regions to show "A contains B".

        Draw outer regions first. `depth` darkens the fill so nested regions stay distinct.
        """
        fill, edge = PALETTE[kind]
        shade = _mix(fill, edge, min(0.12 * depth, 0.5))
        z = 0.1 + 0.01 * len(self.regions)  # later (inner) regions sit on top
        self.ax.add_patch(FancyBboxPatch(
            (x0, y0), x1 - x0, y1 - y0, boxstyle="round,pad=0,rounding_size=0.25",
            facecolor=shade, edgecolor=edge, linewidth=2, zorder=z))
        self.ax.text(x0 + 0.25, y1 - 0.25, label, ha="left", va="top", fontsize=12,
                     fontweight="bold", color=TEXT, family=FONT, zorder=z + 0.005)
        if note:
            self.ax.text(x0 + 0.25, y1 - 0.75, note, ha="left", va="top", fontsize=9,
                         color="#333333", family=FONT, zorder=z + 0.005)
        self.regions.append((x0, y0, x1, y1))

    def note(self, x, y, text, ha="center"):
        """Free-standing small text, for annotations that don't belong in a box."""
        self.ax.text(x, y, text, ha=ha, va="center", fontsize=9, color="#333333",
                     family=FONT, zorder=4)
        self.notes.append((x, y))

    def save(self, path, dpi=200):
        xs = [b.x - b.w / 2 for b in self.boxes.values()] + [b.x + b.w / 2 for b in self.boxes.values()]
        ys = [b.y - b.h / 2 for b in self.boxes.values()] + [b.y + b.h / 2 for b in self.boxes.values()]
        xs += [r[0] for r in self.regions] + [r[2] for r in self.regions] + [n[0] for n in self.notes]
        ys += [r[1] for r in self.regions] + [r[3] for r in self.regions] + [n[1] for n in self.notes]
        m = 0.6
        self.ax.set_xlim(min(xs) - m, max(xs) + m)
        self.ax.set_ylim(min(ys) - m, max(ys) + m)
        width = max(xs) - min(xs) + 2 * m
        height = max(ys) - min(ys) + 2 * m + (0.5 if self.title else 0)
        self.fig.set_size_inches(width * 0.9, height * 0.9)
        if self.title:
            # Attached to the drawing (not the figure), so no empty band appears under it.
            self.ax.set_title(self.title, fontsize=13, fontweight="bold", color=TEXT,
                              family=FONT, pad=12)
        self.fig.savefig(path, dpi=dpi, facecolor="white", bbox_inches="tight",
                         metadata={"Software": None})  # no version stamp → stable bytes
        plt.close(self.fig)
        return Path(path)
