"""Sampling from a categorical distribution, from scratch.

Every time a generative model picks its next token, it samples from a categorical
distribution: a fixed list of outcomes, each with a probability. This file builds a sampler
from one uniform random number and a running total (the cumulative distribution), checks it
against NumPy's built-in sampler, turns raw scores into probabilities with softmax, and shows
why models add log-probabilities instead of multiplying probabilities.

Run:  python sampling.py

Expected output:
    probabilities: sunny 0.5  cloudy 0.3  rain 0.2
    cumulative:    [0.5 0.8 1. ]
    u = 0.10 -> sunny
    u = 0.62 -> cloudy
    u = 0.93 -> rain

    sample frequencies (ours, then NumPy's):
           10 draws: sunny 0.300 cloudy 0.400 rain 0.300 | sunny 0.500 cloudy 0.200 rain 0.300
          100 draws: sunny 0.450 cloudy 0.290 rain 0.260 | sunny 0.460 cloudy 0.280 rain 0.260
       10,000 draws: sunny 0.501 cloudy 0.298 rain 0.201 | sunny 0.494 cloudy 0.307 rain 0.200

    scores [2.0, 1.0, 0.5] -> softmax [0.629, 0.231, 0.14]

    1,000 tokens, each with probability 0.1:
      multiplying probabilities: 0.0
      adding log-probabilities:  -2302.585
"""

import math

import numpy as np

STATES = ["sunny", "cloudy", "rain"]
PROBS = np.array([0.5, 0.3, 0.2])


def sample_categorical(probs: np.ndarray, u: float) -> int:
    """Return the first outcome whose running total of probability exceeds u (0 <= u < 1)."""
    total = 0.0
    for outcome, p in enumerate(probs):
        total += p
        if u < total:
            return outcome
    return len(probs) - 1  # guards against rounding when the probabilities sum to 0.99999...


def softmax(scores: np.ndarray) -> np.ndarray:
    """Turn any real-valued scores into probabilities that sum to 1."""
    exps = np.exp(scores - scores.max())  # subtracting the max avoids overflow; same result
    return exps / exps.sum()


def frequencies(samples: list[int] | np.ndarray) -> str:
    counts = np.bincount(samples, minlength=len(STATES)) / len(samples)
    return " ".join(f"{s} {c:.3f}" for s, c in zip(STATES, counts))


def main() -> None:
    print("probabilities: " + "  ".join(f"{s} {p}" for s, p in zip(STATES, PROBS)))
    print("cumulative:   ", np.cumsum(PROBS))
    for u in (0.10, 0.62, 0.93):
        print(f"u = {u:.2f} -> {STATES[sample_categorical(PROBS, u)]}")

    rng = np.random.default_rng(seed=0)
    print("\nsample frequencies (ours, then NumPy's):")
    for n in (10, 100, 10_000):
        ours = [sample_categorical(PROBS, rng.random()) for _ in range(n)]
        numpys = rng.choice(len(STATES), size=n, p=PROBS)
        print(f"{n:>9,} draws: {frequencies(ours)} | {frequencies(numpys)}")

    scores = np.array([2.0, 1.0, 0.5])
    print(f"\nscores {scores.tolist()} -> softmax {np.round(softmax(scores), 3).tolist()}")

    print("\n1,000 tokens, each with probability 0.1:")
    print("  multiplying probabilities:", math.prod([0.1] * 1000))
    print(f"  adding log-probabilities:  {sum(math.log(0.1) for _ in range(1000)):.3f}")


if __name__ == "__main__":
    main()
