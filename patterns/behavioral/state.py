"""
Implementation of the state pattern

http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/

*TL;DR
Implements state as a derived class of the state pattern interface.
Implements state transitions by invoking methods from the pattern's superclass.
"""

from __future__ import annotations


class State:

    """Base state. This is to share functionality"""

    def scan(self: AmState) -> None:
        """Scan the dial to the next station"""
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print(f"Scanning... Station is {self.stations[self.pos]} {self.name}")


class AmState(State):
    def __init__(self, radio) -> None:
        self.radio: Radio = radio
        self.stations: list[str] = ["1250", "1380", "1510"]
        self.pos: int = 0
        self.name: str = "AM"

    def toggle_amfm(self) -> None:
        print("Switching to FM")
        self.radio.state = self.radio.fmstate


class FmState(State):
    def __init__(self, radio) -> None:
        self.radio: Radio = radio
        self.stations: list[str] = ["81.3", "89.1", "103.9"]
        self.pos: int = 0
        self.name: str = "FM"

    def toggle_amfm(self) -> None:
        print("Switching to AM")
        self.radio.state = self.radio.amstate


class Radio:

    """A radio.     It has a scan button, and an AM/FM toggle switch."""

    def __init__(self) -> None:
        """We have an AM state and an FM state"""
        self.amstate: AmState = AmState(self)
        self.fmstate: FmState = FmState(self)
        self.state: AmState = self.amstate

    def toggle_amfm(self) -> None:
        self.state.toggle_amfm()

    def scan(self) -> None:
        self.state.scan()


def main():
    """
    >>> radio = Radio()
    >>> actions = [radio.scan] * 2 + [radio.toggle_amfm] + [radio.scan] * 2
    >>> actions *= 2

    >>> for action in actions:
    ...    action()
    Scanning... Station is 1380 AM
    Scanning... Station is 1510 AM
    Switching to FM
    Scanning... Station is 89.1 FM
    Scanning... Station is 103.9 FM
    Scanning... Station is 81.3 FM
    Scanning... Station is 89.1 FM
    Switching to AM
    Scanning... Station is 1250 AM
    Scanning... Station is 1380 AM
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
