#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*TL;DR
Encapsulates all information needed to perform an action or trigger an event.

*Examples in Python ecosystem:
Django HttpRequest (without `execute` method):
 https://docs.djangoproject.com/en/2.1/ref/request-response/#httprequest-objects
"""

from __future__ import print_function
import os


class MoveFileCommand(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def execute(self):
        self.rename(self.src, self.dest)

    def undo(self):
        self.rename(self.dest, self.src)

    def rename(self, src, dest):
        print(u"renaming %s to %s" % (src, dest))
        os.rename(src, dest)


def main():
    """
    >>> from os.path import lexists

    >>> command_stack = [
    ...     MoveFileCommand('foo.txt', 'bar.txt'),
    ...     MoveFileCommand('bar.txt', 'baz.txt')
    ... ]

    # Verify that none of the target files exist
    >>> assert not lexists("foo.txt")
    >>> assert not lexists("bar.txt")
    >>> assert not lexists("baz.txt")

    # Create empty file
    >>> open("foo.txt", "w").close()

    # Commands can be executed later on
    >>> for cmd in command_stack:
    ...     cmd.execute()
    renaming foo.txt to bar.txt
    renaming bar.txt to baz.txt

    # And can also be undone at will
    >>> for cmd in reversed(command_stack):
    ...     cmd.undo()
    renaming baz.txt to bar.txt
    renaming bar.txt to foo.txt

    >>> os.unlink("foo.txt")
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod()
