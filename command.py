#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
        print('renaming {} to {}'.format(src, dest))
        os.rename(src, dest)


def main():
    command_stack = []

    # commands are just pushed into the command stack
    command_stack.append(MoveFileCommand('foo.txt', 'bar.txt'))
    command_stack.append(MoveFileCommand('bar.txt', 'baz.txt'))

    # they can be executed later on
    for cmd in command_stack:
        cmd.execute()

    # and can also be undone at will
    for cmd in reversed(command_stack):
        cmd.undo()

if __name__ == "__main__":
    main()

### OUTPUT ###
# renaming foo.txt to bar.txt
# renaming bar.txt to baz.txt
# renaming baz.txt to bar.txt
# renaming bar.txt to foo.txt
