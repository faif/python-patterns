#!/usr/bin/env python
# -*- coding: utf-8 -*-

from proxy import Proxy, NoTalkProxy
from io import StringIO
import sys
from time import time

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

class ProxyTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """ Class scope setup. """
        self.p = Proxy()

    def setUp(self):
        """ Function/test case scope setup. """
        self.output = StringIO()
        self.saved_stdout = sys.stdout
        sys.stdout = self.output

    def tearDown(self):
        """ Function/test case scope teardown. """
        self.output.close()
        sys.stdout = self.saved_stdout

    def test_sales_manager_shall_work_through_proxy_with_delay(self):
        self.p.busy = 'No'
        start_time = time()
        self.p.work()
        end_time = time()
        execution_time = end_time - start_time
        print_output = self.output.getvalue()
        expected_print_output = 'Proxy checking for Sales Manager availability\n\
Sales Manager ready to talk\n'
        self.assertEqual(print_output, expected_print_output)
        expected_execution_time = 2
        self.assertEqual(int(execution_time), expected_execution_time)

    def test_sales_manager_shall_respond_through_proxy_with_delay(self):
        self.p.busy = 'Yes'
        start_time = time()
        self.p.work()
        end_time = time()
        execution_time = end_time - start_time
        print_output = self.output.getvalue()
        expected_print_output = 'Proxy checking for Sales Manager availability\n\
Sales Manager is busy\n'
        self.assertEqual(print_output, expected_print_output)
        expected_execution_time = 2
        self.assertEqual(int(execution_time), expected_execution_time)

class NoTalkProxyTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """ Class scope setup. """
        self.ntp = NoTalkProxy()

    def setUp(self):
        """ Function/test case scope setup. """
        self.output = StringIO()
        self.saved_stdout = sys.stdout
        sys.stdout = self.output

    def tearDown(self):
        """ Function/test case scope teardown. """
        self.output.close()
        sys.stdout = self.saved_stdout

    def test_sales_manager_shall_not_work_through_proxy_with_delay(self):
        self.ntp.busy = 'No'
        start_time = time()
        self.ntp.work()
        end_time = time()
        execution_time = end_time - start_time
        print_output = self.output.getvalue()
        expected_print_output = 'Proxy checking for Sales Manager availability\n\
This Sales Manager will not talk to you whether he/she is busy or not\n'
        self.assertEqual(print_output, expected_print_output)
        expected_execution_time = 2
        self.assertEqual(int(execution_time), expected_execution_time)

    def test_sales_manager_shall_not_respond_through_proxy_with_delay(self):
        self.ntp.busy = 'Yes'
        start_time = time()
        self.ntp.work()
        end_time = time()
        execution_time = end_time - start_time
        print_output = self.output.getvalue()
        expected_print_output = 'Proxy checking for Sales Manager availability\n\
This Sales Manager will not talk to you whether he/she is busy or not\n'
        self.assertEqual(print_output, expected_print_output)
        expected_execution_time = 2
        self.assertEqual(int(execution_time), expected_execution_time)

if __name__ == "__main__":
    unittest.main()
