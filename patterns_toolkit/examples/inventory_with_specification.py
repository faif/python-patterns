"""
Example: Specification Pattern Applied to an Inventory Management System
=========================================================================
This example shows how the Specification pattern can be used to create
flexible, composable filters for inventory queries.

This directly relates to an Inventory Management System project,
demonstrating how design patterns integrate into real-world applications.
"""

from __future__ import annotations
from abc import abstractmethod
from typing import List


# --- Specification Base ---


class Specification:
    @abstractmethod
    def is_satisfied_by(self, candidate) -> bool:
        pass

    def and_(self, other: Specification) -> AndSpec:
        return AndSpec(self, other)

    def or_(self, other: Specification) -> OrSpec:
        return OrSpec(self, other)

    def not_(self) -> NotSpec:
        return NotSpec(self)


class AndSpec(Specification):
    def __init__(self, one: Specification, other: Specification) -> None:
        self._one = one
        self._other = other

    def is_satisfied_by(self, candidate) -> bool:
        return self._one.is_satisfied_by(candidate) and self._other.is_satisfied_by(candidate)


class OrSpec(Specification):
    def __init__(self, one: Specification, other: Specification) -> None:
        self._one = one
        self._other = other

    def is_satisfied_by(self, candidate) -> bool:
        return self._one.is_satisfied_by(candidate) or self._other.is_satisfied_by(candidate)


class NotSpec(Specification):
    def __init__(self, wrapped: Specification) -> None:
        self._wrapped = wrapped

    def is_satisfied_by(self, candidate) -> bool:
        return not self._wrapped.is_satisfied_by(candidate)


# --- Inventory Domain ---


class InventoryItem:
    """A product in the inventory system."""

    def __init__(
        self, name: str, category: str, quantity: int, price: float, supplier: str
    ) -> None:
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.supplier = supplier

    def __repr__(self) -> str:
        return f"{self.name} (qty: {self.quantity})"


# --- Inventory Specifications ---


class LowStockSpec(Specification):
    """Items with quantity below a minimum threshold."""

    def __init__(self, minimum: int = 10) -> None:
        self._minimum = minimum

    def is_satisfied_by(self, candidate: InventoryItem) -> bool:
        return candidate.quantity < self._minimum


class InCategorySpec(Specification):
    """Items belonging to a specific category."""

    def __init__(self, category: str) -> None:
        self._category = category

    def is_satisfied_by(self, candidate: InventoryItem) -> bool:
        return candidate.category == self._category


class PriceAboveSpec(Specification):
    """Items priced above a certain amount."""

    def __init__(self, amount: float) -> None:
        self._amount = amount

    def is_satisfied_by(self, candidate: InventoryItem) -> bool:
        return candidate.price > self._amount


class FromSupplierSpec(Specification):
    """Items from a specific supplier."""

    def __init__(self, supplier: str) -> None:
        self._supplier = supplier

    def is_satisfied_by(self, candidate: InventoryItem) -> bool:
        return candidate.supplier == self._supplier


class OutOfStockSpec(Specification):
    """Items with zero quantity."""

    def is_satisfied_by(self, candidate: InventoryItem) -> bool:
        return candidate.quantity == 0


def main():
    """
    >>> inventory = [
    ...     InventoryItem("Laptop", "electronics", 25, 1200.0, "TechCorp"),
    ...     InventoryItem("Mouse", "electronics", 3, 25.0, "TechCorp"),
    ...     InventoryItem("Desk", "furniture", 8, 350.0, "OfficePlus"),
    ...     InventoryItem("Chair", "furniture", 0, 200.0, "OfficePlus"),
    ...     InventoryItem("Notebook", "stationery", 150, 3.0, "PaperWorld"),
    ...     InventoryItem("Pen", "stationery", 5, 1.5, "PaperWorld"),
    ... ]

    # Find low stock items (below 10 units)
    >>> low_stock = LowStockSpec(10)
    >>> [i for i in inventory if low_stock.is_satisfied_by(i)]
    [Mouse (qty: 3), Desk (qty: 8), Chair (qty: 0), Pen (qty: 5)]

    # Find out-of-stock items
    >>> out_of_stock = OutOfStockSpec()
    >>> [i for i in inventory if out_of_stock.is_satisfied_by(i)]
    [Chair (qty: 0)]

    # Find low stock electronics (combining two rules)
    >>> low_stock_electronics = low_stock.and_(InCategorySpec("electronics"))
    >>> [i for i in inventory if low_stock_electronics.is_satisfied_by(i)]
    [Mouse (qty: 3)]

    # Find expensive items from TechCorp
    >>> expensive_techcorp = PriceAboveSpec(100).and_(FromSupplierSpec("TechCorp"))
    >>> [i for i in inventory if expensive_techcorp.is_satisfied_by(i)]
    [Laptop (qty: 25)]

    # Find items that need reordering: low stock OR out of stock
    >>> needs_reorder = low_stock.or_(out_of_stock)
    >>> [i for i in inventory if needs_reorder.is_satisfied_by(i)]
    [Mouse (qty: 3), Desk (qty: 8), Chair (qty: 0), Pen (qty: 5)]

    # Find furniture that is NOT out of stock
    >>> available_furniture = InCategorySpec("furniture").and_(out_of_stock.not_())
    >>> [i for i in inventory if available_furniture.is_satisfied_by(i)]
    [Desk (qty: 8)]
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()