#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from patterns.creational.builder import construct_building, House, Flat, ComplexHouse


class TestSimple(unittest.TestCase):
    def test_house(self):
        house = House()
        self.assertEqual(house.size, 'Big')
        self.assertEqual(house.floor, 'One')

    def test_flat(self):
        flat = Flat()
        self.assertEqual(flat.size, 'Small')
        self.assertEqual(flat.floor, 'More than One')


class TestComplex(unittest.TestCase):
    def test_house(self):
        house = construct_building(ComplexHouse)
        self.assertEqual(house.size, 'Big and fancy')
        self.assertEqual(house.floor, 'One')
