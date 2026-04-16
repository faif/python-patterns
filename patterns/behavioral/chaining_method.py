from __future__ import annotations

from typing import Self


class Person:
    def __init__(self, name: str) -> None:
        self.name = name
        self.age: int = 0

    def set_name(self, name: str) -> Self:
        self.name = name
        return self

    def set_age(self, age: int) -> Self:
        self.age = age
        return self

    def __str__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}"


if __name__ == "__main__":
    person = Person("Jorge").set_age(28).set_name("Jorge Otero")
    print(person)
