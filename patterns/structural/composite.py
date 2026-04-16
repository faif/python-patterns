from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    @abstractmethod
    def execute(self) -> None: ...


class Leaf(Component):
    def execute(self) -> None:
        print("Leaf executed")


class Composite(Component):
    def __init__(self) -> None:
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)

    def execute(self) -> None:
        print("Composite executing children:")
        for child in self._children:
            child.execute()


if __name__ == "__main__":
    root = Composite()
    root.add(Leaf())
    sub = Composite()
    sub.add(Leaf())
    root.add(sub)
    root.execute()
