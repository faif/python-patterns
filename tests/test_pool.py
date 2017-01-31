#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
try:
    import queue
except ImportError:  # python 2.x compatibility
    import Queue as queue
from creational.pool import ObjectPool


class TestPool(unittest.TestCase):

    def setUp(self):
        self.sample_queue = queue.Queue()
        self.sample_queue.put('first')
        self.sample_queue.put('second')

    def test_items_recoil(self):
        with ObjectPool(self.sample_queue, True) as pool:
            self.assertEqual(pool, 'first')
        self.assertTrue(self.sample_queue.get() == 'second')
        self.assertFalse(self.sample_queue.empty())
        self.assertTrue(self.sample_queue.get() == 'first')
        self.assertTrue(self.sample_queue.empty())

    def test_frozen_pool(self):
        with ObjectPool(self.sample_queue) as pool:
            self.assertEqual(pool, 'first')
            self.assertEqual(pool, 'first')
        self.assertTrue(self.sample_queue.get() == 'second')
        self.assertFalse(self.sample_queue.empty())
        self.assertTrue(self.sample_queue.get() == 'first')
        self.assertTrue(self.sample_queue.empty())
