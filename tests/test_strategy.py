#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess
import unittest


class StrategyTest(unittest.TestCase):

    def test_print_output(self):
        """
        Verifies the print output when strategy.py is executed.
        The expected_output is equivalent to the output on the command
        line when running 'python strategy.py'.
        """
        output = subprocess.check_output(["python", "behavioral/strategy.py"])
        expected_output = os.linesep.join([
            'Strategy Example 0',
            'Strategy Example 1 from execute 1',
            'Strategy Example 2 from execute 2',
            ''
        ])
        # byte representation required due to EOF returned subprocess
        expected_output_as_bytes = expected_output.encode(encoding='UTF-8')
        self.assertEqual(output, expected_output_as_bytes)
