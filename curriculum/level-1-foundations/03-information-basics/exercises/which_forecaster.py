"""Exercise (L1-03): rank four weather forecasters by cross-entropy on a real log.

Each forecaster sees yesterday's weather and gives a distribution for today. Score each one by
the average surprisal (in bits) of what actually happened. That's its cross-entropy on the log:
lower is better, and perplexity = 2 ** cross-entropy.

Your tasks:
  1. Complete average_surprisal(). Return the mean of -log2(p) over the list, or math.inf if
     any p is 0.
  2. Before running, predict the ranking on the 14-day fortnight and on 5,000 generated days.
     Which forecaster knows the real rules of the weather?
  3. Run the file. Why can the ranking differ between the two logs?
  4. Why does no_rain score infinity, and what does smoothed_no_rain do about it?
  5. Stretch: write your own forecaster and try to beat transition on the long log. (You
     can't, on average. L1-03's "Going deeper" section says why.)

The full solution is in solutions/which_forecaster.py.

Run:  python which_forecaster.py
"""

import math
import random

STATES = ["sunny", "cloudy", "rain"]
LOG = ("sunny sunny cloudy rain sunny sunny cloudy "
       "sunny cloudy rain cloudy sunny sunny sunny").split()   # the fortnight from L1-02

TRANSITIONS = {                          # P(today | yesterday), from L1-02
    "sunny": (0.70, 0.20, 0.10),
    "cloudy": (10 / 30, 12 / 30, 8 / 30),
    "rain": (0.25, 0.40, 0.35),
}


def climate(yesterday: str) -> tuple[float, ...]:
    return (0.5, 0.3, 0.2)                                   # ignores yesterday


def persistence(yesterday: str) -> tuple[float, ...]:
    return tuple(0.8 if s == yesterday else 0.1 for s in STATES)  # "same as yesterday"


def transition(yesterday: str) -> tuple[float, ...]:
    return TRANSITIONS[yesterday]


def no_rain(yesterday: str) -> tuple[float, ...]:
    return (0.6, 0.4, 0.0)                                   # certain it never rains


def smoothed_no_rain(yesterday: str) -> tuple[float, ...]:
    """Mix 90% of the no-rain forecast with 10% of a uniform guess, so nothing is impossible."""
    return tuple(0.9 * q + 0.1 / len(STATES) for q in no_rain(yesterday))


def average_surprisal(probabilities: list[float]) -> float:
    """Mean of -log2(p) over the probabilities given to what actually happened."""
    # TODO: if any p is 0, return math.inf. Otherwise return the mean of -math.log2(p).
    return 0.0


def generate_log(days: int, seed: int) -> list[str]:
    """Generate a long log from the transition table (the true model behind the weather)."""
    rng = random.Random(seed)
    log = ["sunny"]
    while len(log) < days:
        log.append(rng.choices(STATES, weights=TRANSITIONS[log[-1]])[0])
    return log


def score(forecaster, log: list[str]) -> float:
    probabilities = []
    for yesterday, today in zip(log, log[1:]):
        forecast = forecaster(yesterday)
        probabilities.append(forecast[STATES.index(today)])
    return average_surprisal(probabilities)


def main() -> None:
    forecasters = [climate, persistence, transition, no_rain, smoothed_no_rain]
    for title, log in [("the fortnight", LOG), ("5,000 generated days", generate_log(5000, seed=11))]:
        print(f"{title}: {len(log) - 1:,} forecasts scored")
        scores = {f.__name__: score(f, log) for f in forecasters}
        for name in sorted(scores, key=scores.get):
            h = scores[name]
            print(f"  {name:<17} cross-entropy {h:6.3f} bits/day   perplexity {2 ** h:6.3f}")


if __name__ == "__main__":
    main()
