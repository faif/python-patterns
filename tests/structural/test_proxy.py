import sys
from time import time
import unittest
from io import StringIO

from patterns.structural.proxy import Proxy, NoTalkProxy


class ProxyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """ Class scope setup. """
        cls.p = Proxy()

    def setUp(cls):
        """ Function/test case scope setup. """
        cls.output = StringIO()
        cls.saved_stdout = sys.stdout
        sys.stdout = cls.output

    def tearDown(cls):
        """ Function/test case scope teardown. """
        cls.output.close()
        sys.stdout = cls.saved_stdout

    def test_sales_manager_shall_talk_through_proxy_with_delay(cls):
        cls.p.busy = 'No'
        start_time = time()
        cls.p.talk()
        end_time = time()
        execution_time = end_time - start_time
        print_output = cls.output.getvalue()
        expected_print_output = 'Proxy checking for Sales Manager availability\n\
Sales Manager ready to talk\n'
        cls.assertEqual(print_output, expected_print_output)
        expected_execution_time = 1
        cls.assertEqual(int(execution_time * 10), expected_execution_time)

    def test_sales_manager_shall_respond_through_proxy_with_delay(cls):
        cls.p.busy = 'Yes'
        start_time = time()
        cls.p.talk()
        end_time = time()
        execution_time = end_time - start_time
        print_output = cls.output.getvalue()
        expected_print_output = 'Proxy checking for Sales Manager availability\n\
Sales Manager is busy\n'
        cls.assertEqual(print_output, expected_print_output)
        expected_execution_time = 1
        cls.assertEqual(int(execution_time * 10), expected_execution_time)


class NoTalkProxyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """ Class scope setup. """
        cls.ntp = NoTalkProxy()

    def setUp(cls):
        """ Function/test case scope setup. """
        cls.output = StringIO()
        cls.saved_stdout = sys.stdout
        sys.stdout = cls.output

    def tearDown(cls):
        """ Function/test case scope teardown. """
        cls.output.close()
        sys.stdout = cls.saved_stdout

    def test_sales_manager_shall_not_talk_through_proxy_with_delay(cls):
        cls.ntp.busy = 'No'
        start_time = time()
        cls.ntp.talk()
        end_time = time()
        execution_time = end_time - start_time
        print_output = cls.output.getvalue()
        expected_print_output = 'Proxy checking for Sales Manager availability\n\
This Sales Manager will not talk to you whether he/she is busy or not\n'
        cls.assertEqual(print_output, expected_print_output)
        expected_execution_time = 1
        cls.assertEqual(int(execution_time * 10), expected_execution_time)

    def test_sales_manager_shall_not_respond_through_proxy_with_delay(cls):
        cls.ntp.busy = 'Yes'
        start_time = time()
        cls.ntp.talk()
        end_time = time()
        execution_time = end_time - start_time
        print_output = cls.output.getvalue()
        expected_print_output = 'Proxy checking for Sales Manager availability\n\
This Sales Manager will not talk to you whether he/she is busy or not\n'
        cls.assertEqual(print_output, expected_print_output)
        expected_execution_time = 1
        cls.assertEqual(int(execution_time * 10), expected_execution_time)
