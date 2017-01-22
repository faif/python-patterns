#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Reference: https://en.wikipedia.org/wiki/Delegation_pattern
Author: https://github.com/IuryAlves
"""


class Delegator(object):
    """
    >>> delegator = Delegator(Delegate())
    >>> delegator.do_something("nothing")
    'Doing nothing'
    >>> delegator.do_anything()

    """

    def __init__(self, delegate):
        self.delegate = delegate

    def __getattr__(self, name):
        def wrapper(*args, **kwargs):
            if hasattr(self.delegate, name):
                attr = getattr(self.delegate, name)
                if callable(attr):
                    return attr(*args, **kwargs)
        return wrapper


class Delegate(object):

    def do_something(self, something):
        return "Doing %s" % something


if __name__ == '__main__':
    import doctest
    doctest.testmod()
