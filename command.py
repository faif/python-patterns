import os


class MoveFileCommand(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def execute(self):
        self()
        
    def __call__(self):
        print('renaming {} to {}'.format(self.src, self.dest))
        os.rename(self.src, self.dest)

    def undo(self):
        print('renaming {} to {}'.format(self.dest, self.src))
        os.rename(self.dest, self.src)


if __name__ == "__main__":
    undo_stack = []
    ren1 = MoveFileCommand('foo.txt', 'bar.txt')
    ren2 = MoveFileCommand('bar.txt', 'baz.txt')

    # commands are just pushed into the command stack
    for cmd in ren1, ren2:
        undo_stack.append(cmd)

    # they can be executed later on will
    for cmd in undo_stack:
        cmd.execute()     # foo.txt is now renamed to baz.txt

    # and can also be undone on will
    for cmd in undo_stack:
        undo_stack.pop().undo()  # Now it's bar.txt
        undo_stack.pop().undo()  # and back to foo.txt
