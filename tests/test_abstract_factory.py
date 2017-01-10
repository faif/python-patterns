#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from creational.abstract_factory import PetShop,\
    Dog, Cat, DogFactory, CatFactory
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch


class TestPetShop(unittest.TestCase):

    def test_dog_pet_shop_shall_show_dog_instance(self):
        f = DogFactory()
        with patch.object(f, 'get_pet') as mock_f_get_pet,\
                patch.object(f, 'get_food') as mock_f_get_food:
            ps = PetShop(f)
            ps.show_pet()
            self.assertEqual(mock_f_get_pet.call_count, 1)
            self.assertEqual(mock_f_get_food.call_count, 1)

    def test_cat_pet_shop_shall_show_cat_instance(self):
        f = CatFactory()
        with patch.object(f, 'get_pet') as mock_f_get_pet,\
                patch.object(f, 'get_food') as mock_f_get_food:
            ps = PetShop(f)
            ps.show_pet()
            self.assertEqual(mock_f_get_pet.call_count, 1)
            self.assertEqual(mock_f_get_food.call_count, 1)


class TestCat(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.c = Cat()

    def test_cat_shall_meow(cls):
        cls.assertEqual(cls.c.speak(), 'meow')

    def test_cat_shall_be_printable(cls):
        cls.assertEqual(str(cls.c), 'Cat')


class TestDog(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.d = Dog()

    def test_dog_shall_woof(cls):
        cls.assertEqual(cls.d.speak(), 'woof')

    def test_dog_shall_be_printable(cls):
        cls.assertEqual(str(cls.d), 'Dog')
