#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*TL;DR80
Encapsulates all information needed to perform an action or trigger an event.

*Examples in Python ecosystem:
Django HttpRequest (without `execute` method):
 https://docs.djangoproject.com/en/2.1/ref/request-response/#httprequest-objects
"""

from __future__ import print_function
import os
from os.path import lexists


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
    command_stack = []

    # commands are just pushed into the command stack
    command_stack.append(MoveFileCommand('foo.txt', 'bar.txt'))
    command_stack.append(MoveFileCommand('bar.txt', 'baz.txt'))

    # verify that none of the target files exist
    assert not lexists("foo.txt")
    assert not lexists("bar.txt")
    assert not lexists("baz.txt")
    try:
        with open("foo.txt", "w"):  # Creating the file
            pass

        # they can be executed later on
        for cmd in command_stack:
            cmd.execute()

        # and can also be undone at will
        for cmd in reversed(command_stack):
            cmd.undo()
    finally:
        os.unlink("foo.txt")


if __name__ == "__main__":
    main()


OUTPUT = """
renaming foo.txt to bar.txt
renaming bar.txt to baz.txt
renaming baz.txt to bar.txt
renaming bar.txt to foo.txt
"""
