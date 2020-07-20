"""
Command pattern decouples the object invoking a job from the one who knows
how to do it. As mentioned in the GoF book, a good example is in menu items.
You have a menu that has lots of items. Each item is responsible for doing a
special thing and you want your menu item just call the execute method when
it is pressed. To achieve this you implement a command object with the execute
method for each menu item and pass to it.

*About the example
We have a menu containing two items. Each item accepts a file name, one hides the file
and the other deletes it. Both items have an undo option.
Each item is a MenuItem class that accepts the corresponding command as input and executes
it's execute method when it is pressed.

*TL;DR
Object oriented implementation of callback functions.

*Examples in Python ecosystem:
Django HttpRequest (without execute method):
https://docs.djangoproject.com/en/2.1/ref/request-response/#httprequest-objects
"""

from typing import Union


class HideFileCommand:
    """
    A command to hide a file given its name
    """

    def __init__(self) -> None:
        # an array of files hidden, to undo them as needed
        self._hidden_files = []

    def execute(self, filename: str) -> None:
        print(f"hiding {filename}")
        self._hidden_files.append(filename)

    def undo(self) -> None:
        filename = self._hidden_files.pop()
        print(f"un-hiding {filename}")


class DeleteFileCommand:
    """
    A command to delete a file given its name
    """

    def __init__(self) -> None:
        # an array of deleted files, to undo them as needed
        self._deleted_files = []

    def execute(self, filename: str) -> None:
        print(f"deleting {filename}")
        self._deleted_files.append(filename)

    def undo(self) -> None:
        filename = self._deleted_files.pop()
        print(f"restoring {filename}")


class MenuItem:
    """
    The invoker class. Here it is items in a menu.
    """

    def __init__(self, command: Union[HideFileCommand, DeleteFileCommand]) -> None:
        self._command = command

    def on_do_press(self, filename: str) -> None:
        self._command.execute(filename)

    def on_undo_press(self) -> None:
        self._command.undo()


def main():
    """
    >>> item1 = MenuItem(DeleteFileCommand())

    >>> item2 = MenuItem(HideFileCommand())

    # create a file named `test-file` to work with
    >>> test_file_name = 'test-file'

    # deleting `test-file`
    >>> item1.on_do_press(test_file_name)
    deleting test-file

    # restoring `test-file`
    >>> item1.on_undo_press()
    restoring test-file

    # hiding `test-file`
    >>> item2.on_do_press(test_file_name)
    hiding test-file

    # un-hiding `test-file`
    >>> item2.on_undo_press()
    un-hiding test-file
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
