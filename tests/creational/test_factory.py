import unittest
from patterns.creational.factory import get_localizer, GreekLocalizer, EnglishLocalizer

class TestFactory(unittest.TestCase):
    def test_get_localizer_greek(self):
        localizer = get_localizer("Greek")
        self.assertIsInstance(localizer, GreekLocalizer)
        self.assertEqual(localizer.localize("dog"), "σκύλος")
        self.assertEqual(localizer.localize("cat"), "γάτα")
        # Test unknown word returns the word itself
        self.assertEqual(localizer.localize("monkey"), "monkey")

    def test_get_localizer_english(self):
        localizer = get_localizer("English")
        self.assertIsInstance(localizer, EnglishLocalizer)
        self.assertEqual(localizer.localize("dog"), "dog")
        self.assertEqual(localizer.localize("cat"), "cat")

    def test_get_localizer_default(self):
        # Test default argument
        localizer = get_localizer()
        self.assertIsInstance(localizer, EnglishLocalizer)

    def test_get_localizer_unknown_language(self):
        # Test fallback for unknown language if applicable, 
        # or just verify what happens. 
        # Based on implementation: localizers.get(language, EnglishLocalizer)()
        # It defaults to EnglishLocalizer for unknown keys.
        localizer = get_localizer("Spanish")
        self.assertIsInstance(localizer, EnglishLocalizer)
