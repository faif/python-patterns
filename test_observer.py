import sys
from io import StringIO
from observer import Subject, Data, DecimalViewer, HexViewer

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest


class TestSubject(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.s = Subject()
        self.dec_obs = DecimalViewer()
        self.hex_obs = HexViewer()

    def test_a_observer_list_shall_be_empty_initially(self):
        self.assertEqual(len(self.s._observers), 0)

    def test_b_observers_shall_be_attachable(self):
        self.s.attach(self.dec_obs)
        self.assertEqual(isinstance(self.s._observers[0], DecimalViewer), True)
        self.assertEqual(len(self.s._observers), 1)
        self.s.attach(self.hex_obs)
        self.assertEqual(isinstance(self.s._observers[1], HexViewer), True)
        self.assertEqual(len(self.s._observers), 2)

    def test_c_observers_shall_be_detachable(self):
        self.s.detach(self.dec_obs)
        # hex viewer shall be remaining if dec viewer is detached first
        self.assertEqual(isinstance(self.s._observers[0], HexViewer), True)
        self.assertEqual(len(self.s._observers), 1)
        self.s.detach(self.hex_obs)
        self.assertEqual(len(self.s._observers), 0)

class TestData(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        dec_obs = DecimalViewer()
        hex_obs = HexViewer()
        self.sub1 = Data('Data 1')
        self.sub2 = Data('Data 2')
        #inherited behavior already tested with TestSubject
        self.sub1.attach(dec_obs)
        self.sub1.attach(hex_obs)
        self.sub2.attach(dec_obs)
        self.sub2.attach(hex_obs)

    def setUp(self):
        self.output = StringIO()
        self.saved_stdout = sys.stdout
        sys.stdout = self.output

#    def test_observers_shall_be_notified(self):
#        self.sub1.data = 10

    def tearDown(self):
        self.output.close()
        sys.stdout = self.saved_stdout

if __name__ == "__main__":
    unittest.main()
