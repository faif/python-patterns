from patterns.structural.flyweight import Card


def test_card_flyweight_identity_and_repr():
    c1 = Card("9", "h")
    c2 = Card("9", "h")
    assert c1 is c2
    assert repr(c1) == "<Card: 9h>"


def test_card_attribute_persistence_and_pool_clear():
    Card._pool.clear()
    c1 = Card("A", "s")
    c1.temp = "t"
    c2 = Card("A", "s")
    assert hasattr(c2, "temp")

    Card._pool.clear()
    c3 = Card("A", "s")
    assert not hasattr(c3, "temp")
