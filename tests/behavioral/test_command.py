#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil
import unittest
from patterns.behavioral.command import MoveFileCommand


class CommandTest(unittest.TestCase):
    @classmethod
    def __get_test_directory(self):
        """
        Get the temporary directory for the tests.
        """
        self.test_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_command')

    @classmethod
    def setUpClass(self):
        """
        - Create a temporary directory and file
        /test_command
           /foo.txt
        - get the temporary test directory
        - and initializes the command stack.
        """
        os.mkdir('tests/behavioral/test_command')
        open('tests/behavioral/test_command/foo.txt', 'w').close()
        self.__get_test_directory()
        self.command_stack = []
        self.command_stack.append(
            MoveFileCommand(os.path.join(self.test_dir, 'foo.txt'), os.path.join(self.test_dir, 'bar.txt'))
        )
        self.command_stack.append(
            MoveFileCommand(os.path.join(self.test_dir, 'bar.txt'), os.path.join(self.test_dir, 'baz.txt'))
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
    def tearDownClass(self):
        """
        Remove the temporary directory /test_command and its content.
        """
        shutil.rmtree('tests/behavioral/test_command')
