import sys
from io import StringIO
from observer import Subject, Data, DecimalViewer, HexViewer

if sys.version_info < (2, 7):
    import unittest2 as unittest
    
else:
    import unittest
    
from unittest.mock import patch

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
        self.dec_obs = DecimalViewer()
        self.hex_obs = HexViewer()
        self.sub = Data('Data')
        #inherited behavior already tested with TestSubject
        self.sub.attach(self.dec_obs)
        self.sub.attach(self.hex_obs)

    def test_data_change_shall_notify_all_observers_once(self):
        with patch.object(self.dec_obs, 'update') as mock_dec_obs_update, patch.object(self.hex_obs, 'update') as mock_hex_obs_update:
                self.sub.data = 10
                self.assertEqual(mock_dec_obs_update.call_count, 1)
                self.assertEqual(mock_hex_obs_update.call_count, 1)

    def test_data_value_shall_be_changeable(self):
        self.sub.data = 20
        self.assertEqual(self.sub._data, 20)

    def test_data_name_shall_be_changeable(self):
        self.sub.name = 'New Data Name'
        self.assertEqual(self.sub.name, 'New Data Name')

if __name__ == "__main__":
    unittest.main()
