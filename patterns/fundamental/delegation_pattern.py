"""
Reference: https://en.wikipedia.org/wiki/Delegation_pattern
Author: https://github.com/IuryAlves

*TL;DR
Allows object composition to achieve the same code reuse as inheritance.
"""

from __future__ import annotations

from typing import Any, Callable, Union


class Delegator:
    """
    >>> delegator = Delegator(Delegate())
    >>> delegator.p1
    123
    >>> delegator.p2
    Traceback (most recent call last):
    ...
    AttributeError: 'Delegate' object has no attribute 'p2'
    >>> delegator.do_something("nothing")
    'Doing nothing'
    >>> delegator.do_anything()
    Traceback (most recent call last):
    ...
    AttributeError: 'Delegate' object has no attribute 'do_anything'
    """

    def __init__(self, delegate: Delegate):
        self.delegate = delegate

    def __getattr__(self, name: str) -> Union[Any, Callable]:
        attr = getattr(self.delegate, name)

        if not callable(attr):
            return attr

        def wrapper(*args, **kwargs):
            return attr(*args, **kwargs)

        return wrapper


class Delegate:
    def __init__(self):
        self.p1 = 123

    def do_something(self, something: str) -> str:
        return f"Doing {something}"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
