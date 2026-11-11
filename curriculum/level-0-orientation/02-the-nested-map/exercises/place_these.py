"""Exercise (L0-02): place six more systems on the nested map.

For each system below, replace every None with True or False by answering the four
questions in code/where_does_it_fit.py. Then run the file to see where each one lands.
If a result surprises you, decide whether your answers or the map's assumptions are wrong.

You can do this on paper too: answer the four questions, then follow the arrows in the
lesson's diagram.

The full solution is in solutions/place_these.py.

Run:  python place_these.py
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class System:
    name: str
    does_ai_task: bool | None
    learns_from_data: bool | None
    deep_network: bool | None
    generates: bool | None


def place(s: System) -> str:
    if None in (s.does_ai_task, s.learns_from_data, s.deep_network, s.generates):
        return "TODO: answer all four questions"
    if not s.does_ai_task:
        return "Not AI: conventional software"
    if not s.learns_from_data:
        return "AI, but not machine learning"
    if not s.deep_network:
        if s.generates:
            return "Machine learning: a simple generative model (not deep learning)"
        return "Machine learning, but not deep learning"
    if s.generates:
        return "Generative AI (deep learning that creates content)"
    return "Deep learning, but not generative"


SYSTEMS = [
    System("Thermostat that switches heating on below 19 °C", None, None, None, None),
    System("Route planner that searches a road map for the shortest path", None, None, None, None),
    System("Speech-to-text on a phone, using a deep network", None, None, None, None),
    System("Music generator that composes new melodies with a deep network", None, None, None, None),
    System("House-price estimator fitted to past sales with a straight line", None, None, None, None),
    System("Rule-based chatbot that fills in templates like 'Tell me more about X'", None, None, None, None),
]

if __name__ == "__main__":
    for s in SYSTEMS:
        print(f"{s.name}  ->  {place(s)}")
