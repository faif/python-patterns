import pytest

from patterns.behavioral.specification import (
    User,
    UserSpecification,
    SuperUserSpecification,
    Product,
    PriceBelowSpecification,
    InCategorySpecification,
    InStockSpecification,
)


# --- Fixtures ---


@pytest.fixture
def normal_user():
    return User(super_user=False)


@pytest.fixture
def super_user():
    return User(super_user=True)


@pytest.fixture
def products():
    return [
        Product("Python Book", 45.0, "books", True),
        Product("Laptop", 1200.0, "electronics", True),
        Product("Headphones", 80.0, "electronics", False),
        Product("Notebook", 5.0, "stationery", True),
    ]


# --- User Specification Tests ---


def test_user_specification_with_user(normal_user):
    spec = UserSpecification()
    assert spec.is_satisfied_by(normal_user) is True


def test_user_specification_with_non_user():
    spec = UserSpecification()
    assert spec.is_satisfied_by("not a user") is False


def test_super_user_specification_true(super_user):
    spec = SuperUserSpecification()
    assert spec.is_satisfied_by(super_user) is True


def test_super_user_specification_false(normal_user):
    spec = SuperUserSpecification()
    assert spec.is_satisfied_by(normal_user) is False


def test_user_and_super_user_combined(normal_user, super_user):
    spec = UserSpecification().and_specification(SuperUserSpecification())
    assert spec.is_satisfied_by(normal_user) is False
    assert spec.is_satisfied_by(super_user) is True


# --- Product Specification Tests ---


def test_price_below(products):
    spec = PriceBelowSpecification(100)
    result = [p for p in products if spec.is_satisfied_by(p)]
    assert len(result) == 3
    assert all(p.price < 100 for p in result)


def test_in_category(products):
    spec = InCategorySpecification("electronics")
    result = [p for p in products if spec.is_satisfied_by(p)]
    assert len(result) == 2
    assert all(p.category == "electronics" for p in result)


def test_in_stock(products):
    spec = InStockSpecification()
    result = [p for p in products if spec.is_satisfied_by(p)]
    assert len(result) == 3
    assert all(p.in_stock for p in result)


# --- Composite Specification Tests ---


def test_and_specification(products):
    cheap_and_available = PriceBelowSpecification(100).and_specification(
        InStockSpecification()
    )
    result = [p for p in products if cheap_and_available.is_satisfied_by(p)]
    assert [p.name for p in result] == ["Python Book", "Notebook"]


def test_or_specification(products):
    cheap_or_electronics = PriceBelowSpecification(100).or_specification(
        InCategorySpecification("electronics")
    )
    result = [p for p in products if cheap_or_electronics.is_satisfied_by(p)]
    assert len(result) == 4  # All products match


def test_not_specification(products):
    not_in_stock = InStockSpecification().not_specification()
    result = [p for p in products if not_in_stock.is_satisfied_by(p)]
    assert len(result) == 1
    assert result[0].name == "Headphones"


def test_complex_combination(products):
    electronics_out_of_stock = InCategorySpecification(
        "electronics"
    ).and_specification(InStockSpecification().not_specification())
    result = [p for p in products if electronics_out_of_stock.is_satisfied_by(p)]
    assert len(result) == 1
    assert result[0].name == "Headphones"