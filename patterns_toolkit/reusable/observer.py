"""
Reusable Observer Pattern Template
===================================
Copy this file into your project and customize the concrete observers
to fit your domain. The Subject base class works as-is.

Usage:
    1. Create concrete observers by inheriting from Observer
    2. Implement the update() method in each observer
    3. Attach observers to a subject
    4. When the subject's state changes, call self.notify()
"""

from __future__ import annotations
from typing import List


class Observer:
    """Base observer interface. Subclass this and implement update()."""

    def update(self, subject: Subject) -> None:
        raise NotImplementedError("Subclasses must implement update()")


class Subject:
    """
    Base subject that maintains a list of observers and notifies them
    automatically when state changes.
    """

    def __init__(self) -> None:
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        """Subscribe an observer to receive updates."""
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """Unsubscribe an observer from receiving updates."""
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self) -> None:
        """Notify all attached observers by calling their update method."""
        for observer in self._observers:
            observer.update(self)