"""Solution (L0-06): make a program print exactly its expected output.

Small details matter when you compare output exactly: "07:00" vs "7:00", or a missing word.
Exact comparison is strict on purpose. It catches real bugs that a quick glance misses.

Run:  python match_the_output.py

Expected output:
    ferry departures: 7 per morning
    first: 07:00  last: 10:00
    gap between departures: 30 minutes
    ferries before 08:30: 3
"""

DEPARTURES = [420, 450, 480, 510, 540, 570, 600]  # minutes after midnight


def as_clock(minutes: int) -> str:
    hours, mins = divmod(minutes, 60)
    return f"{hours:02d}:{mins:02d}"


def main() -> None:
    print(f"ferry departures: {len(DEPARTURES)} per morning")
    print(f"first: {as_clock(DEPARTURES[0])}  last: {as_clock(DEPARTURES[-1])}")
    print(f"gap between departures: {DEPARTURES[1] - DEPARTURES[0]} minutes")
    print(f"ferries before 08:30: {sum(1 for d in DEPARTURES if d < 8 * 60 + 30)}")


if __name__ == "__main__":
    main()
