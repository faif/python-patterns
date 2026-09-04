"""
Reusable Singleton Pattern Template
=====================================
Copy this file into your project and inherit from Singleton
for any class that must have only one instance.

Usage:
    1. Inherit your class from Singleton
    2. Use _initialized flag to prevent re-initialization
    3. All calls to YourClass() return the same instance
"""

from __future__ import annotations
from typing import Any


class Singleton:
    """
    Base Singleton class. Any class inheriting from this will only
    ever have one instance throughout the program's lifetime.
    """

    _instance = None

    def __new__(cls, *args: Any, **kwargs: Any):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance