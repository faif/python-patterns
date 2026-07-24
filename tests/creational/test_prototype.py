import pytest

from patterns.creational.prototype import Prototype, PrototypeDispatcher


class TestPrototypeFeatures:
    def setup_method(self):
        self.prototype = Prototype()

    def test_cloning_propperty_innate_values(self):
        sample_object_1 = self.prototype.clone()
        sample_object_2 = self.prototype.clone()
        assert sample_object_1.value == sample_object_2.value

    def test_extended_property_values_cloning(self):
        sample_object_1 = self.prototype.clone()
        sample_object_1.some_value = "test string"
        sample_object_2 = self.prototype.clone()
        pytest.raises(AttributeError, lambda: sample_object_2.some_value)

    def test_cloning_propperty_assigned_values(self):
        sample_object_1 = self.prototype.clone()
        sample_object_2 = self.prototype.clone(value="re-assigned")
        assert sample_object_1.value != sample_object_2.value


class TestDispatcherFeatures:
    def setup_method(self):
        self.dispatcher = PrototypeDispatcher()
        self.prototype = Prototype()
        c = self.prototype.clone()
        a = self.prototype.clone(value="a-value", ext_value="E")
        b = self.prototype.clone(value="b-value", diff=True)
        self.dispatcher.register_object("A", a)
        self.dispatcher.register_object("B", b)
        self.dispatcher.register_object("C", c)

    def test_batch_retrieving(self):
        assert len(self.dispatcher.get_objects()) == 3

    def test_particular_properties_retrieving(self):
        assert self.dispatcher.get_objects()["A"].value == "a-value"
        assert self.dispatcher.get_objects()["B"].value == "b-value"
        assert self.dispatcher.get_objects()["C"].value == "default"

    def test_extended_properties_retrieving(self):
        assert self.dispatcher.get_objects()["A"].ext_value == "E"
        assert self.dispatcher.get_objects()["B"].diff
