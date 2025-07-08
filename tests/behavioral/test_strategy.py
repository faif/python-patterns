import pytest

from patterns.behavioral.strategy import Order, on_sale_discount, ten_percent_discount


@pytest.fixture
def order():
    return Order(100)


@pytest.mark.parametrize(
    "func, discount", [(ten_percent_discount, 10.0), (on_sale_discount, 45.0)]
)
def test_discount_function_return(func, order, discount):
    assert func(order) == discount


@pytest.mark.parametrize(
    "func, price", [(ten_percent_discount, 100), (on_sale_discount, 100)]
)
def test_order_discount_strategy_validate_success(func, price):
    order = Order(price, func)

    assert order.price == price
    assert order.discount_strategy == func


def test_order_discount_strategy_validate_error():
    order = Order(10, discount_strategy=on_sale_discount)

    assert order.discount_strategy is None


@pytest.mark.parametrize(
    "func, price, discount",
    [(ten_percent_discount, 100, 90.0), (on_sale_discount, 100, 55.0)],
)
def test_discount_apply_success(func, price, discount):
    order = Order(price, func)

    assert order.apply_discount() == discount
