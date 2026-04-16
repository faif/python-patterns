import pytest
from patterns.creational.factory import GreekGetter, EnglishGetter
from patterns.behavioral.strategy import Order, ten_percent_discount

def test_factory_logic():
    greek = GreekGetter()
    english = EnglishGetter()
    assert "papadopoulos" in greek.trans["dog"]
    assert "dog" in english.trans["dog"]

def test_strategy_logic():
    order = Order(100, ten_percent_discount)
    assert order.apply_strategy() == 90.0
