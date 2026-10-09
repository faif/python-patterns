"""
Reusable Specification Pattern Template
=========================================
Copy this file into your project and create concrete specifications
for your business rules. Combine them freely with and_/or_/not_.

Usage:
    1. Inherit from CompositeSpecification
    2. Implement is_satisfied_by() for each business rule
    3. Combine specifications: spec_a.and_(spec_b).or_(spec_c)
"""

from __future__ import annotations
from abc import abstractmethod


class Specification:
    """Base specification interface."""

    @abstractmethod
    def is_satisfied_by(self, candidate) -> bool:
        pass

    def and_(self, other: Specification) -> AndSpecification:
        return AndSpecification(self, other)

    def or_(self, other: Specification) -> OrSpecification:
        return OrSpecification(self, other)

    def not_(self) -> NotSpecification:
        return NotSpecification(self)


class AndSpecification(Specification):
    def __init__(self, one: Specification, other: Specification) -> None:
        self._one = one
        self._other = other

    def is_satisfied_by(self, candidate) -> bool:
        return self._one.is_satisfied_by(candidate) and self._other.is_satisfied_by(candidate)


class OrSpecification(Specification):
    def __init__(self, one: Specification, other: Specification) -> None:
        self._one = one
        self._other = other

    def is_satisfied_by(self, candidate) -> bool:
        return self._one.is_satisfied_by(candidate) or self._other.is_satisfied_by(candidate)


class NotSpecification(Specification):
    def __init__(self, wrapped: Specification) -> None:
        self._wrapped = wrapped

    def is_satisfied_by(self, candidate) -> bool:
        return not self._wrapped.is_satisfied_by(candidate)