#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from structural.facade import TestRunner


class TestRunnerFacilities(unittest.TestCase):

    def setUp(self):
        self.runner = TestRunner()
        self.average_result = """###### In Test 1 ######
Setting up
Running test
Tearing down
Test Finished

###### In Test 2 ######
Setting up
Running test
Tearing down
Test Finished

###### In Test 3 ######
Setting up
Running test
Tearing down
Test Finished"""

    def test_bunch_launch(self):
        import sys
        try:
            from io import StringIO
        except:
            from StringIO import StringIO
        out = StringIO()
        sys.stdout = out
        self.runner.runAll()
        output = out.getvalue().strip()
        self.assertEqual(output, self.average_result)


