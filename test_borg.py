#!/usr/bin/env python
from borg import Borg, YourBorg
import sys

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

class BorgTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.b1 = Borg()
        self.b2 = Borg()
        self.ib1 = YourBorg()

    def test_initial_borg_state_shall_be_init(self):
        b = Borg()
        self.assertEqual(b.state, 'Init')

    def test_changing_instance_attribute_shall_change_borg_state(self):
        self.b1.state = 'Running'
        self.assertEqual(self.b1.state, 'Running')
        self.assertEqual(self.b2.state, 'Running')
        self.assertEqual(self.ib1.state, 'Running')

    def test_instances_shall_have_own_ids(self):
        self.assertNotEqual(id(self.b1), id(self.b2), id(self.ib1))

if __name__ == "__main__":
    unittest.main()
