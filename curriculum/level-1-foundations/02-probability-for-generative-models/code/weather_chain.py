"""A tiny generative model: Brindlewick's weather, one day at a time.

The weather station's log gives 100 pairs of consecutive days (today, tomorrow). From those
counts we compute joint, marginal and conditional probabilities, then generate a new fortnight
of weather by repeatedly sampling "tomorrow given today". Swap days for tokens and three kinds
of weather for a vocabulary of 50,000, and this is how a language model generates text.

Run:  python weather_chain.py

Expected output:
    joint counts (rows = today, columns = tomorrow):
              sunny cloudy   rain
      sunny      35     10      5
      cloudy     10     12      8
      rain        5      8      7

    P(today = sunny)                  = 0.50
    P(today = sunny, tomorrow = rain) = 0.05
    P(tomorrow = rain | today = sunny) = 0.10
    P(tomorrow = rain | today = rain)  = 0.35

    P(tomorrow | today):
              sunny cloudy   rain
      sunny   0.700  0.200  0.100
      cloudy  0.333  0.400  0.267
      rain    0.250  0.400  0.350

    P(sunny, sunny, rain) = 0.5 x 0.7 x 0.1 = 0.035

    a generated fortnight, starting sunny:
      sunny sunny cloudy rain sunny sunny cloudy sunny cloudy rain cloudy sunny sunny sunny
    share of days in 10,000 generated days: sunny 0.498  cloudy 0.297  rain 0.204
"""

import numpy as np

STATES = ["sunny", "cloudy", "rain"]

# How often each (today, tomorrow) pair appeared in 100 pairs of consecutive days.
JOINT_COUNTS = np.array([
    [35, 10, 5],   # today sunny
    [10, 12, 8],   # today cloudy
    [5, 8, 7],     # today rain
])


def print_table(table: np.ndarray, fmt: str) -> None:
    print("         " + " ".join(f"{s:>6}" for s in STATES))
    for state, row in zip(STATES, table):
        print(f"  {state:<7}" + " ".join(f"{x:{fmt}}" for x in row))


def generate(transitions: np.ndarray, start: int, days: int, rng: np.random.Generator) -> list[int]:
    """Repeatedly sample tomorrow's weather from P(tomorrow | today)."""
    sequence = [start]
    while len(sequence) < days:
        today = sequence[-1]
        sequence.append(int(rng.choice(len(STATES), p=transitions[today])))
    return sequence


def main() -> None:
    print("joint counts (rows = today, columns = tomorrow):")
    print_table(JOINT_COUNTS, "6d")

    joint = JOINT_COUNTS / JOINT_COUNTS.sum()          # P(today, tomorrow)
    marginal = joint.sum(axis=1)                       # P(today): add across each row
    transitions = joint / marginal[:, np.newaxis]      # P(tomorrow | today) = joint / marginal
    s, c, r = 0, 1, 2

    print(f"\nP(today = sunny)                  = {marginal[s]:.2f}")
    print(f"P(today = sunny, tomorrow = rain) = {joint[s, r]:.2f}")
    print(f"P(tomorrow = rain | today = sunny) = {transitions[s, r]:.2f}")
    print(f"P(tomorrow = rain | today = rain)  = {transitions[r, r]:.2f}")

    print("\nP(tomorrow | today):")
    print_table(transitions, "6.3f")

    # Chain rule: P(a, b, c) = P(a) * P(b | a) * P(c | b), when each day depends only on the last.
    p = marginal[s] * transitions[s, s] * transitions[s, r]
    print(f"\nP(sunny, sunny, rain) = {marginal[s]:.1f} x {transitions[s, s]:.1f} x "
          f"{transitions[s, r]:.1f} = {p:.3f}")

    rng = np.random.default_rng(seed=7)
    fortnight = generate(transitions, start=s, days=14, rng=rng)
    print("\na generated fortnight, starting sunny:")
    print("  " + " ".join(STATES[i] for i in fortnight))

    long_run = np.bincount(generate(transitions, start=s, days=10_000, rng=rng), minlength=3) / 10_000
    print("share of days in 10,000 generated days: "
          + "  ".join(f"{state} {share:.3f}" for state, share in zip(STATES, long_run)))


if __name__ == "__main__":
    main()
