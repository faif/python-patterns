#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from structural.facade import TestRunner, TC1, TC2, TC3


class TestRunnerFacilities(unittest.TestCase):

    def setUp(self):
        self.tc = TC1()
        self.average_result_tc1 = "###### In Test 1 ######\n" + \
                                  "Setting up\n" + \
                                  "Running test\n" + \
                                  "Tearing down\n" + \
                                  "Test Finished"

    def test_tc1_output(self):
        import sys
        try:
            from io import StringIO
        except:
            from StringIO import StringIO
        out = StringIO()
        sys.stdout = out
        self.tc.run()
        output = out.getvalue().strip()
        self.assertEqual(output, self.average_result_tc1)


# ###### In Test 2 ######
# Setting up
# Running test
# Tearing down
# Test Finished

# ###### In Test 3 ######
# Setting up
# Running test
# Tearing down
# Test Finished"""

    # def test_bunch_launch(self):
    #     import sys
    #     try:
    #         from io import StringIO
    #     except:
    #         from StringIO import StringIO
    #     out = StringIO()
    #     sys.stdout = out
    #     self.runner.runAll()
    #     output = out.getvalue().strip()
    #     self.assertEqual(output, self.average_result)


