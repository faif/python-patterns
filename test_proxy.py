from proxy import Proxy
from io import StringIO
import sys

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

    def test_sales_manager_shall_work_through_proxy(self):
        self.p.busy = 'No'
        self.p.work()
        print_output = self.output.getvalue()
        expected_print_output = 'Proxy checking for Sales Manager availability\n\
Sales Manager ready to talk\n'
        self.assertEqual(print_output, expected_print_output)

    def test_sales_manager_shall_respond_through_proxy(self):
        self.p.busy = 'Yes'
        self.p.work()
        print_output = self.output.getvalue()
        expected_print_output = 'Proxy checking for Sales Manager availability\n\
Sales Manager is busy\n'
        self.assertEqual(print_output, expected_print_output)

if __name__ == "__main__":
    unittest.main()
