from patterns.creational.lazy_evaluation import Person


class TestDynamicExpanding:
    def setup_method(self):
        self.John = Person("John", "Coder")

    def test_innate_properties(self):
        assert {
            "name": "John",
            "occupation": "Coder",
            "call_count2": 0,
        } == self.John.__dict__

    def test_relatives_not_in_properties(self):
        assert "relatives" not in self.John.__dict__

    def test_extended_properties(self):
        print(f"John's relatives: {self.John.relatives}")
        assert {
            "name": "John",
            "occupation": "Coder",
            "relatives": "Many relatives.",
            "call_count2": 0,
        } == self.John.__dict__

    def test_relatives_after_access(self):
        print(f"John's relatives: {self.John.relatives}")
        assert "relatives" in self.John.__dict__

    def test_parents(self):
        for _ in range(2):
            assert self.John.parents == "Father and mother"
        assert self.John.call_count2 == 1
