import os
import shutil
import tempfile

from .compat import unittest
from patterns.command import MoveFileCommand


TEST_DIRECTORY = 'test_command'


class CommandTest(unittest.TestCase):

    @classmethod
    def __get_test_directory(cls):
        """
        Get the temporary directory for the tests.
        """
        cls.test_dir = os.path.join(
            tempfile.gettempdir(), 'test_command'
        )
        if not os.path.exists(cls.test_dir):
            os.mkdir(cls.test_dir)

    @classmethod
    def setUpClass(cls):
        """
        - Create a temporary directory and file
        /test_command
           /foo.txt
        - get the temporary test directory
        - and initializes the command stack.
        """
        cls.__get_test_directory()
        open(os.path.join(cls.test_dir, 'foo.txt'), 'w').close()
        cls.command_stack = []
        cls.command_stack.append(
            MoveFileCommand(
                os.path.join(cls.test_dir, 'foo.txt'),
                os.path.join(cls.test_dir, 'bar.txt')
            )
        )
        cls.command_stack.append(
            MoveFileCommand(
                os.path.join(cls.test_dir, 'bar.txt'),
                os.path.join(cls.test_dir, 'baz.txt')
            )
        )

    def test_sequential_execution(self):
        self.command_stack[0].execute()
        output_after_first_execution = os.listdir(self.test_dir)
        self.assertEqual(output_after_first_execution[0], 'bar.txt')
        self.command_stack[1].execute()
        output_after_second_execution = os.listdir(self.test_dir)
        self.assertEqual(output_after_second_execution[0], 'baz.txt')

    def test_sequential_undo(self):
        self.command_stack = list(reversed(self.command_stack))
        self.command_stack[0].undo()
        output_after_first_undo = os.listdir(self.test_dir)
        self.assertEqual(output_after_first_undo[0], 'bar.txt')
        self.command_stack[1].undo()
        output_after_second_undo = os.listdir(self.test_dir)
        self.assertEqual(output_after_second_undo[0], 'foo.txt')

    @classmethod
    def tearDownClass(cls):
        """
        Remove the temporary directory /test_command and its content.
        """
        shutil.rmtree(cls.test_dir)

if __name__ == "__main__":
    unittest.main()
