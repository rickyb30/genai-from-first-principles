"""Exercise (L1-02): score every three-day weather sequence with the chain rule.

The weather model from the lesson gives P(first day) and P(tomorrow | today). Your tasks:
  1. Complete sequence_log_prob(): return log P(sequence), using the chain rule
     P(a, b, c) = P(a) * P(b | a) * P(c | b), but ADD log-probabilities instead of
     multiplying probabilities.
  2. Complete sample_categorical(): the strip method from the lesson, with one uniform number.
  3. Run the file. If your function is right, the probabilities of all 27 possible
     three-day sequences add up to exactly 1. Why must they?
  4. Before running, predict the most likely three-day sequence, and P(rain, rain, rain).
  5. Stretch: estimate P(rain, rain, rain) by generating many sequences and counting how
     often it appears, using sample_categorical() for each day. How close is the estimate
     with 1,000 sequences? With 100,000?

The full solution is in solutions/three_day_forecasts.py.

Run:  python three_day_forecasts.py
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
    # TODO: start from math.log(START[first day]). Then, for each (today, tomorrow) pair of
    # neighbouring days (zip(sequence, sequence[1:]) gives them), add
    # math.log(TRANSITIONS[today, tomorrow]).
    return 0.0


def sample_categorical(probs: np.ndarray, u: float) -> int:
    """Index of the outcome whose slice of the 0-to-1 strip contains u (a uniform number)."""
    # TODO: keep a running total of probs. Return the first index i where u < running total.
    # If none is found (totals can add up to 0.99999...), return the last index.
    return 0


def main() -> None:
    all_sequences = list(itertools.product(range(3), repeat=3))
    log_probs = {seq: sequence_log_prob(seq) for seq in all_sequences}
    total = sum(math.exp(lp) for lp in log_probs.values())
    print(f"{len(all_sequences)} sequences, probabilities sum to {total:.6f}")

    print("most likely:")
    for seq in sorted(log_probs, key=lambda s: -log_probs[s])[:3]:
        words = " ".join(STATES[i] for i in seq)
        print(f"  {words:<20}  {math.exp(log_probs[seq]):.4f}   log-prob {log_probs[seq]:.3f}")

    print(f"P(rain, rain, rain) = {math.exp(log_probs[(2, 2, 2)]):.4f}")
    draws = ", ".join(f"u = {u:.2f} -> {STATES[sample_categorical(START, u)]}"
                      for u in (0.10, 0.62, 0.93))
    print(f"strip check: {draws}")


if __name__ == "__main__":
    main()
