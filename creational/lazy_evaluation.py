#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Lazily-evaluated property pattern in Python.

https://en.wikipedia.org/wiki/Lazy_evaluation

*References:
bottle
https://github.com/bottlepy/bottle/blob/cafc15419cbb4a6cb748e6ecdccf92893bb25ce5/bottle.py#L270
django
https://github.com/django/django/blob/ffd18732f3ee9e6f0374aff9ccf350d85187fac2/django/utils/functional.py#L19
pip
https://github.com/pypa/pip/blob/cb75cca785629e15efb46c35903827b3eae13481/pip/utils/__init__.py#L821
pyramimd
https://github.com/Pylons/pyramid/blob/7909e9503cdfc6f6e84d2c7ace1d3c03ca1d8b73/pyramid/decorator.py#L4
werkzeug
https://github.com/pallets/werkzeug/blob/5a2bf35441006d832ab1ed5a31963cbc366c99ac/werkzeug/utils.py#L35

*TL;DR80
Delays the eval of an expr until its value is needed and avoids repeated evals.
"""

from __future__ import print_function
import functools


class lazy_property(object):
    def __init__(self, function):
        self.function = function
        functools.update_wrapper(self, function)

    def __get__(self, obj, type_):
        if obj is None:
            return self
        val = self.function(obj)
        obj.__dict__[self.function.__name__] = val
        return val


def lazy_property2(fn):
    attr = '_lazy__' + fn.__name__

    @property
    def _lazy_property(self):
        if not hasattr(self, attr):
            setattr(self, attr, fn(self))
        return getattr(self, attr)

    return _lazy_property


class Person(object):
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
        self.call_count2 = 0

    @lazy_property
    def relatives(self):
        # Get all relatives, let's assume that it costs much time.
        relatives = "Many relatives."
        return relatives

    @lazy_property2
    def parents(self):
        self.call_count2 += 1
        return "Father and mother"


def main():
    Jhon = Person('Jhon', 'Coder')
    print(u"Name: {0}    Occupation: {1}".format(Jhon.name, Jhon.occupation))
    print(u"Before we access `relatives`:")
    print(Jhon.__dict__)
    print(u"Jhon's relatives: {0}".format(Jhon.relatives))
    print(u"After we've accessed `relatives`:")
    print(Jhon.__dict__)
    print(Jhon.parents)
    print(Jhon.__dict__)
    print(Jhon.parents)
    print(Jhon.call_count2)


if __name__ == '__main__':
    main()

### OUTPUT ###
# Name: Jhon    Occupation: Coder
# Before we access `relatives`:
# {'call_count2': 0, 'name': 'Jhon', 'occupation': 'Coder'}
# Jhon's relatives: Many relatives.
# After we've accessed `relatives`:
# {'relatives': 'Many relatives.', 'call_count2': 0, 'name': 'Jhon', 'occupation': 'Coder'}
# Father and mother
# {'_lazy__parents': 'Father and mother', 'relatives': 'Many relatives.', 'call_count2': 1, 'name': 'Jhon', 'occupation': 'Coder'}  # noqa flake8
# Father and mother
# 1
