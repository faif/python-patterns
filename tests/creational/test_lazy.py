import unittest

from patterns.creational.lazy_evaluation import Person


class TestDynamicExpanding(unittest.TestCase):
    def setUp(self):
        self.John = Person("John", "Coder")

    def test_innate_properties(self):
        self.assertDictEqual(
            {"name": "John", "occupation": "Coder", "call_count2": 0},
            self.John.__dict__,
        )

    def test_relatives_not_in_properties(self):
        self.assertNotIn("relatives", self.John.__dict__)

    def test_extended_properties(self):
        print(f"John's relatives: {self.John.relatives}")
        self.assertDictEqual(
            {
                "name": "John",
                "occupation": "Coder",
                "relatives": "Many relatives.",
                "call_count2": 0,
            },
            self.John.__dict__,
        )

    def test_relatives_after_access(self):
        print(f"John's relatives: {self.John.relatives}")
        self.assertIn("relatives", self.John.__dict__)

    def test_parents(self):
        for _ in range(2):
            self.assertEqual(self.John.parents, "Father and mother")
        self.assertEqual(self.John.call_count2, 1)
