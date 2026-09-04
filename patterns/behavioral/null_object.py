"""
http://code.tutsplus.com/articles/null-object-design-pattern--mobile-19377

*TL;DR
Provides a default object that acts as a surrogate for a missing object,
avoiding the need for null checks throughout the codebase.

*Examples in Python ecosystem:
Python's logging module uses a NullHandler to discard log records when
no other handlers are configured: https://docs.python.org/3/library/logging.handlers.html#logging.NullHandler
"""

# null_object.py

from __future__ import annotations
from typing import Union


class Customer:
    """
    A real customer with actual behavior.
    """

    def __init__(self, name: str, email: str) -> None:
        """
        Initialize a customer with a name and email.

        Args:
            name (str): The customer's name.
            email (str): The customer's email address.
        """
        self.name = name
        self.email = email

    def send_notification(self, message: str) -> None:
        """
        Send a notification to the customer.

        Args:
            message (str): The notification message.
        """
        print(f"Sending '{message}' to {self.name} at {self.email}")

    def is_null(self) -> bool:
        """
        Indicate that this is a real customer, not a null object.
        """
        return False


class NullCustomer(Customer):
    """
    A null object that mimics a Customer but performs no action.
    Used as a safe default when a real customer is not found.
    """

    def __init__(self) -> None:
        """
        Initialize the null customer with default empty values.
        """
        self.name = "N/A"
        self.email = "N/A"

    def send_notification(self, message: str) -> None:
        """
        Override to do nothing instead of sending a notification.

        Args:
            message (str): The notification message (ignored).
        """
        pass

    def is_null(self) -> bool:
        """
        Indicate that this is a null customer.
        """
        return True


class CustomerRepository:
    """
    A simple repository that stores and retrieves customers.
    Returns a NullCustomer when the requested customer is not found.
    """

    def __init__(self) -> None:
        self._customers = {
            1: Customer("Ahmed", "ahmed@example.com"),
            2: Customer("Sara", "sara@example.com"),
        }

    def get_customer(self, customer_id: int) -> Union[Customer, NullCustomer]:
        """
        Retrieve a customer by ID, or return a NullCustomer if not found.

        Args:
            customer_id (int): The customer's unique identifier.

        Returns:
            Customer or NullCustomer: The matching customer or a null object.
        """
        return self._customers.get(customer_id, NullCustomer())


def main():
    """
    >>> repo = CustomerRepository()

    # Retrieve an existing customer and send a notification
    >>> customer = repo.get_customer(1)
    >>> customer.is_null()
    False
    >>> customer.send_notification("Your order has shipped")
    Sending 'Your order has shipped' to Ahmed at ahmed@example.com

    # Retrieve a non-existing customer - returns NullCustomer
    >>> missing = repo.get_customer(999)
    >>> missing.is_null()
    True

    # Calling methods on NullCustomer is safe and does nothing
    >>> missing.send_notification("Your order has shipped")

    # No null checks needed - the code stays clean
    >>> for customer_id in [1, 2, 999]:
    ...     repo.get_customer(customer_id).send_notification("Hello")
    Sending 'Hello' to Ahmed at ahmed@example.com
    Sending 'Hello' to Sara at sara@example.com
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()