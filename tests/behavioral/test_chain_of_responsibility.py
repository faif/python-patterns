import pytest
from patterns.behavioral.chain_of_responsibility import (
    ConcreteHandler0,
    ConcreteHandler1,
    ConcreteHandler2,
    FallbackHandler,
)

# These tests are written in TDD style — they currently fail because:
#   - Handler.handle() returns None (planned to return bool)
#   - FallbackHandler has no mode= parameter (planned in next task)
# Failures are intentional. Subsequent tasks implement against these tests.


def make_chain(fallback=None):
    """Build h0 -> h1 -> h2 -> fallback (optional)."""
    h2 = ConcreteHandler2(fallback)
    h1 = ConcreteHandler1(h2)
    h0 = ConcreteHandler0(h1)
    return h0


class TestHandlerRouting:
    """handle() returns True when a concrete handler processes the request."""

    def test_routes_to_handler0(self):
        assert make_chain().handle(5) is True

    def test_routes_to_handler1(self):
        assert make_chain().handle(15) is True

    def test_routes_to_handler2(self):
        assert make_chain().handle(25) is True

    def test_boundary_value_handler0(self):
        assert make_chain().handle(0) is True  # range is [0, 10)

    def test_boundary_value_handler1(self):
        assert make_chain().handle(10) is True  # range is [10, 20)

    def test_boundary_value_handler2(self):
        assert make_chain().handle(20) is True  # range is [20, 30)


class TestChainWithoutExplicitFallback:
    """When no FallbackHandler is chained, the base no-op fires — no crash."""

    def test_returns_false_when_no_handler_matches(self):
        chain = make_chain()  # No FallbackHandler
        assert chain.handle(99) is False

    def test_does_not_raise(self):
        chain = make_chain()
        chain.handle(99)  # must not raise


class TestFallbackLogMode:
    """FallbackHandler(mode='log') prints a warning and returns False."""

    def test_returns_false(self):
        chain = make_chain(FallbackHandler(mode="log"))
        assert chain.handle(99) is False

    def test_prints_warning(self, capsys):
        chain = make_chain(FallbackHandler(mode="log"))
        chain.handle(99)
        captured = capsys.readouterr()
        assert captured.out.strip() == "end of chain, no handler for 99"

    def test_default_mode_is_log(self, capsys):
        chain = make_chain(FallbackHandler())
        result = chain.handle(99)
        captured = capsys.readouterr()
        assert result is False
        assert "no handler for 99" in captured.out

    def test_does_not_raise(self):
        chain = make_chain(FallbackHandler(mode="log"))
        chain.handle(99)  # must not raise, unlike strict mode


class TestFallbackStrictMode:
    """FallbackHandler(mode='strict') raises ValueError for unhandled requests."""

    def test_raises_value_error(self):
        chain = make_chain(FallbackHandler(mode="strict"))
        with pytest.raises(ValueError, match="No handler found for request 99"):
            chain.handle(99)

    def test_does_not_raise_for_handled_request(self):
        chain = make_chain(FallbackHandler(mode="strict"))
        assert chain.handle(5) is True  # handled by ConcreteHandler0, strict never fires


class TestFallbackHandlerValidation:
    """FallbackHandler rejects unknown modes at construction time."""

    def test_invalid_mode_raises(self):
        with pytest.raises(ValueError, match="Invalid mode"):
            FallbackHandler(mode="invalid")

    def test_valid_modes_do_not_raise(self):
        FallbackHandler(mode="log")
        FallbackHandler(mode="strict")
