"""Vectors, dot products, lengths and cosine similarity, first by hand and then with NumPy.

Each word gets a hand-made vector of three features: how much it has to do with water, with
books, and with travel. Real models learn their vectors (L2-02) and use hundreds of features
that nobody chose, but the arithmetic is exactly the same.

Run:  python word_vectors.py

Expected output:
    ferry   = [4, 0, 3]
    river   = [5, 0, 0]
    dot(ferry, river)     by hand: 20   with NumPy: 20
    length(ferry)         by hand: 5.0  with NumPy: 5.0
    cosine(ferry, river)  by hand: 0.8  with NumPy: 0.8

    cosine similarity to "ferry":
      ferry    1.000
      boat     0.960
      river    0.800
      train    0.600
      museum   0.360
      library  0.000

    distance vs cosine for "ferry" and "harbour" = [8, 0, 6]:
      dot 50   cosine 1.000   euclidean distance 5.000
"""

import math

import numpy as np

# Features:        water  books  travel
WORDS: dict[str, list[float]] = {
    "ferry":   [4, 0, 3],
    "boat":    [3, 0, 4],
    "river":   [5, 0, 0],
    "train":   [0, 0, 5],
    "museum":  [0, 4, 3],
    "library": [0, 5, 0],
}


def dot_by_hand(a: list[float], b: list[float]) -> float:
    """Multiply matching entries and add them up."""
    return sum(x * y for x, y in zip(a, b))


def length_by_hand(a: list[float]) -> float:
    """Pythagoras in any number of dimensions: the square root of the sum of squares."""
    return math.sqrt(sum(x * x for x in a))


def cosine_by_hand(a: list[float], b: list[float]) -> float:
    """Dot product divided by both lengths: the cosine of the angle between a and b."""
    return dot_by_hand(a, b) / (length_by_hand(a) * length_by_hand(b))


def cosine(a: np.ndarray, b: np.ndarray) -> float:
    """The same calculation in NumPy. `@` is the dot product."""
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))


def main() -> None:
    ferry, river = WORDS["ferry"], WORDS["river"]
    f, r = np.array(ferry), np.array(river)
    print("ferry   =", ferry)
    print("river   =", river)
    print(f"dot(ferry, river)     by hand: {dot_by_hand(ferry, river):g}   with NumPy: {f @ r:g}")
    print(f"length(ferry)         by hand: {length_by_hand(ferry)}  with NumPy: {np.linalg.norm(f)}")
    print(f"cosine(ferry, river)  by hand: {cosine_by_hand(ferry, river)}  with NumPy: {cosine(f, r)}")

    print('\ncosine similarity to "ferry":')
    scores = {word: cosine(f, np.array(vec)) for word, vec in WORDS.items()}
    for word, score in sorted(scores.items(), key=lambda item: -item[1]):
        print(f"  {word:<8} {score:.3f}")

    # "harbour" points the same way as "ferry" but is twice as long.
    harbour = np.array([8, 0, 6])
    print('\ndistance vs cosine for "ferry" and "harbour" = [8, 0, 6]:')
    print(f"  dot {f @ harbour:g}   cosine {cosine(f, harbour):.3f}   "
          f"euclidean distance {np.linalg.norm(f - harbour):.3f}")


if __name__ == "__main__":
    main()
