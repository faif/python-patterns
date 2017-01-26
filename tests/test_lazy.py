#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from creational.lazy_evaluation import Person


class TestDynamicExpanding(unittest.TestCase):

    def setUp(self):
        self.John = Person('John', 'Coder')

    def test_innate_properties(self):
        self.assertDictEqual({'name': 'John', 'occupation': 'Coder'},
                             self.John.__dict__)

    def test_extended_properties(self):
        print("Jhon's relatives: {0}".format(self.John.relatives))
        self.assertDictEqual({'name': 'John', 'occupation': 'Coder',
                              'relatives': 'Many relatives.'},
                             self.John.__dict__)
