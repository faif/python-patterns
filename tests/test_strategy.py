"""
Tests for strategy.py
"""
import subprocess

from .compat import unittest


class StrategyTest(unittest.TestCase):

    def test_print_output(self):
        """
        Verifies the print output when strategy.py is executed.
        The expected_output is equivalent to the output on the command
        line when running 'python strategy.py'.
        """
        output = subprocess.check_output(["python", "patterns/strategy.py"])
        expected_output = 'Strategy Example 0\r\n\
Strategy Example 1 from execute 1\r\n\
Strategy Example 2 from execute 2\r\n'
        # byte representation required due to EOF returned subprocess
        expected_output_as_bytes = expected_output.encode(encoding='UTF-8')
        self.assertEqual(
            output.splitlines(), expected_output_as_bytes.splitlines()
        )
