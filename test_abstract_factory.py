#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abstract_factory import PetShop, Dog, Cat, DogFactory, CatFactory
import sys

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

from unittest.mock import patch

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

if __name__ == "__main__":
    unittest.main()

