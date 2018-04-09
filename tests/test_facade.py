#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import sys
try:
    from io import StringIO
except:
    from StringIO import StringIO
from structural.facade import TestRunner, TC1, TC2, TC3


class TestRunnerFacilities(unittest.TestCase):

    def setUp(self):
        self.tc1 = TC1()
        self.tc2 = TC2()
        self.tc3 = TC3()
        self.average_result_tc1 = "###### In Test 1 ######\n" + \
                                  "Setting up\n" + \
                                  "Running test\n" + \
                                  "Tearing down\n" + \
                                  "Test Finished"
        self.average_result_tc2 = "###### In Test 2 ######\n" + \
                                  "Setting up\n" + \
                                  "Running test\n" + \
                                  "Tearing down\n" + \
                                  "Test Finished"
        self.average_result_tc3 = "###### In Test 3 ######\n" + \
                                  "Setting up\n" + \
                                  "Running test\n" + \
                                  "Tearing down\n" + \
                                  "Test Finished"
        self.runner = TestRunner()
        self.out = StringIO()
        self.saved_stdout = sys.stdout
        sys.stdout = self.out

    def tearDown(self):
        self.out.close()
        sys.stdout = self.saved_stdout

    def test_tc1_output(self):
        self.tc1.run()
        output = self.out.getvalue().strip()
        self.assertEqual(output, self.average_result_tc1)

    def test_tc2_output(self):
        self.tc2.run()
        output = self.out.getvalue().strip()
        self.assertEqual(output, self.average_result_tc2)

    def test_tc3_output(self):
        self.tc3.run()
        output = self.out.getvalue().strip()
        self.assertEqual(output, self.average_result_tc3)

    def test_bunch_launch(self):
        self.runner.runAll()
        output = self.out.getvalue().strip()
        self.assertEqual(output, str(self.average_result_tc1 + '\n\n' +
                         self.average_result_tc2 + '\n\n' +
                         self.average_result_tc3))
