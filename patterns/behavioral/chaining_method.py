class Person:
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def do_action(self):
        print(self.name, self.action.name, end=' ')
        return self.action


class Action:
    def __init__(self, name):
        self.name = name

    def amount(self, val):
        print(val, end=' ')
        return self

    def stop(self):
        print('then stop')


def main():
    """
    >>> move = Action('move')
    >>> person = Person('Jack', move)
    >>> person.do_action().amount('5m').stop()
    Jack move 5m then stop
    """


if __name__ == '__main__':
    import doctest
    doctest.testmod()
