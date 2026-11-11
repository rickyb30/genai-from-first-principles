"""Exercise (L0-03): what happens when you give the letter generator MORE context?

code/shannon_approximations.py went up to 4 letters of context. Your task:
  1. Generate 60 characters with 2, 6, 8 and 12 letters of context.
  2. For each result, find the longest run of characters that appears word-for-word in the
     source text.
  3. Explain what you see. Is more context always better when the source text is small?

Fill in the TODO in longest_copied_run(). The full solution is in solutions/more_context.py.

Run:  python more_context.py
"""

import random
import sys
from pathlib import Path

# Reuse the generator and source text from the lesson's code folder.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "code"))
from shannon_approximations import TEXT, clean, letters_order  # noqa: E402


def longest_copied_run(generated: str, source: str) -> int:
    """Length of the longest piece of `generated` that appears exactly in `source`."""
    # TODO: try every start position in `generated` and grow the piece while it is still
    # found in `source`. Return the longest length you find.
    return 0


if __name__ == "__main__":
    text = clean(TEXT)
    rng = random.Random(7)
    for context in (2, 6, 8, 12):
        sample = letters_order(text, context, 60, rng)
        print(f"{context:>2} letters of context: {sample}")
        print(f"   longest copied run: {longest_copied_run(sample, text)} of 60 characters")
