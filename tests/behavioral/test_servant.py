from patterns.behavioral.servant import GeometryTools, Circle, Rectangle, Position
import pytest
import math

def test_calculate_area():
    circle = Circle(3, Position(0, 0))
    assert GeometryTools.calculate_area(circle) == math.pi * 3 ** 2

    rectangle = Rectangle(4, 5, Position(0, 0))
    assert GeometryTools.calculate_area(rectangle) == 4 * 5

    with pytest.raises(ValueError):
        GeometryTools.calculate_area("invalid shape")

def test_calculate_perimeter():
    circle = Circle(3, Position(0, 0))
    assert GeometryTools.calculate_perimeter(circle) == 2 * math.pi * 3

    rectangle = Rectangle(4, 5, Position(0, 0))
    assert GeometryTools.calculate_perimeter(rectangle) == 2 * (4 + 5)

    with pytest.raises(ValueError):
        GeometryTools.calculate_perimeter("invalid shape")


def test_move_to():
    circle = Circle(3, Position(0, 0))
    new_position = Position(1, 1)
    GeometryTools.move_to(circle, new_position)
    assert circle.position == new_position

    rectangle = Rectangle(4, 5, Position(0, 0))
    new_position = Position(1, 1)
    GeometryTools.move_to(rectangle, new_position)
    assert rectangle.position == new_position
