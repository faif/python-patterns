#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from creational.factory_method import get_localizer


class TestLocalizer(unittest.TestCase):

    def setUp(self):
        self.e, self.g = get_localizer(language="English"), \
                         get_localizer(language="Greek")

    def test_parrot_eng_localization(self):
        self.assertEqual(self.e.get('parrot'), 'parrot')

    def test_parrot_greek_localization(self):
        self.assertEqual(self.g.get('parrot'), 'parrot')

    def test_dog_eng_localization(self):
        self.assertEqual(self.e.get('dog'), 'dog')

    def test_dog_greek_localization(self):
        self.assertEqual(self.g.get('dog'), 'σκύλος')

    def test_cat_eng_localization(self):
        self.assertEqual(self.e.get('cat'), 'cat')

    def test_cat_greek_localization(self):
        self.assertEqual(self.g.get('cat'), 'γάτα')

    def test_bear_eng_localization(self):
        self.assertEqual(self.e.get('bear'), 'bear')

    def test_bear_greek_localization(self):
        self.assertEqual(self.g.get('bear'), 'bear')
