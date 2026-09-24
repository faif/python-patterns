from patterns.structural.flyweight_with_metaclass import Card2


def test_same_arguments_share_an_instance():
    Card2.pool.clear()
    assert Card2("10", "h", a=1) is Card2("10", "h", a=1)


def test_different_arguments_do_not_share_an_instance():
    Card2.pool.clear()
    assert Card2("10", "h", a=1) is not Card2("10", "h", a=2)


def test_argument_boundaries_are_part_of_the_key():
    Card2.pool.clear()
    assert Card2("1", "0") is not Card2("10")


def test_argument_types_are_part_of_the_key():
    Card2.pool.clear()
    assert Card2(1) is not Card2("1")


def test_keyword_argument_order_does_not_matter():
    Card2.pool.clear()
    assert Card2(a=1, b=2) is Card2(b=2, a=1)
