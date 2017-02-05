#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""http://code.activestate.com/recipes/413838-memento-closure/"""

from copy import copy
from copy import deepcopy


def memento(obj, deep=False):
    state = deepcopy(obj.__dict__) if deep else copy(obj.__dict__)

    def restore():
        obj.__dict__.clear()
        obj.__dict__.update(state)

    return restore


class Transaction(object):
    """A transaction guard.

    This is, in fact, just syntactic sugar around a memento closure.
    """
    deep = False
    states = []

    def __init__(self, deep, *targets):
        self.deep = deep
        self.targets = targets
        self.commit()

    def commit(self):
        self.states = [memento(target, self.deep) for target in self.targets]

    def rollback(self):
        for a_state in self.states:
            a_state()


class Transactional(object):
    """Adds transactional semantics to methods. Methods decorated  with

    @Transactional will rollback to entry-state upon exceptions.
    """

    def __init__(self, method):
        self.method = method

    def __get__(self, obj, T):
        def transaction(*args, **kwargs):
            state = memento(obj)
            try:
                return self.method(obj, *args, **kwargs)
            except Exception as e:
                state()
                raise e

        return transaction


class NumObj(object):

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return '<%s: %r>' % (self.__class__.__name__, self.value)

    def increment(self):
        self.value += 1

    @Transactional
    def do_stuff(self):
        self.value = '1111'  # <- invalid value
        self.increment()  # <- will fail and rollback


if __name__ == '__main__':
    num_obj = NumObj(-1)
    print(num_obj)

    a_transaction = Transaction(True, num_obj)
    try:
        for i in range(3):
            num_obj.increment()
            print(num_obj)
        a_transaction.commit()
        print('-- committed')

        for i in range(3):
            num_obj.increment()
            print(num_obj)
        num_obj.value += 'x'  # will fail
        print(num_obj)
    except Exception as e:
        a_transaction.rollback()
        print('-- rolled back')
    print(num_obj)

    print('-- now doing stuff ...')
    try:
        num_obj.do_stuff()
    except Exception as e:
        print('-> doing stuff failed!')
        import sys
        import traceback

        traceback.print_exc(file=sys.stdout)
    print(num_obj)


### OUTPUT ###
# <NumObj: -1>
# <NumObj: 0>
# <NumObj: 1>
# <NumObj: 2>
# -- committed
# <NumObj: 3>
# <NumObj: 4>
# <NumObj: 5>
# -- rolled back
# <NumObj: 2>
# -- now doing stuff ...
# -> doing stuff failed!
# Traceback (most recent call last):
# File "memento.py", line 97, in <module>
#     num_obj.do_stuff()
#   File "memento.py", line 52, in transaction
#     raise e
#   File "memento.py", line 49, in transaction
#     return self.method(obj, *args, **kwargs)
#   File "memento.py", line 70, in do_stuff
#     self.increment()     # <- will fail and rollback
#   File "memento.py", line 65, in increment
#     self.value += 1
# TypeError: Can't convert 'int' object to str implicitly
# <NumObj: 2>
