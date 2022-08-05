"""
http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/
Implementation of the iterator pattern with a generator

*TL;DR
Traverses a container and accesses the container's elements.
"""

from typing import Any, Generator


def count_to(count: int) -> Generator[str, Any, None]:
    """Counts by word numbers, up to a maximum of five"""
    numbers = ["one", "two", "three", "four", "five"]
    yield from numbers[:count]


# Test the generator
def count_to_two() -> Generator[str, Any, None]:
    return count_to(2)


def count_to_five() -> Generator[str, Any, None]:
    return count_to(5)


def main():
    """
    # Counting to two...
    >>> for number in count_to_two():
    ...     print(number)
    one
    two

    # Counting to five...
    >>> for number in count_to_five():
    ...     print(number)
    one
    two
    three
    four
    five
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
