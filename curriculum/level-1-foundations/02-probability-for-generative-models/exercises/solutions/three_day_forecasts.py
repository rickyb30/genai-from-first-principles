"""Solution (L1-02): score every three-day weather sequence with the chain rule.

The chain rule gives P(a, b, c) = P(a) * P(b | a) * P(c | b) for this model, because each day
depends only on the day before. Working in log-probabilities (adding instead of multiplying)
is how real models score long sequences without the result rounding to zero.

Run:  python three_day_forecasts.py

Expected output:
    27 sequences, probabilities sum to 1.000000
    most likely:
      sunny sunny sunny     0.2450   log-prob -1.406
      sunny sunny cloudy    0.0700   log-prob -2.659
      cloudy sunny sunny    0.0700   log-prob -2.659
    P(rain, rain, rain) = 0.0245
    strip check: u = 0.10 -> sunny, u = 0.62 -> cloudy, u = 0.93 -> rain
    estimated from 100,000 generated sequences: 0.0250
"""

import itertools
import math

import numpy as np

STATES = ["sunny", "cloudy", "rain"]
START = np.array([0.5, 0.3, 0.2])            # P(first day)
TRANSITIONS = np.array([                      # P(tomorrow | today), rows = today
    [0.70, 0.20, 0.10],
    [10 / 30, 12 / 30, 8 / 30],
    [0.25, 0.40, 0.35],
])


def sequence_log_prob(sequence: tuple[int, ...]) -> float:
    """log P(sequence) = log P(first) + sum of log P(next | previous)."""
    total = math.log(START[sequence[0]])
    for today, tomorrow in zip(sequence, sequence[1:]):
        total += math.log(TRANSITIONS[today, tomorrow])
    return total


def sample_categorical(probs: np.ndarray, u: float) -> int:
    """Index of the outcome whose slice of the 0-to-1 strip contains u (a uniform number)."""
    running = 0.0
    for i, p in enumerate(probs):
        running += p
        if u < running:
            return i
    return len(probs) - 1    # guard: totals can add up to 0.99999...


def sample_sequences(count: int, days: int, rng: np.random.Generator) -> np.ndarray:
    """Generate `count` sequences at once: sample the first day, then each next day given the last.

    Each step draws one uniform number per sequence and finds where it lands in the running
    totals of the right row (the strip from the lesson), for all sequences in parallel.
    """
    first = np.searchsorted(np.cumsum(START), rng.random(count), side="right")
    columns = [first]
    cumulative = np.cumsum(TRANSITIONS, axis=1)
    for _ in range(days - 1):
        rows = cumulative[columns[-1]]                     # each sequence's P(next | last), as totals
        u = rng.random(count)[:, np.newaxis]
        passed = (u >= rows).sum(axis=1)                   # how many totals u has passed
        columns.append(np.minimum(passed, len(STATES) - 1))  # guard against totals of 0.99999...
    return np.stack(columns, axis=1)


def main() -> None:
    all_sequences = list(itertools.product(range(3), repeat=3))
    log_probs = {seq: sequence_log_prob(seq) for seq in all_sequences}
    total = sum(math.exp(lp) for lp in log_probs.values())
    print(f"{len(all_sequences)} sequences, probabilities sum to {total:.6f}")

    print("most likely:")
    for seq in sorted(log_probs, key=lambda s: -log_probs[s])[:3]:
        words = " ".join(STATES[i] for i in seq)
        print(f"  {words:<20}  {math.exp(log_probs[seq]):.4f}   log-prob {log_probs[seq]:.3f}")

    rain3 = (2, 2, 2)
    print(f"P(rain, rain, rain) = {math.exp(log_probs[rain3]):.4f}")
    draws = ", ".join(f"u = {u:.2f} -> {STATES[sample_categorical(START, u)]}"
                      for u in (0.10, 0.62, 0.93))
    print(f"strip check: {draws}")
    rng = np.random.default_rng(seed=3)
    n = 100_000
    samples = sample_sequences(n, 3, rng)
    hits = int(np.all(samples == rain3, axis=1).sum())
    print(f"estimated from {n:,} generated sequences: {hits / n:.4f}")


if __name__ == "__main__":
    main()
