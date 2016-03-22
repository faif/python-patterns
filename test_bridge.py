#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bridge import DrawingAPI1, DrawingAPI2, CircleShape
from sys import version_info

if version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

from unittest.mock import patch

class BridgeTest(unittest.TestCase):

    def test_bridge_shall_draw_with_concrete_implementation(cls):
        ci1 = DrawingAPI1()
        ci2 = DrawingAPI2()
        with patch.object(ci1, 'draw_circle') as mock_ci1_draw_circle,\
             patch.object(ci2, 'draw_circle') as mock_ci2_draw_circle:
            sh1 = CircleShape(1, 2, 3, ci1)
            sh1.draw()
            cls.assertEqual(mock_ci1_draw_circle.call_count, 1)
            sh2 = CircleShape(1, 2, 3, ci2)
            sh2.draw()
            cls.assertEqual(mock_ci2_draw_circle.call_count, 1)

    def test_bridge_shall_scale_with_own_implementation(cls):
        ci = DrawingAPI1()
        sh = CircleShape(1, 2, 3, ci)
        sh.scale(2)
        cls.assertEqual(sh._radius, 6)
        with patch.object(sh, 'scale') as mock_sh_scale_circle:
            sh.scale(2)
            cls.assertEqual(mock_sh_scale_circle.call_count, 1)

if __name__ == "__main__":
    unittest.main()

