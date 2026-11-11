"""Draw the nested map: generative AI inside deep learning inside machine learning inside AI.

Run:  python nested_map.py

Expected output:
    wrote nested_map.png
"""

import sys
from pathlib import Path

ROOT = next(p for p in Path(__file__).resolve().parents if (p / "shared").is_dir())
sys.path.insert(0, str(ROOT))

from shared.diagram_kit import Diagram  # noqa: E402

d = Diagram(title="The nested map: each field sits inside the one before it")

d.region("Artificial intelligence (AI)", 0, 0, 15, 8.4, depth=0,
         note="Any technique that makes machines do tasks we'd call intelligent.\n"
              "e.g. route planners, chess search, rule-based expert systems")
d.region("Machine learning (ML)", 0.6, 0.5, 14.4, 6.7, kind="data", depth=0,
         note="Systems that learn their behaviour from data instead of hand-written rules.\n"
              "e.g. spam filters, price estimates, recommendations")
d.region("Deep learning", 1.2, 1.0, 13.8, 5.0, kind="data", depth=2,
         note="Machine learning with neural networks of many layers.\n"
              "e.g. face recognition, speech-to-text, medical-image screening")
d.region("Generative AI", 1.8, 1.5, 13.2, 3.3, kind="action", depth=1,
         note="Deep learning models that create new content.\n"
              "e.g. chat assistants, image and music generators, code assistants")

print("wrote", d.save(Path(__file__).with_suffix(".png")).name)
