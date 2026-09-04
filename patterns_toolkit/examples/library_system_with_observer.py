"""
Example: Observer Pattern Applied to a Library Management System
=================================================================
This example shows how the Observer pattern can be used to notify
users when a book they are waiting for becomes available.

This directly relates to a Library Management System project,
demonstrating how design patterns integrate into real-world applications.
"""

from __future__ import annotations
from typing import List


# --- Observer Pattern Base ---


class Observer:
    def update(self, subject: Book) -> None:
        raise NotImplementedError


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


# --- Library Domain ---


class Book(Subject):
    """A book in the library catalog that notifies waiting users when returned."""

    def __init__(self, title: str, author: str) -> None:
        super().__init__()
        self.title = title
        self.author = author
        self._available = True

    @property
    def available(self) -> bool:
        return self._available

    def borrow(self, borrower_name: str) -> str:
        if not self._available:
            return f"'{self.title}' is currently unavailable"
        self._available = False
        return f"'{self.title}' borrowed by {borrower_name}"

    def return_book(self) -> str:
        self._available = True
        self.notify()  # Notify all waiting users
        return f"'{self.title}' has been returned and is now available"


class WaitingUser(Observer):
    """A library member waiting for a specific book to become available."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.notifications: List[str] = []

    def update(self, subject: Book) -> None:
        message = f"Dear {self.name}, '{subject.title}' by {subject.author} is now available!"
        self.notifications.append(message)
        print(message)


class EmailNotifier(Observer):
    """Sends email notifications when a book becomes available."""

    def update(self, subject: Book) -> None:
        print(f"[EMAIL] Sending availability alert for '{subject.title}' to all subscribers")


class SMSNotifier(Observer):
    """Sends SMS notifications when a book becomes available."""

    def update(self, subject: Book) -> None:
        print(f"[SMS] '{subject.title}' is back in the library")


def main():
    """
    >>> book = Book("Design Patterns", "Gang of Four")

    # Users register interest in the book
    >>> ahmed = WaitingUser("Ahmed")
    >>> sara = WaitingUser("Sara")
    >>> email = EmailNotifier()

    >>> book.attach(ahmed)
    >>> book.attach(sara)
    >>> book.attach(email)

    # Someone borrows the book
    >>> book.borrow("Omar")
    "'Design Patterns' borrowed by Omar"

    # Try to borrow again while unavailable
    >>> book.borrow("Ali")
    "'Design Patterns' is currently unavailable"

    # Book is returned - all observers are notified automatically
    >>> book.return_book()
    Dear Ahmed, 'Design Patterns' by Gang of Four is now available!
    Dear Sara, 'Design Patterns' by Gang of Four is now available!
    [EMAIL] Sending availability alert for 'Design Patterns' to all subscribers
    "'Design Patterns' has been returned and is now available"

    # Ahmed got notified
    >>> ahmed.notifications
    ["Dear Ahmed, 'Design Patterns' by Gang of Four is now available!"]

    # Detach Ahmed (he already borrowed the book)
    >>> book.detach(ahmed)

    # Return the book again - only Sara and email get notified
    >>> book.borrow("Ahmed")
    "'Design Patterns' borrowed by Ahmed"
    >>> book.return_book()
    Dear Sara, 'Design Patterns' by Gang of Four is now available!
    [EMAIL] Sending availability alert for 'Design Patterns' to all subscribers
    "'Design Patterns' has been returned and is now available"
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()