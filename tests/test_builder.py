#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from creational.builder import Director, BuilderHouse,  BuilderFlat


class TestHouseBuilding(unittest.TestCase):

    def setUp(self):
        self.director = Director()
        self.director.builder = BuilderHouse()
        self.director.construct_building()
        self.building = self.director.get_building()

    def test_house_size(self):
        self.assertEqual(self.building.size, 'Big')

    def test_num_floor_in_house(self):
        self.assertEqual(self.building.floor, 'One')


class TestFlatBuilding(unittest.TestCase):

    def setUp(self):
        self.director = Director()
        self.director.builder = BuilderFlat()
        self.director.construct_building()
        self.building = self.director.get_building()

    def test_house_size(self):
        self.assertEqual(self.building.size, 'Small')

    def test_num_floor_in_house(self):
        self.assertEqual(self.building.floor, 'More than One')
