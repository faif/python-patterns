from __future__ import annotations


class Person:
    def __init__(self, name: str, action: Action) -> None:
        self.name = name
        self.action = action

    def do_action(self) -> Action:
        print(self.name, self.action.name, end=" ")
        return self.action


class Action:
    def __init__(self, name: str) -> None:
        self.name = name

    def amount(self, val: str) -> Action:
        print(val, end=" ")
        return self

    def stop(self) -> None:
        print("then stop")


def main():
    """
    >>> move = Action('move')
    >>> person = Person('Jack', move)
    >>> person.do_action().amount('5m').stop()
    Jack move 5m then stop
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
