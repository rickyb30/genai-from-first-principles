"""Simulate the Leitner box system: the spaced-repetition method the catalog's flashcards use.

Every card starts in box 1. When you review a card:
  * remember it -> it moves up one box, and you see it again later
  * forget it   -> it goes back to box 1, and you see it again tomorrow
Higher boxes wait longer between reviews: 1, 2, 4, 8 and 16 days.

The "learner" here is simulated. The chance of remembering a card in each box is a made-up
number chosen for illustration, not a measurement. The point is the shape of the result: far
fewer reviews than studying every card every day, with most cards ending up well learned.

Run:  python leitner_boxes.py

Expected output:
    week 1:  78 reviews  [20, 7, 17, 7, 7, 5, 15]
    week 2:  36 reviews  [6, 7, 5, 7, 5, 5, 1]
    week 3:  31 reviews  [13, 2, 4, 3, 4, 4, 1]
    week 4:  14 reviews  [2, 2, 4, 2, 0, 3, 1]
    total with Leitner boxes : 159 reviews
    total, every card daily  : 560 reviews
    cards in each box at the end: box 1: 0  box 2: 1  box 3: 1  box 4: 3  box 5: 15
"""

import random

INTERVAL_DAYS = {1: 1, 2: 2, 3: 4, 4: 8, 5: 16}
# Illustrative only: the chance of recalling a card, by box.
RECALL_CHANCE = {1: 0.50, 2: 0.70, 3: 0.85, 4: 0.93, 5: 0.97}


def simulate(cards: int, days: int, rng: random.Random) -> tuple[list[int], dict[int, int]]:
    """Return the number of reviews on each day, and how many cards end in each box."""
    box = {c: 1 for c in range(cards)}
    due = {c: 0 for c in range(cards)}  # every card is due on day 0
    reviews_per_day = []
    for day in range(days):
        todays = [c for c in range(cards) if due[c] == day]
        for c in todays:
            if rng.random() < RECALL_CHANCE[box[c]]:
                box[c] = min(box[c] + 1, 5)
            else:
                box[c] = 1
            due[c] = day + INTERVAL_DAYS[box[c]]
        reviews_per_day.append(len(todays))
    final = {b: sum(1 for c in box if box[c] == b) for b in range(1, 6)}
    return reviews_per_day, final


def main() -> None:
    cards, days = 20, 28
    reviews, final = simulate(cards, days, random.Random(2006))
    for week in range(days // 7):
        week_reviews = reviews[week * 7:(week + 1) * 7]
        print(f"week {week + 1}: {sum(week_reviews):>3} reviews  {week_reviews}")
    print(f"total with Leitner boxes : {sum(reviews)} reviews")
    print(f"total, every card daily  : {cards * days} reviews")
    print("cards in each box at the end:", "  ".join(f"box {b}: {n}" for b, n in final.items()))


if __name__ == "__main__":
    main()
