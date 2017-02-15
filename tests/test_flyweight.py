#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from structural.flyweight import Card


class TestCard(unittest.TestCase):

    def test_instances_shall_reference_same_object(self):
        c1 = Card('9', 'h')
        c2 = Card('9', 'h')
        self.assertEqual(c1, c2)
        self.assertEqual(id(c1), id(c2))

    def test_instances_with_different_suit(self):
        """
        shall reference different objects
        """
        c1 = Card('9', 'a')
        c2 = Card('9', 'b')
        self.assertNotEqual(id(c1), id(c2))

    def test_instances_with_different_values(self):
        """
        shall reference different objects
        """
        c1 = Card('9', 'h')
        c2 = Card('A', 'h')
        self.assertNotEqual(id(c1), id(c2))

    def test_instances_shall_share_additional_attributes(self):
        expected_attribute_name = 'attr'
        expected_attribute_value = 'value of attr'
        c1 = Card('9', 'h')
        c1.attr = expected_attribute_value
        c2 = Card('9', 'h')
        self.assertEqual(hasattr(c2, expected_attribute_name), True)
        self.assertEqual(c2.attr, expected_attribute_value)
