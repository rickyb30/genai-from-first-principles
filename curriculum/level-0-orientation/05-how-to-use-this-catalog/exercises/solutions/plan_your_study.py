"""Solution (L0-05): plan your route through the catalog.

math.ceil rounds up, so a plan that needs 19.25 weeks becomes 20 weeks. Notice how much the
pace matters: a steady few hours every week finishes a long path in months, not years.
A regular schedule also helps your memory: spaced study beats the same hours crammed together.

Run:  python plan_your_study.py

Expected output:
    path: 55 h of reading and code, about 77 h with exercises
     2.0 hours a week -> about 39 weeks
     4.0 hours a week -> about 20 weeks
     8.0 hours a week -> about 10 weeks
"""

import math

PATH_HOURS = 55
HOURS_PER_WEEK = 4
EXERCISE_EXTRA = 0.40


def weeks_needed(path_hours: float, hours_per_week: float) -> int:
    total = path_hours * (1 + EXERCISE_EXTRA)
    return math.ceil(total / hours_per_week)


if __name__ == "__main__":
    print(f"path: {PATH_HOURS} h of reading and code, about {PATH_HOURS * (1 + EXERCISE_EXTRA):.0f} h with exercises")
    for pace in (HOURS_PER_WEEK / 2, HOURS_PER_WEEK, HOURS_PER_WEEK * 2):
        print(f"{pace:>4.1f} hours a week -> about {weeks_needed(PATH_HOURS, pace)} weeks")
