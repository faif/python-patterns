"""
Reusable Null Object Pattern Template
=======================================
Copy this file into your project and adapt the base class
and its null counterpart to your domain.

Usage:
    1. Define your real class with actual behavior
    2. Create a Null version that inherits from it
    3. Override methods to do nothing safely
    4. Return the Null version instead of None
"""

from __future__ import annotations


class NullObjectMixin:
    """
    Mixin that provides a standard is_null() check.
    Add this to both your real class and null class.
    """

    def is_null(self) -> bool:
        return False


class NullMixin:
    """
    Mixin for the null version of a class.
    """

    def is_null(self) -> bool:
        return True