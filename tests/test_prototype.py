#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from creational.prototype import Prototype, PrototypeDispatcher


class TestPrototypeFeatures(unittest.TestCase):

    def setUp(self):
        self.prototype = Prototype()

    def test_cloning_propperty_innate_values(self):
        sample_object_1 = self.prototype.clone()
        sample_object_2 = self.prototype.clone()
        self.assertEqual(sample_object_1.value, sample_object_2.value)

    def test_extended_property_values_cloning(self):
        sample_object_1 = self.prototype.clone()
        sample_object_1.some_value = 'test string'
        sample_object_2 = self.prototype.clone()
        self.assertRaises(AttributeError, lambda: sample_object_2.some_value)

    def test_cloning_propperty_assigned_values(self):
        sample_object_1 = self.prototype.clone()
        sample_object_2 = self.prototype.clone(value='re-assigned')
        self.assertNotEqual(sample_object_1.value, sample_object_2.value)


class TestDispatcherFeatures(unittest.TestCase):

    def setUp(self):
        self.dispatcher = PrototypeDispatcher()
        self.prototype = Prototype()
        c = self.prototype.clone()
        a = self.prototype.clone(value='a-value', ext_value='E')
        b = self.prototype.clone(value='b-value', diff=True)
        self.dispatcher.register_object('A', a)
        self.dispatcher.register_object('B', b)
        self.dispatcher.register_object('C', c)

    def test_batch_retrieving(self):
        self.assertEqual(len(self.dispatcher.get_objects()), 3)

    def test_particular_properties_retrieving(self):
        self.assertEqual(self.dispatcher.get_objects()['A'].value, 'a-value')
        self.assertEqual(self.dispatcher.get_objects()['B'].value, 'b-value')
        self.assertEqual(self.dispatcher.get_objects()['C'].value, 'default')

    def test_extended_properties_retrieving(self):
        self.assertEqual(self.dispatcher.get_objects()['A'].ext_value, 'E')
        self.assertTrue(self.dispatcher.get_objects()['B'].diff)

