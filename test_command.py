from command import MoveFileCommand
import unittest, os, shutil, subprocess


class StrategyTest(unittest.TestCase):

    def __get_directories(self):
        """
        Get the directories relevant for tests:
        - self.file_dir: the directory of this script
        - self.test_dir: the root directory for tests
        """
        self.file_dir = os.path.dirname(os.path.realpath(__file__))
        self.test_dir = os.path.join(self.file_dir, 'test_command')

    def setUp(self):
        """
        Creates a temporary directory and file:
        ./test_command
           /foo.txt
        """
        os.mkdir('test_command')
        open('test_command/foo.txt', 'w').close()
        self.__get_directories()

    def test_sequential_execution(self):
        self.command_stack = []
        self.command_stack.append(MoveFileCommand(os.path.join(self.test_dir, 'foo.txt'), os.path.join(self.test_dir, 'bar.txt')))
        self.command_stack.append(MoveFileCommand(os.path.join(self.test_dir, 'bar.txt'), os.path.join(self.test_dir, 'baz.txt')))
        self.command_stack[0].execute()
        output_after_first_command = os.listdir(self.test_dir)
        self.assertEqual(output_after_first_command[0], 'bar.txt')
        self.command_stack[1].execute()
        output_after_second_command = os.listdir(self.test_dir)
        self.assertEqual(output_after_second_command[0], 'baz.txt')

    def tearDown(self):
        """
        Removes the temporary directory and its content:
        ./test_command
           ...
        """
        shutil.rmtree('test_command')

if __name__ == "__main__":
    unittest.main()
