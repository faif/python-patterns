import pytest

from patterns.fundamental.delegation_pattern import Delegator, Delegate


def test_delegator_delegates_attribute_and_call():
    d = Delegator(Delegate())
    assert d.p1 == 123
    assert d.do_something("something") == "Doing something"
    assert d.do_something("something", kw=", hi") == "Doing something, hi"


def test_delegator_missing_attribute_raises():
    d = Delegator(Delegate())
    with pytest.raises(AttributeError):
        _ = d.p2
