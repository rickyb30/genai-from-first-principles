"""Exercise (L0-05): plan your route through the catalog.

LEARNING_PATHS.md gives an approximate number of hours for each path, covering reading and
running the code. The catalog's rough estimate is that exercises add 30–50% on top; use 40%.

Your task:
  1. Set PATH_HOURS to the hours for your path and HOURS_PER_WEEK to what you can realistically
     give each week.
  2. Implement weeks_needed() so it returns the number of whole weeks needed, including an
     extra 40% for exercises. A partial week counts as a full week.
  3. Print the total hours including exercises, then a plan for three paces: half your pace,
     your pace, and double your pace.

The full solution is in solutions/plan_your_study.py.

Run:  python plan_your_study.py
"""

PATH_HOURS = 55        # for example, the software developer path
HOURS_PER_WEEK = 4
EXERCISE_EXTRA = 0.40


def weeks_needed(path_hours: float, hours_per_week: float) -> int:
    # TODO: total = path_hours * (1 + EXERCISE_EXTRA); round UP to whole weeks.
    return 0


if __name__ == "__main__":
    for pace in (HOURS_PER_WEEK / 2, HOURS_PER_WEEK, HOURS_PER_WEEK * 2):
        print(f"{pace:>4.1f} hours a week -> about {weeks_needed(PATH_HOURS, pace)} weeks")
