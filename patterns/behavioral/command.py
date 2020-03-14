"""
Command pattern decouples the object invoking a job from the one who knows
how to do it. As mentioned in the GoF book, a good example is in menu items.
You have a menu that has lots of items. Each item is responsible for doing a
special thing and you want your menu item just call the `execute` method when
it is pressed. To achieve this you implement a command object with the `execute`
method for each menu item and pass to it.

*About the example
We have a menu containing two items. Each item accept a file name, one hides the file
and the other deletes it. Both items have undo option.
Each item is a MenuItem class that accept corresponding command as input and executes
its `execute` method when it is pressed.

*TL;DR
Object oriented implementation of callback functions.

*Examples in Python ecosystem:
Django HttpRequest (without `execute` method):
https://docs.djangoproject.com/en/2.1/ref/request-response/#httprequest-objects
"""

import os


class HideFileCommand:
    """
    A command to hide a file given its name
    """

    def __init__(self):
        # an array of files hidden, to undo them as needed
        self._hidden_files = []

    def execute(self, filename):
        if os.path.isfile(filename):
            print(f'hiding {filename}')

            os.rename(filename, f'.{filename}')
            self._hidden_files.append(filename)
        else:
            print(f'{filename} dose not exists to hide')

    def undo(self):
        if len(self._hidden_files) > 0:
            filename = self._hidden_files.pop()

            print(f'un-hiding {filename}')

            os.rename(f'.{filename}', filename)


class DeleteFileCommand:
    """
    A command to delete a file given its name
    """

    def __init__(self):
        # an array of deleted files, to undo them as needed
        self._deleted_files = []

        # create a directory to store deleted files
        if not os.path.exists('bin'):
            os.makedirs('bin')

    def execute(self, filename):
        if os.path.isfile(filename):
            print(f'deleting {filename}')

            os.rename(filename, f'bin/{filename}')
            self._deleted_files.append(filename)
        else:
            print(f'{filename} dose not exists to delete')

    def undo(self):
        if len(self._deleted_files) > 0:
            filename = self._deleted_files.pop()

            print(f'un-deleting {filename}')

            os.rename(f'bin/{filename}', filename)


class MenuItem:
    """
    The invoker class. Here it is items in a menu.
    """

    def __init__(self, command):
        self._command = command

    def on_do_press(self, filename):
        self._command.execute(filename)

    def on_undo_press(self):
        self._command.undo()


def main():
    """
    >>> item1 = MenuItem(DeleteFileCommand())

    >>> item2 = MenuItem(HideFileCommand())

    # create a file named `test-file` to work with
    >>> test_file_name = 'test-file'
    >>> open(test_file_name, 'w').close()

    # deleting `test-file`
    >>> item1.on_do_press(test_file_name)
    deleting test-file

    # hiding `test-file` but it dose not exists
    >>> item2.on_do_press(test_file_name)
    test-file dose not exists to hide

    # un-deleting `test-file`
    >>> item1.on_undo_press()
    un-deleting test-file

    # hiding `test-file`
    >>> item2.on_do_press(test_file_name)
    hiding test-file
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
