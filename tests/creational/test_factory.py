from patterns.creational.factory import EnglishLocalizer, GreekLocalizer, get_localizer


class TestFactory:
    def test_get_localizer_greek(self):
        localizer = get_localizer("Greek")
        assert isinstance(localizer, GreekLocalizer)
        assert localizer.localize("dog") == "σκύλος"
        assert localizer.localize("cat") == "γάτα"
        # Test unknown word returns the word itself
        assert localizer.localize("monkey") == "monkey"

    def test_get_localizer_english(self):
        localizer = get_localizer("English")
        assert isinstance(localizer, EnglishLocalizer)
        assert localizer.localize("dog") == "dog"
        assert localizer.localize("cat") == "cat"

    def test_get_localizer_default(self):
        # Test default argument
        localizer = get_localizer()
        assert isinstance(localizer, EnglishLocalizer)

    def test_get_localizer_unknown_language(self):
        # Test fallback for unknown language if applicable,
        # or just verify what happens.
        # Based on implementation: localizers.get(language, EnglishLocalizer)()
        # It defaults to EnglishLocalizer for unknown keys.
        localizer = get_localizer("Spanish")
        assert isinstance(localizer, EnglishLocalizer)
