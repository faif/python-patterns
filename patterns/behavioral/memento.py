from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Memento:
    state: str


class Originator:
    def __init__(self, state: str) -> None:
        self._state = state

    def save(self) -> Memento:
        return Memento(self._state)

    def restore(self, memento: Memento) -> None:
        self._state = memento.state
        print(f"Originator: State restored to: {self._state}")

    def set_state(self, state: str) -> None:
        print(f"Originator: Setting state to: {state}")
        self._state = state


if __name__ == "__main__":
    originator = Originator("Initial State")
    caretaker: List[Memento] = []

    caretaker.append(originator.save())
    originator.set_state("State #1")

    caretaker.append(originator.save())
    originator.set_state("State #2")

    originator.restore(caretaker[0])
