"""
Implementation of the Servant design pattern.

The Servant design pattern is a behavioral pattern used to offer functionality
to a group of classes without requiring them to inherit from a base class.

This pattern involves creating a Servant class that provides certain services
or functionalities. These services are used by other classes which do not need
to be related through a common parent class. It is particularly useful in
scenarios where adding the desired functionality through inheritance is impractical
or would lead to a rigid class hierarchy.

This pattern is characterized by the following:

- A Servant class that provides specific services or actions.
- Client classes that need these services, but do not derive from the Servant class.
- The use of the Servant class by the client classes to perform actions on their behalf.

References:
- https://en.wikipedia.org/wiki/Servant_(design_pattern)
"""

import math


class Position:
    """Representation of a 2D position with x and y coordinates."""

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    """Representation of a circle defined by a radius and a position."""

    def __init__(self, radius, position: Position):
        self.radius = radius
        self.position = position


class Rectangle:
    """Representation of a rectangle defined by width, height, and a position."""

    def __init__(self, width, height, position: Position):
        self.width = width
        self.height = height
        self.position = position


class GeometryTools:
    """
    Servant class providing geometry-related services, including area and
    perimeter calculations and position updates.
    """

    @staticmethod
    def calculate_area(shape):
        """
        Calculate the area of a given shape.

        Args:
            shape: The geometric shape whose area is to be calculated.

        Returns:
            The area of the shape.

        Raises:
            ValueError: If the shape type is unsupported.
        """
        if isinstance(shape, Circle):
            return math.pi * shape.radius**2
        elif isinstance(shape, Rectangle):
            return shape.width * shape.height
        else:
            raise ValueError("Unsupported shape type")

    @staticmethod
    def calculate_perimeter(shape):
        """
        Calculate the perimeter of a given shape.

        Args:
            shape: The geometric shape whose perimeter is to be calculated.

        Returns:
            The perimeter of the shape.

        Raises:
            ValueError: If the shape type is unsupported.
        """
        if isinstance(shape, Circle):
            return 2 * math.pi * shape.radius
        elif isinstance(shape, Rectangle):
            return 2 * (shape.width + shape.height)
        else:
            raise ValueError("Unsupported shape type")

    @staticmethod
    def move_to(shape, new_position: Position):
        """
        Move a given shape to a new position.

        Args:
            shape: The geometric shape to be moved.
            new_position: The new position to move the shape to.
        """
        shape.position = new_position
        print(f"Moved to ({shape.position.x}, {shape.position.y})")


def main():
    """
    >>> servant = GeometryTools()
    >>> circle = Circle(5, Position(0, 0))
    >>> rectangle = Rectangle(3, 4, Position(0, 0))
    >>> servant.calculate_area(circle)
    78.53981633974483
    >>> servant.calculate_perimeter(rectangle)
    14
    >>> servant.move_to(circle, Position(3, 4))
    Moved to (3, 4)
    >>> servant.move_to(rectangle, Position(5, 6))
    Moved to (5, 6)
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
