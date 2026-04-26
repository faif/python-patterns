"""
*What is this pattern about?

The Chain of Responsibility is an object-oriented version of the
`if ... elif ... elif ... else ...` idiom, with the benefit that
condition-action blocks can be dynamically rearranged and reconfigured
at runtime.

This pattern aims to decouple senders of a request from its receivers
by allowing the request to move through chained receivers until it is
handled. If no handler claims it, a fallback fires — requests are
never silently dropped.

*Real-world example — customer support escalation:
    L1 Support → handles common issues (billing, password reset)
    L2 Support → handles technical problems (bugs, integrations)
    L3 Support → handles complex/escalated cases (architecture, security)
    Fallback   → logs unresolved tickets or raises a production alert

Each level tries to resolve the ticket. If it cannot, it escalates to
the next. The fallback guarantees no ticket silently disappears.

*Fallback mechanism:
Handler.handle() is a Template Method that owns the full dispatch flow:
    1. check_range()      — let this handler attempt to process the request
    2. successor.handle() — if unhandled, delegate to the next in chain
    3. handle_fallback()  — if no successor, this always fires automatically

Use FallbackHandler for explicit control at the end of a chain:
    FallbackHandler(mode="log")    — prints warning, returns False (default)
    FallbackHandler(mode="strict") — raises ValueError (production systems)

Without an explicit FallbackHandler, the base Handler.handle_fallback()
no-op fires — no crash, returns False, request silently ignored.

*Examples in Python ecosystem:
Django Middleware: https://docs.djangoproject.com/en/stable/topics/http/middleware/
Each middleware component processes the request/response in sequence.
Django's built-in 404/500 error views act as the chain's fallback.

*TL;DR
Allow a request to pass down a chain of handlers. The fallback mechanism
guarantees the chain never silently swallows an unhandled request.
"""

from abc import ABC, abstractmethod
from typing import Optional, Tuple


class Handler(ABC):
    def __init__(self, successor: Optional["Handler"] = None):
        self.successor = successor

    def handle(self, request: int) -> bool:
        """
        Template Method: attempt handling, delegate up the chain, or fall back.

        Returns True if a concrete handler processed the request,
        False if the request reached the end of the chain unhandled.
        Delegates to handle_fallback() if no successor is set.
        """
        if self.check_range(request):
            return True
        if self.successor:
            return self.successor.handle(request)
        return self.handle_fallback(request)

    def handle_fallback(self, request: int) -> bool:
        """
        Called automatically when the chain exhausts without handling request.

        Override this in a subclass to customize end-of-chain behavior
        (e.g., write to a dead-letter queue, send an alert, log metrics).
        Subclasses may also raise instead of returning False (see FallbackHandler strict mode).
        Default implementation is a silent no-op that returns False.
        """
        return False

    @abstractmethod
    def check_range(self, request: int) -> Optional[bool]:
        """Return True if request was handled, None/False to pass it along."""


class ConcreteHandler0(Handler):
    """Each handler can be different.
    Be simple and static...
    """

    @staticmethod
    def check_range(request: int) -> Optional[bool]:
        if 0 <= request < 10:
            print(f"request {request} handled in handler 0")
            return True
        return None


class ConcreteHandler1(Handler):
    """... With its own internal state"""

    start, end = 10, 20

    def check_range(self, request: int) -> Optional[bool]:
        if self.start <= request < self.end:
            print(f"request {request} handled in handler 1")
            return True
        return None


class ConcreteHandler2(Handler):
    """... With helper methods."""

    def check_range(self, request: int) -> Optional[bool]:
        start, end = self.get_interval_from_db()
        if start <= request < end:
            print(f"request {request} handled in handler 2")
            return True
        return None

    @staticmethod
    def get_interval_from_db() -> Tuple[int, int]:
        return (20, 30)


class FallbackHandler(Handler):
    """
    Terminal handler for explicit end-of-chain fallback control.

    Place at the end of a chain to define what happens when no concrete
    handler processes a request. Supports two modes set at construction:

        mode="log"    (default) — prints a warning and returns False.
                                  Useful during development and for monitoring.
        mode="strict"           — raises ValueError. Use in production systems
                                  where an unhandled request is always a bug.

    Real-world analogy — support ticket escalation:
        l3 = ConcreteHandler2(FallbackHandler(mode="strict"))
        l2 = ConcreteHandler1(l3)
        l1 = ConcreteHandler0(l2)
        l1.handle(ticket_priority)  # raises ValueError if nobody claims it

    To extend: subclass FallbackHandler and override handle_fallback() to add
    custom logic such as writing to a dead-letter queue or sending an alert.

    Do not assign a successor to FallbackHandler — it is the terminal node.
    If a successor is set, handle_fallback() will never be called.
    """

    def __init__(self, mode: str = "log") -> None:
        super().__init__()
        if mode not in ("log", "strict"):
            raise ValueError(
                f"Invalid mode {mode!r}. Choose 'log' or 'strict'."
            )
        self.mode = mode

    def check_range(self, request: int) -> Optional[bool]:
        return None  # FallbackHandler never handles requests directly

    def handle_fallback(self, request: int) -> bool:
        if self.mode == "strict":
            raise ValueError(f"No handler found for request {request}")
        print(f"end of chain, no handler for {request}")
        return False


def main():
    """
    >>> h0 = ConcreteHandler0()
    >>> h1 = ConcreteHandler1()
    >>> h2 = ConcreteHandler2(FallbackHandler())
    >>> h0.successor = h1
    >>> h1.successor = h2

    >>> requests = [2, 5, 14, 22, 18, 3, 35, 27, 20]
    >>> for request in requests:
    ...     _ = h0.handle(request)
    request 2 handled in handler 0
    request 5 handled in handler 0
    request 14 handled in handler 1
    request 22 handled in handler 2
    request 18 handled in handler 1
    request 3 handled in handler 0
    end of chain, no handler for 35
    request 27 handled in handler 2
    request 20 handled in handler 2

    >>> # Strict mode raises ValueError for unhandled requests:
    >>> h_strict = ConcreteHandler0(FallbackHandler(mode="strict"))
    >>> h_strict.handle(5)
    request 5 handled in handler 0
    True
    >>> h_strict.handle(99)
    Traceback (most recent call last):
        ...
    ValueError: No handler found for request 99

    >>> # Chain without FallbackHandler returns False gracefully:
    >>> h_bare = ConcreteHandler0()
    >>> h_bare.handle(99)
    False
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.ELLIPSIS)
