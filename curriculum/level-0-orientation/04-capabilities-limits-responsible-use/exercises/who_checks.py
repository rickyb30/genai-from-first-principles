"""Exercise (L0-04): decide how much checking a generated output needs.

The lesson's diagram asks two questions about any generated output:
  1. Could an error hurt someone, cost money, or break a rule or law?   -> a person reviews it first
  2. Otherwise: does it state facts someone will rely on?               -> check facts against sources
  3. Otherwise                                                          -> use it, and stay alert

Your task:
  * Answer the two questions (True or False) for each use below.
  * Implement decide() so it returns one of the three recommendations.

You can also do this on paper. The full solution is in solutions/who_checks.py.

Run:  python who_checks.py
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Use:
    description: str
    could_cause_harm: bool | None   # TODO: True or False (harm, money lost, or a rule broken)
    states_facts: bool | None       # TODO: True or False


def decide(use: Use) -> str:
    # TODO: return "a person reviews it first", "check facts against sources",
    # or "use it, and stay alert", following the two questions above.
    return "TODO"


USES = [
    Use("Ideas for a birthday message to a friend", None, None),
    Use("A plain-language summary of a medicine leaflet for a patient", None, None),
    Use("Ferry times for the town's tourism web page", None, None),
    Use("Name ideas for a new chess club", None, None),
    Use("A script that deletes old files on a shared server", None, None),
    Use("A summary of a long report, for your own reading", None, None),
]

if __name__ == "__main__":
    for use in USES:
        print(f"{use.description}\n   -> {decide(use)}")
