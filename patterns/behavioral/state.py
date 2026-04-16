from __future__ import annotations

from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def scan(self) -> None: ...


class AmState(State):
    def __init__(self, radio: Radio) -> None:
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0

    def scan(self) -> None:
        self.pos = (self.pos + 1) % len(self.stations)
        print(f"Scanning... Station is {self.stations[self.pos]} AM")


class FmState(State):
    def __init__(self, radio: Radio) -> None:
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0

    def scan(self) -> None:
        self.pos = (self.pos + 1) % len(self.stations)
        print(f"Scanning... Station is {self.stations[self.pos]} FM")


class Radio:
    def __init__(self) -> None:
        self.am_state = AmState(self)
        self.fm_state = FmState(self)
        self.state: State = self.am_state

    def toggle_am_fm(self) -> None:
        self.state = self.fm_state if self.state == self.am_state else self.am_state

    def scan(self) -> None:
        self.state.scan()


if __name__ == "__main__":
    radio = Radio()
    actions = [radio.scan] * 2 + [radio.toggle_am_fm] + [radio.scan] * 2
    for action in actions:
        action()
