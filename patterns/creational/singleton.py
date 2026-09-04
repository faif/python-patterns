"""
https://en.wikipedia.org/wiki/Singleton_pattern

*TL;DR
Ensures a class has only one instance and provides a global point of access to it.
Useful for shared resources such as configuration objects, connection pools, and loggers
where having multiple instances would waste resources or cause inconsistent behavior.

*Examples in Python ecosystem:
Python's logging module returns the same logger instance for the same name, effectively
applying the Singleton pattern: https://docs.python.org/3/library/logging.html#logging.getLogger
"""

# singleton.py

from __future__ import annotations
from typing import Any, Dict


class Singleton:
    """
    Classic Singleton implementation using __new__.

    Ensures that only one instance of the class exists during the lifetime
    of the program. Any subsequent call to the constructor returns the
    same instance that was created on the first call.
    """

    _instance: "Singleton" = None  # type: ignore

    def __new__(cls, *args: Any, **kwargs: Any) -> "Singleton":
        """
        Override the default object creation to return the existing instance
        if one already exists, otherwise create and store a new instance.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


class AppConfig(Singleton):
    """
    Application configuration object implemented as a Singleton.

    All parts of the program that request AppConfig receive the same
    instance, ensuring a single, consistent source of configuration.
    """

    _initialized: bool = False

    def __init__(self) -> None:
        """
        Initialize default settings only on the first instantiation.
        Subsequent instantiations leave the existing settings untouched.
        """
        if self._initialized:
            return
        self._settings: Dict[str, Any] = {
            "database_url": "localhost:5432",
            "debug": False,
            "language": "en",
        }
        self._initialized = True

    def get(self, key: str) -> Any:
        """
        Retrieve a configuration value by key.

        Args:
            key (str): The configuration key to look up.

        Returns:
            The associated configuration value, or None if the key is missing.
        """
        return self._settings.get(key)

    def set(self, key: str, value: Any) -> None:
        """
        Update or add a configuration value.

        Args:
            key (str): The configuration key to set.
            value: The new configuration value.
        """
        self._settings[key] = value


def main():
    """
    >>> config1 = AppConfig()
    >>> config2 = AppConfig()

    # Both variables refer to the exact same instance
    >>> config1 is config2
    True

    # Default settings are accessible from any reference
    >>> config1.get("language")
    'en'
    >>> config2.get("debug")
    False

    # Changing a setting through one reference is visible through the other
    >>> config1.set("language", "ar")
    >>> config2.get("language")
    'ar'

    # Adding a new setting works the same way
    >>> config2.set("theme", "dark")
    >>> config1.get("theme")
    'dark'

    # A missing key returns None
    >>> config1.get("missing_key") is None
    True
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()