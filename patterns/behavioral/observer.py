"""
http://code.activestate.com/recipes/131499-observer-pattern/

*TL;DR
Maintains a list of dependents and notifies them of any state changes.

*Examples in Python ecosystem:
Django Signals: https://docs.djangoproject.com/en/3.1/topics/signals/
Flask Signals: https://flask.palletsprojects.com/en/1.1.x/signals/
"""

# observer.py

from __future__ import annotations
from typing import List

class Observer:
    def update(self, subject: Subject) -> None:
        """
        Receive update from the subject.

        Args:
            subject (Subject): The subject instance sending the update.
        """
        pass


class Subject:
    _observers: List[Observer]

    def __init__(self) -> None:
        """
        Initialize the subject with an empty observer list.
        """
        self._observers = []

    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.

        Args:
            observer (Observer): The observer instance to attach.
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.

        Args:
            observer (Observer): The observer instance to detach.
        """
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self) -> None:
        """
        Notify all attached observers by calling their update method.
        """
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


def main():
    """
    >>> data1 = Data('Data 1')
    >>> data2 = Data('Data 2')
    >>> view1 = DecimalViewer()
    >>> view2 = HexViewer()
    >>> data1.attach(view1)
    >>> data1.attach(view2)
    >>> data2.attach(view2)
    >>> data2.attach(view1)

    >>> data1.data = 10
    DecimalViewer: Subject Data 1 has data 10
    HexViewer: Subject Data 1 has data 0xa

    >>> data2.data = 15
    HexViewer: Subject Data 2 has data 0xf
    DecimalViewer: Subject Data 2 has data 15

    >>> data1.data = 3
    DecimalViewer: Subject Data 1 has data 3
    HexViewer: Subject Data 1 has data 0x3

    >>> data2.data = 5
    HexViewer: Subject Data 2 has data 0x5
    DecimalViewer: Subject Data 2 has data 5

    # Detach HexViewer from data1 and data2
    >>> data1.detach(view2)
    >>> data2.detach(view2)

    >>> data1.data = 10
    DecimalViewer: Subject Data 1 has data 10

    >>> data2.data = 15
    DecimalViewer: Subject Data 2 has data 15
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
