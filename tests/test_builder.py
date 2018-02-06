#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from creational.builder import construct_building, BuilderHouse,  BuilderFlat


class TestHouseBuilding(unittest.TestCase):

    def setUp(self):
        self.building = construct_building(BuilderHouse())

    def test_house_size(self):
        self.assertEqual(self.building.size, 'Big')

    def test_num_floor_in_house(self):
        self.assertEqual(self.building.floor, 'One')


class TestFlatBuilding(unittest.TestCase):

    def setUp(self):
        self.building = construct_building(BuilderFlat())

    def test_house_size(self):
        self.assertEqual(self.building.size, 'Small')

    def test_num_floor_in_house(self):
        self.assertEqual(self.building.floor, 'More than One')
