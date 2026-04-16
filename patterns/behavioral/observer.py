from __future__ import annotations
from typing import List, Protocol

class Observer(Protocol):
    def update(self, subject: Subject) -> None: ...

class Subject:
    def __init__(self) -> None:
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

class Data(Subject):
    def __init__(self, name: str = "") -> None:
        super().__init__()
        self.name = name
        self._data = 0

    @property
    def data(self) -> int:
        return self._data

    @data.setter
    def data(self, value: int) -> None:
        self._data = value
        self.notify()

class HexViewer:
    def update(self, subject: Data) -> None:
        print(f"HexViewer: Subject {subject.name} has data 0x{subject.data:x}")

class DecimalViewer:
    def update(self, subject: Data) -> None:
        print(f"DecimalViewer: Subject {subject.name} has data {subject.data}")

if __name__ == "__main__":
    data1 = Data("Data 1")
    data1.attach(HexViewer())
    data1.attach(DecimalViewer())

    data1.data = 10
    data1.data = 15
