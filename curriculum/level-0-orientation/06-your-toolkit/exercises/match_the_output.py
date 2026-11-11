"""Exercise (L0-06): make a program print exactly its expected output.

Every example in this catalog promises an exact output in its docstring. This exercise
practises that habit. Complete main() so the program prints EXACTLY these four lines:

    ferry departures: 7 per morning
    first: 07:00  last: 10:00
    gap between departures: 30 minutes
    ferries before 08:30: 3

Hints:
  * The departure times are in minutes after midnight, in the DEPARTURES list.
  * divmod(420, 60) gives (7, 0): 7 hours and 0 minutes.
  * f"{7:02d}" formats 7 as "07".

Then compare your output with the lines above, character by character. The full solution is
in solutions/match_the_output.py.

Run:  python match_the_output.py
"""

DEPARTURES = [420, 450, 480, 510, 540, 570, 600]  # minutes after midnight


def as_clock(minutes: int) -> str:
    # TODO: turn 420 into "07:00"
    return "??:??"


def main() -> None:
    # TODO: print the four lines shown in the docstring.
    print("ferry departures:", len(DEPARTURES))


if __name__ == "__main__":
    main()
