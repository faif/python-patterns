from patterns.structural.decorator import BoldWrapper, ItalicWrapper, TextTag


class TestTextWrapping:
    def setup_method(self):
        self.raw_string = TextTag("raw but not cruel")

    def test_italic(self):
        assert ItalicWrapper(self.raw_string).render() == "<i>raw but not cruel</i>"

    def test_bold(self):
        assert BoldWrapper(self.raw_string).render() == "<b>raw but not cruel</b>"

    def test_mixed_bold_and_italic(self):
        assert (
            BoldWrapper(ItalicWrapper(self.raw_string)).render()
            == "<b><i>raw but not cruel</i></b>"
        )
