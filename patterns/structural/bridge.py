"""
*References:
http://en.wikibooks.org/wiki/Computer_Science_Design_Patterns/Bridge_Pattern#Python

*TL;DR
Decouples an abstraction from its implementation.
"""
from typing import Union


# ConcreteImplementor 1/2
class DrawingAPI1:
    def draw_circle(self, x: int, y: int, radius: float) -> None:
        print(f"API1.circle at {x}:{y} radius {radius}")


# ConcreteImplementor 2/2
class DrawingAPI2:
    def draw_circle(self, x: int, y: int, radius: float) -> None:
        print(f"API2.circle at {x}:{y} radius {radius}")


# Refined Abstraction
class CircleShape:
    def __init__(
        self, x: int, y: int, radius: int, drawing_api: Union[DrawingAPI2, DrawingAPI1]
    ) -> None:
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    # low-level i.e. Implementation specific
    def draw(self) -> None:
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    # high-level i.e. Abstraction specific
    def scale(self, pct: float) -> None:
        self._radius *= pct


def main():
    """
    >>> shapes = (CircleShape(1, 2, 3, DrawingAPI1()), CircleShape(5, 7, 11, DrawingAPI2()))

    >>> for shape in shapes:
    ...    shape.scale(2.5)
    ...    shape.draw()
    API1.circle at 1:2 radius 7.5
    API2.circle at 5:7 radius 27.5
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
