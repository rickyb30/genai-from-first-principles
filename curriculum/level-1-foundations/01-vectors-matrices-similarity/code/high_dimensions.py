"""In many dimensions, random vectors are almost perpendicular to each other.

Draw pairs of random vectors (each entry from a standard normal distribution) and measure the
cosine similarity of each pair. In 2 dimensions, cosines are spread across the whole range
from -1 to 1. In 1,000 dimensions, nearly all of them sit close to 0. So a cosine of 0.3
would be extraordinary for random vectors with hundreds of dimensions. Learned vectors are not
random, though, and their typical cosines depend on the model (see the lesson's 🔴 section).

Run:  python high_dimensions.py

Expected output:
    dimensions   average |cosine|   1/sqrt(d)
             2              0.645       0.707
            10              0.260       0.316
           100              0.078       0.100
         1,000              0.025       0.032
"""

import numpy as np

PAIRS = 2_000


def random_cosines(dimensions: int, rng: np.random.Generator) -> np.ndarray:
    """Cosine similarity of PAIRS random vector pairs."""
    a = rng.standard_normal((PAIRS, dimensions))
    b = rng.standard_normal((PAIRS, dimensions))
    dots = (a * b).sum(axis=1)  # one dot product per row pair
    return dots / (np.linalg.norm(a, axis=1) * np.linalg.norm(b, axis=1))


def main() -> None:
    rng = np.random.default_rng(seed=0)
    print("dimensions   average |cosine|   1/sqrt(d)")
    for d in (2, 10, 100, 1_000):
        mean_abs = np.abs(random_cosines(d, rng)).mean()
        print(f"{d:>10,}   {mean_abs:>16.3f}   {1 / np.sqrt(d):>9.3f}")


if __name__ == "__main__":
    main()
