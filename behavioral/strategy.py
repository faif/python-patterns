#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*What is this pattern about?
Define a family of algorithms, encapsulate each one, and make them interchangeable.
Strategy lets the algorithm vary independently from clients that use it.

*TL;DR80
Enables selecting an algorithm at runtime.
"""


class Order:
    def __init__(self, price, discount_strategy=None):
        self.price = price
        self.discount_strategy = discount_strategy

    def price_after_discount(self):
        if self.discount_strategy:
            discount = self.discount_strategy(self)
        else:
            discount = 0
        return self.price - discount

    def __repr__(self):
        fmt = "<Price: {}, price after discount: {}>"
        return fmt.format(self.price, self.price_after_discount())


def ten_percent_discount(order):
    return order.price * 0.10


def on_sale_discount(order):
    return order.price * 0.25 + 20


def main():
    order0 = Order(100)
    order1 = Order(100, discount_strategy=ten_percent_discount)
    order2 = Order(1000, discount_strategy=on_sale_discount)
    print(order0)
    print(order1)
    print(order2)


if __name__ == "__main__":
    main()


OUTPUT = """
<Price: 100, price after discount: 100>
<Price: 100, price after discount: 90.0>
<Price: 1000, price after discount: 730.0>
"""
