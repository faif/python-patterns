#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from creational.borg import Borg, YourBorg


class BorgTest(unittest.TestCase):

    def setUp(self):
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
