import unittest

from patterns.creational.singleton import Sun


class TestSingletonCreation(unittest.TestCase):

    def test_define_multiple_objects(self):
        sample_object_1 = Sun()
        sample_object_2 = Sun()
        self.assertEqual(sample_object_1, sample_object_2)
