"""
@author: Gordeev Andrey <gordeev.and.and@gmail.com>

https://en.wikipedia.org/wiki/Specification_pattern

*TL;DR
Encapsulates business rules as standalone objects that can be combined using
boolean logic (AND, OR, NOT). This allows complex selection criteria to be
built dynamically without hardcoding conditions throughout the codebase.

*Examples in Python ecosystem:
Django QuerySet API uses Q objects to compose database queries with logical
operators, applying the same composition principle as the Specification pattern:
https://docs.djangoproject.com/en/stable/topics/db/queries/#complex-lookups-with-q-objects
"""

from abc import abstractmethod
from typing import Union


class Specification:
    """
    Base interface for all specifications.

    A specification encapsulates a single business rule and can be combined
    with other specifications using logical operators.
    """

    def and_specification(self, candidate):
        """Combine this specification with another using logical AND."""
        raise NotImplementedError()

    def or_specification(self, candidate):
        """Combine this specification with another using logical OR."""
        raise NotImplementedError()

    def not_specification(self):
        """Return the logical negation of this specification."""
        raise NotImplementedError()

    @abstractmethod
    def is_satisfied_by(self, candidate):
        """
        Check whether the given candidate satisfies this specification.

        Args:
            candidate: The object to evaluate against the rule.

        Returns:
            bool: True if the candidate satisfies the rule, otherwise False.
        """
        pass


class CompositeSpecification(Specification):
    """
    Abstract specification that provides default implementations for
    combining specifications using AND, OR, and NOT.

    All concrete specifications should inherit from this class to gain
    automatic support for logical composition.
    """

    @abstractmethod
    def is_satisfied_by(self, candidate):
        pass

    def and_specification(self, candidate: "Specification") -> "AndSpecification":
        """Return a new specification that is satisfied when both rules are satisfied."""
        return AndSpecification(self, candidate)

    def or_specification(self, candidate: "Specification") -> "OrSpecification":
        """Return a new specification that is satisfied when at least one rule is satisfied."""
        return OrSpecification(self, candidate)

    def not_specification(self) -> "NotSpecification":
        """Return a new specification that is satisfied when this rule is NOT satisfied."""
        return NotSpecification(self)


class AndSpecification(CompositeSpecification):
    """
    Composite specification satisfied only when BOTH inner specifications are satisfied.
    """

    def __init__(self, one: "Specification", other: "Specification") -> None:
        self._one: Specification = one
        self._other: Specification = other

    def is_satisfied_by(self, candidate) -> bool:
        return bool(
            self._one.is_satisfied_by(candidate)
            and self._other.is_satisfied_by(candidate)
        )


class OrSpecification(CompositeSpecification):
    """
    Composite specification satisfied when AT LEAST ONE of the inner specifications is satisfied.
    """

    def __init__(self, one: "Specification", other: "Specification") -> None:
        self._one: Specification = one
        self._other: Specification = other

    def is_satisfied_by(self, candidate) -> bool:
        return bool(
            self._one.is_satisfied_by(candidate)
            or self._other.is_satisfied_by(candidate)
        )


class NotSpecification(CompositeSpecification):
    """
    Composite specification satisfied when the wrapped specification is NOT satisfied.
    """

    def __init__(self, wrapped: "Specification") -> None:
        self._wrapped: Specification = wrapped

    def is_satisfied_by(self, candidate) -> bool:
        return bool(not self._wrapped.is_satisfied_by(candidate))


# ---------------------------------------------------------------------------
# Original example: User / SuperUser
# ---------------------------------------------------------------------------


class User:
    def __init__(self, super_user: bool = False) -> None:
        self.super_user = super_user


class UserSpecification(CompositeSpecification):
    """Specification satisfied when the candidate is a User instance."""

    def is_satisfied_by(self, candidate) -> bool:
        return isinstance(candidate, User)


class SuperUserSpecification(CompositeSpecification):
    """Specification satisfied when the candidate is a super-user."""

    def is_satisfied_by(self, candidate) -> bool:
        return getattr(candidate, "super_user", False)


# ---------------------------------------------------------------------------
# Real-world example: filtering products in an e-commerce catalog
# ---------------------------------------------------------------------------


class Product:
    """A simple product in an e-commerce catalog."""

    def __init__(self, name: str, price: float, category: str, in_stock: bool) -> None:
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock

    def __repr__(self) -> str:
        return self.name


class PriceBelowSpecification(CompositeSpecification):
    """Specification satisfied when the product's price is below a given limit."""

    def __init__(self, limit: float) -> None:
        self._limit = limit

    def is_satisfied_by(self, candidate: Product) -> bool:
        return candidate.price < self._limit


class InCategorySpecification(CompositeSpecification):
    """Specification satisfied when the product belongs to a given category."""

    def __init__(self, category: str) -> None:
        self._category = category

    def is_satisfied_by(self, candidate: Product) -> bool:
        return candidate.category == self._category


class InStockSpecification(CompositeSpecification):
    """Specification satisfied when the product is in stock."""

    def is_satisfied_by(self, candidate: Product) -> bool:
        return candidate.in_stock


def main():
    """
    >>> andrey = User()
    >>> ivan = User(super_user=True)
    >>> vasiliy = 'not User instance'

    >>> root_specification = UserSpecification().and_specification(SuperUserSpecification())

    # Is specification satisfied by <name>
    >>> root_specification.is_satisfied_by(andrey), 'andrey'
    (False, 'andrey')
    >>> root_specification.is_satisfied_by(ivan), 'ivan'
    (True, 'ivan')
    >>> root_specification.is_satisfied_by(vasiliy), 'vasiliy'
    (False, 'vasiliy')

    # Real-world example: filtering products in an e-commerce catalog
    >>> products = [
    ...     Product('Python Book', 45.0, 'books', True),
    ...     Product('Laptop', 1200.0, 'electronics', True),
    ...     Product('Headphones', 80.0, 'electronics', False),
    ...     Product('Notebook', 5.0, 'stationery', True),
    ... ]

    # Build composable rules
    >>> cheap = PriceBelowSpecification(100)
    >>> electronics = InCategorySpecification('electronics')
    >>> available = InStockSpecification()

    # Show cheap products that are in stock
    >>> cheap_and_available = cheap.and_specification(available)
    >>> [p for p in products if cheap_and_available.is_satisfied_by(p)]
    [Python Book, Notebook]

    # Show electronics that are out of stock (using NOT)
    >>> out_of_stock_electronics = electronics.and_specification(available.not_specification())
    >>> [p for p in products if out_of_stock_electronics.is_satisfied_by(p)]
    [Headphones]

    # Show cheap items OR electronics
    >>> cheap_or_electronics = cheap.or_specification(electronics)
    >>> [p for p in products if cheap_or_electronics.is_satisfied_by(p)]
    [Python Book, Laptop, Headphones, Notebook]
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()