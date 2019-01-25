#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Reference: https://en.wikipedia.org/wiki/Delegation_pattern
Author: https://github.com/IuryAlves

*TL;DR80
Allows object composition to achieve the same code reuse as inheritance.
"""


class Delegator(object):
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

    def __init__(self, delegate):
        self.delegate = delegate

    def __getattr__(self, name):
        attr = getattr(self.delegate, name)

        if not callable(attr):
            return attr

        def wrapper(*args, **kwargs):
            return attr(*args, **kwargs)
        return wrapper


class Delegate(object):
    def __init__(self):
        self.p1 = 123

    def do_something(self, something):
        return "Doing %s" % something


if __name__ == '__main__':
    import doctest

    doctest.testmod()
