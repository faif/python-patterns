import unittest
from unittest.mock import patch

from patterns.structural.bridge import CircleShape, DrawingAPI1, DrawingAPI2


class BridgeTest(unittest.TestCase):
    def test_bridge_shall_draw_with_concrete_api_implementation(cls):
        ci1 = DrawingAPI1()
        ci2 = DrawingAPI2()
        with patch.object(ci1, "draw_circle") as mock_ci1_draw_circle, patch.object(
            ci2, "draw_circle"
        ) as mock_ci2_draw_circle:
            sh1 = CircleShape(1, 2, 3, ci1)
            sh1.draw()
            cls.assertEqual(mock_ci1_draw_circle.call_count, 1)
            sh2 = CircleShape(1, 2, 3, ci2)
            sh2.draw()
            cls.assertEqual(mock_ci2_draw_circle.call_count, 1)

    def test_bridge_shall_scale_both_api_circles_with_own_implementation(cls):
        SCALE_FACTOR = 2
        CIRCLE1_RADIUS = 3
        EXPECTED_CIRCLE1_RADIUS = 6
        CIRCLE2_RADIUS = CIRCLE1_RADIUS * CIRCLE1_RADIUS
        EXPECTED_CIRCLE2_RADIUS = CIRCLE2_RADIUS * SCALE_FACTOR

        ci1 = DrawingAPI1()
        ci2 = DrawingAPI2()
        sh1 = CircleShape(1, 2, CIRCLE1_RADIUS, ci1)
        sh2 = CircleShape(1, 2, CIRCLE2_RADIUS, ci2)
        sh1.scale(SCALE_FACTOR)
        sh2.scale(SCALE_FACTOR)
        cls.assertEqual(sh1._radius, EXPECTED_CIRCLE1_RADIUS)
        cls.assertEqual(sh2._radius, EXPECTED_CIRCLE2_RADIUS)
        with patch.object(sh1, "scale") as mock_sh1_scale_circle, patch.object(
            sh2, "scale"
        ) as mock_sh2_scale_circle:
            sh1.scale(2)
            sh2.scale(2)
            cls.assertEqual(mock_sh1_scale_circle.call_count, 1)
            cls.assertEqual(mock_sh2_scale_circle.call_count, 1)
