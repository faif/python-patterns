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
        expected_output = os.linesep.join(
            ['<Price: 100, price after discount: 100>', '<Price: 100, price after discount: 90.0>', '<Price: 1000, price after discount: 730.0>', '']
        )
        # byte representation required due to EOF returned subprocess
        expected_output_as_bytes = expected_output.encode(encoding='UTF-8')
        self.assertEqual(output, expected_output_as_bytes)
