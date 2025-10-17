"""
http://code.activestate.com/recipes/413838-memento-closure/

*TL;DR
Provides the ability to restore an object to its previous state.
"""

from copy import copy, deepcopy
from typing import Callable, List


def memento(obj: Any, deep: bool = False) -> Callable:
    state = deepcopy(obj.__dict__) if deep else copy(obj.__dict__)

    def restore() -> None:
        obj.__dict__.clear()
        obj.__dict__.update(state)

    return restore


class Transaction:
    """A transaction guard.

    This is, in fact, just syntactic sugar around a memento closure.
    """

    deep = False
    states: List[Callable[[], None]] = []

    def __init__(self, deep: bool, *targets: Any) -> None:
        self.deep = deep
        self.targets = targets
        self.commit()

    def commit(self) -> None:
        self.states = [memento(target, self.deep) for target in self.targets]

    def rollback(self) -> None:
        for a_state in self.states:
            a_state()


def Transactional(method):
    """Adds transactional semantics to methods. Methods decorated  with
    @Transactional will roll back to entry-state upon exceptions.

    :param method: The function to be decorated.
    """

    def __init__(self, method: Callable) -> None:
        self.method = method

    def __get__(self, obj: Any, T: Type) -> Callable:
        """
        A decorator that makes a function transactional.

        :param method: The function to be decorated.
        """

        def transaction(*args, **kwargs):
            state = memento(obj)
            try:
                return self.method(obj, *args, **kwargs)
            except Exception as e:
                state()
                raise e

    return transaction


class NumObj:
    def __init__(self, value: int) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: {self.value!r}>"

    def increment(self) -> None:
        self.value += 1

    @Transactional
    def do_stuff(self) -> None:
        self.value = "1111"  # <- invalid value
        self.increment()  # <- will fail and rollback


def main():
    """
    >>> num_obj = NumObj(-1)
    >>> print(num_obj)
    <NumObj: -1>

    >>> a_transaction = Transaction(True, num_obj)

    >>> try:
    ...    for i in range(3):
    ...        num_obj.increment()
    ...        print(num_obj)
    ...    a_transaction.commit()
    ...    print('-- committed')
    ...    for i in range(3):
    ...        num_obj.increment()
    ...        print(num_obj)
    ...    num_obj.value += 'x'  # will fail
    ...    print(num_obj)
    ... except Exception:
    ...    a_transaction.rollback()
    ...    print('-- rolled back')
    <NumObj: 0>
    <NumObj: 1>
    <NumObj: 2>
    -- committed
    <NumObj: 3>
    <NumObj: 4>
    <NumObj: 5>
    -- rolled back

    >>> print(num_obj)
    <NumObj: 2>

    >>> print('-- now doing stuff ...')
    -- now doing stuff ...

    >>> try:
    ...    num_obj.do_stuff()
    ... except Exception:
    ...    print('-> doing stuff failed!')
    ...    import sys
    ...    import traceback
    ...    traceback.print_exc(file=sys.stdout)
    -> doing stuff failed!
    Traceback (most recent call last):
    ...
    TypeError: ...str...int...

    >>> print(num_obj)
    <NumObj: 2>
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.ELLIPSIS)
