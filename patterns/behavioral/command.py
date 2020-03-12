"""
Command pattern decouples the object invoking a job from the one who knows
how to do it. As mentioned in the GoF book, a good example is in menu items.
You have a menu that has lots of items. Each item is responsible for doing a
special thing and you want your menu item just call the `execute` method when
it is pressed. To achieve this you implement a command object with the `execute`
method for each menu item and pass to it.

*TL;DR
Object oriented implementation of callback functions.

*Examples in Python ecosystem:
Django HttpRequest (without `execute` method):
https://docs.djangoproject.com/en/2.1/ref/request-response/#httprequest-objects
"""


class Command:
    """
    The interface that commands implement. This is used to abstract invoker from
    the command is going to handle the job.
    """

    def execute(self):
        raise NotImplementedError()


class MakeBoldCommand(Command):
    """
    A simple command to bold a text.
    """

    def execute(self):
        print('I am making it bold.')


class MakeItalicCommand(Command):
    """
    A simple command to italic a text.
    """

    def execute(self):
        print('I am making it italic.')


class MenuItem:
    """
    The invoker class. Here it is items in a menu.
    """

    def __init__(self, command):
        self._command = command

    def on_press(self):
        self._command.execute()


def main():
    """
    >>> item1 = MenuItem(MakeBoldCommand())

    >>> item2 = MenuItem(MakeItalicCommand())

    >>> item1.on_press()
    I am making it bold.

    >>> item2.on_press()
    I am making it italic.
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod()
