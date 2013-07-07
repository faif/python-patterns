#!/user/bin/env python 

"""http://code.activestate.com/recipes/68205-null-object-design-pattern/"""


class Null:
    def __init__(self, *args, **kwargs):
        """Ignore parameters."""
        return None

    def __call__(self, *args, **kwargs):
        """Ignore method calls."""
        return self

    def __getattr__(self, mname):
        """Ignore attribute requests."""
        return self

    def __setattr__(self, name, value):
        """Ignore attribute setting."""
        return self

    def __delattr__(self, name):
        """Ignore deleting attributes."""
        return self

    def __repr__(self):
        """Return a string representation."""
        return "<Null>"

    def __str__(self):
        """Convert to a string and return it."""
        return "Null"


def test():
    """Perform some decent tests, or rather: demos."""

    # constructing and calling

    n = Null()
    print(n)

    n = Null('value')
    print(n)

    n = Null('value', param='value')
    print(n)

    n()
    n('value')
    n('value', param='value')
    print(n)

    # attribute handling

    n.attr1
    print('attr1', n.attr1)
    n.attr1.attr2
    n.method1()
    n.method1().method2()
    n.method('value')
    n.method(param='value')
    n.method('value', param='value')
    n.attr1.method1()
    n.method1().attr1

    n.attr1 = 'value'
    n.attr1.attr2 = 'value'

    del n.attr1
    del n.attr1.attr2.attr3

    # representation and conversion to a string
    
    assert repr(n) == '<Null>'
    assert str(n) == 'Null'


if __name__ == '__main__':
    test()
