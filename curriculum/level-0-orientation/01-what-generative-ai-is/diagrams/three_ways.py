"""Draw the three ways a computer can produce an output: rules, learning and generation.

Run:  python three_ways.py

Expected output:
    wrote three_ways.png
"""

import sys
from pathlib import Path

ROOT = next(p for p in Path(__file__).resolve().parents if (p / "shared").is_dir())
sys.path.insert(0, str(ROOT))

from shared.diagram_kit import Diagram  # noqa: E402

d = Diagram(title="Three ways to get an output from a computer", box_size=(3.0, 1.1))

rows = [
    ("rules", 4.8, "Rules written\nby a person", "+ new data", "Program", "Answers", "default"),
    ("ml", 2.4, "Examples with\nanswers", "(labelled data)", "Learning", "Learned rules\n(a model)", "action"),
    ("gen", 0.0, "A prompt", "your question or request", "Generative\nmodel", "New content", "action"),
]
for key, y, inp, sub, proc, out, kind in rows:
    d.box(f"{key}_in", 0, y, inp, subtitle=sub, kind="data", h=1.4)
    d.box(f"{key}_proc", 4.6, y, proc, kind=kind, h=1.4)
    d.box(f"{key}_out", 9.2, y, out, kind="default", h=1.4)
    d.arrow(f"{key}_in", f"{key}_proc")
    d.arrow(f"{key}_proc", f"{key}_out")

d.group("1  Conventional software", ["rules_in", "rules_proc", "rules_out"], pad=0.3)
d.group("2  Machine learning", ["ml_in", "ml_proc", "ml_out"], pad=0.3)
d.group("3  Generative AI", ["gen_in", "gen_proc", "gen_out"], pad=0.3)

print("wrote", d.save(Path(__file__).with_suffix(".png")).name)
