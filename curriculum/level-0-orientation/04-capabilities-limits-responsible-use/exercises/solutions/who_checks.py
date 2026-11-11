"""Solution (L0-04): how much checking does a generated output need?

Reasoning for the less obvious cases:
  * Medicine summary: a wrong dose or a missing warning can hurt someone. A qualified person
    reviews it, even if it reads perfectly.
  * Ferry times: an error is an inconvenience, not a danger, but people will rely on the times,
    so check them against the official timetable.
  * Deleting files: a mistake can destroy work, so a person reviews it, and ideally tests it
    on copies first.
  * Report summary for yourself: it states facts, so check anything you'll repeat or act on.
    Being "just for me" lowers the stakes, but not the error rate.

Run:  python who_checks.py

Expected output:
    Ideas for a birthday message to a friend
       -> use it, and stay alert
    A plain-language summary of a medicine leaflet for a patient
       -> a person reviews it first
    Ferry times for the town's tourism web page
       -> check facts against sources
    Name ideas for a new chess club
       -> use it, and stay alert
    A script that deletes old files on a shared server
       -> a person reviews it first
    A summary of a long report, for your own reading
       -> check facts against sources
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Use:
    description: str
    could_cause_harm: bool
    states_facts: bool


def decide(use: Use) -> str:
    if use.could_cause_harm:
        return "a person reviews it first"
    if use.states_facts:
        return "check facts against sources"
    return "use it, and stay alert"


USES = [
    Use("Ideas for a birthday message to a friend", False, False),
    Use("A plain-language summary of a medicine leaflet for a patient", True, True),
    Use("Ferry times for the town's tourism web page", False, True),
    Use("Name ideas for a new chess club", False, False),
    Use("A script that deletes old files on a shared server", True, False),
    Use("A summary of a long report, for your own reading", False, True),
]

if __name__ == "__main__":
    for use in USES:
        print(f"{use.description}\n   -> {decide(use)}")
