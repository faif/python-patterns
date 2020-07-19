"""
*What is this pattern about?
The composite pattern describes a group of objects that is treated the
same way as a single instance of the same type of object. The intent of
a composite is to "compose" objects into tree structures to represent
part-whole hierarchies. Implementing the composite pattern lets clients
treat individual objects and compositions uniformly.

*What does this example do?
The example implements a graphic class，which can be either an ellipse
or a composition of several graphics. Every graphic can be printed.

*Where is the pattern used practically?
In graphics editors a shape can be basic or complex. An example of a
simple shape is a line, where a complex shape is a rectangle which is
made of four line objects. Since shapes have many operations in common
such as rendering the shape to screen, and since shapes follow a
part-whole hierarchy, composite pattern can be used to enable the
program to deal with all shapes uniformly.

*References:
https://en.wikipedia.org/wiki/Composite_pattern
https://infinitescript.com/2014/10/the-23-gang-of-three-design-patterns/

*TL;DR
Describes a group of objects that is treated as a single instance.
"""

from abc import ABC, abstractmethod
from typing import List


class Graphic(ABC):
    @abstractmethod
    def render(self) -> None:
        raise NotImplementedError("You should implement this!")


class CompositeGraphic(Graphic):
    def __init__(self) -> None:
        self.graphics: List[Graphic] = []

    def render(self) -> None:
        for graphic in self.graphics:
            graphic.render()

    def add(self, graphic: Graphic) -> None:
        self.graphics.append(graphic)

    def remove(self, graphic: Graphic) -> None:
        self.graphics.remove(graphic)


class Ellipse(Graphic):
    def __init__(self, name: str) -> None:
        self.name = name

    def render(self) -> None:
        print(f"Ellipse: {self.name}")


def main():
    """
    >>> ellipse1 = Ellipse("1")
    >>> ellipse2 = Ellipse("2")
    >>> ellipse3 = Ellipse("3")
    >>> ellipse4 = Ellipse("4")

    >>> graphic1 = CompositeGraphic()
    >>> graphic2 = CompositeGraphic()

    >>> graphic1.add(ellipse1)
    >>> graphic1.add(ellipse2)
    >>> graphic1.add(ellipse3)
    >>> graphic2.add(ellipse4)

    >>> graphic = CompositeGraphic()

    >>> graphic.add(graphic1)
    >>> graphic.add(graphic2)

    >>> graphic.render()
    Ellipse: 1
    Ellipse: 2
    Ellipse: 3
    Ellipse: 4
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
