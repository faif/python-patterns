import pytest

from patterns.behavioral.visitor import A, B, C, Visitor

@pytest.fixture
def visitor():
    return Visitor()

def test_visiting_generic_node(visitor):
    a = A()
    token = visitor.visit(a)
    assert token == 'generic_visit A', "The expected generic object was not called"

def test_visiting_specific_nodes(visitor):
    b = B()
    token = visitor.visit(b)
    assert token == 'visit_B B', "The expected specific object was not called"

def test_visiting_inherited_nodes(visitor):
    c = C()
    token = visitor.visit(c)
    assert token == 'visit_B C', "The expected inherited object was not called"
