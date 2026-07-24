from patterns.creational.builder import ComplexHouse, Flat, House, construct_building


class TestSimple:
    def test_house(self):
        house = House()
        assert house.size == "Big"
        assert house.floor == "One"

    def test_flat(self):
        flat = Flat()
        assert flat.size == "Small"
        assert flat.floor == "More than One"


class TestComplex:
    def test_house(self):
        house = construct_building(ComplexHouse)
        assert house.size == "Big and fancy"
        assert house.floor == "One"
