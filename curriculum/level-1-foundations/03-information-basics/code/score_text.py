"""Score text with three character models, and measure each with cross-entropy and perplexity.

A model's cross-entropy on a text is its average surprisal per character: the mean of
-log2 P(character) over the text. This is the same number a language model is trained to
lower (its loss), just with characters and a very simple model.

The three models:
  uniform    every one of 27 symbols (a-z and space) equally likely
  counted    each symbol's share of the training text, no smoothing
  smoothed   the same counts, plus 1 for every symbol so nothing has probability 0

Run:  python score_text.py

Expected output:
    training text: 354 characters   test text: 80 characters
    symbols in the test text that never appear in training: ['j', 'z']

    model      train bits/char  train perplexity   test bits/char  test perplexity
      uniform         4.755           27.00              4.755           27.00
      counted         4.075           16.85                inf             inf
      smoothed        4.087           16.99              4.248           19.00

    log2(27) = 4.755 bits, so a uniform guess has perplexity 27
"""

import math
from collections import Counter

SYMBOLS = "abcdefghijklmnopqrstuvwxyz "

TRAIN = """
Brindlewick sits where the river meets the harbour. The ferry leaves the east pier every
hour from six in the morning until nine at night, and the library opens at ten on weekdays.
On market days the square fills with stalls selling bread, honey, apples and wool. Visitors
should carry a map, because the old lanes bend and the signposts are often hidden by ivy.
"""

TEST = "the museum by the harbour is open on sunday and visitors can join a quiz at noon"


def clean(text: str) -> str:
    """Lowercase, keep a-z, and turn everything else into single spaces."""
    kept = "".join(ch if ch in SYMBOLS else " " for ch in text.lower())
    return " ".join(kept.split())


def uniform_model() -> dict[str, float]:
    return {s: 1 / len(SYMBOLS) for s in SYMBOLS}


def counted_model(text: str, add: int = 0) -> dict[str, float]:
    """Each symbol's probability is (its count + add) / (total + add * 27)."""
    counts = Counter(text)
    total = len(text) + add * len(SYMBOLS)
    return {s: (counts[s] + add) / total for s in SYMBOLS}


def cross_entropy_bits(model: dict[str, float], text: str) -> float:
    """Average surprisal per character, in bits. Infinite if any character has probability 0."""
    total = 0.0
    for ch in text:
        if model[ch] == 0:
            return math.inf
        total += -math.log2(model[ch])
    return total / len(text)


def main() -> None:
    train, test = clean(TRAIN), clean(TEST)
    print(f"training text: {len(train)} characters   test text: {len(test)} characters")
    unseen = sorted(set(test) - set(train))
    print(f"symbols in the test text that never appear in training: {unseen}")

    models = {
        "uniform": uniform_model(),
        "counted": counted_model(train),
        "smoothed": counted_model(train, add=1),
    }
    print("\nmodel      train bits/char  train perplexity   test bits/char  test perplexity")
    for name, model in models.items():
        h_train = cross_entropy_bits(model, train)
        h_test = cross_entropy_bits(model, test)
        print(f"  {name:<9}  {h_train:>10.3f}  {2 ** h_train:>14.2f}  "
              f"{h_test:>17.3f}  {2 ** h_test:>14.2f}")

    print(f"\nlog2(27) = {math.log2(27):.3f} bits, so a uniform guess has perplexity 27")


if __name__ == "__main__":
    main()
