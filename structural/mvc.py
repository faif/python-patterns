#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*TL;DR80
Separates data in GUIs from the ways it is presented, and accepted.
"""
from abc import ABC, abstractmethod


class Model(ABC):
    """Abstract model defines interfaces."""

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def get(self, item):
        """Returns an object with a .items() call method
        that iterates over key,value pairs of its information."""
        pass

    @abstractmethod
    def item_type(self):
        pass


class View(ABC):
    """Abstract view defines interfaces."""

    @abstractmethod
    def show_item_list(self, item_type, item_list):
        pass

    @abstractmethod
    def show_item_information(self, item_type, item_name, item_info):
        """Will look for item information by iterating over key,value pairs
        yielded by item_info.items()"""
        pass

    @abstractmethod
    def item_not_found(self, item_type, item_name):
        pass


class Controller(ABC):
    """Abstract controller defines interfaces."""

    @abstractmethod
    def show_items(self):
        pass

    @abstractmethod
    def show_item_information(self, item_name):
        pass


class ProductModel(Model):
    """Concrete product model."""

    class Price(float):
        """A polymorphic way to pass a float with a particular
        __str__ functionality."""

        def __str__(self):
            first_digits_str = str(round(self, 2))
            try:
                dot_location = first_digits_str.index('.')
            except ValueError:
                return '{}.00'.format(first_digits_str)
            return '{}{}'.format(first_digits_str, '0' * (3 + dot_location - len(first_digits_str)))

    products = {
        'milk': {'price': Price(1.50), 'quantity': 10},
        'eggs': {'price': Price(0.20), 'quantity': 100},
        'cheese': {'price': Price(2.00), 'quantity': 10}
    }

    @property
    def item_type(self):
        return 'product'

    def __iter__(self):
        for item in self.products:
            yield item

    def get(self, product):
        try:
            return self.products[product]
        except KeyError as e:
            raise KeyError(str(e) + " not in the model's item list.")



class ConsoleView(View):
    """Concrete console view."""

    def show_item_list(self, item_type, item_list):
        print("{} LIST:".format(item_type.upper()))
        for item in item_list:
            print(item)
        print('\n')

    @staticmethod
    def capitalizer(string):
        return '{}{}'.format(string[0].upper(), string[1:].lower())

    def show_item_information(self, item_type, item_name, item_info):
        print('{} INFORMATION:'.format(item_type.upper()))
        printout = 'Name: {}'.format(item_name)
        for key, value in item_info.items():
            printout += ', ' + self.capitalizer(str(key)) + ': ' + str(value)
        printout += '\n'
        print(printout)

    def item_not_found(self, item_type, item_name):
        print('That {} "{}" does not exist in the records'.format(item_type, item_name))


class ItemController(Controller):
    """Concrete item controller."""

    def __init__(self, model, view):
        self._model = model
        self._view = view

    def show_items(self):
        items = list(self._model)
        item_type = self._model.item_type
        self._view.show_item_list(item_type, items)

    def show_item_information(self, item_name):
        try:
            item_info = self._model.get(item_name)
        except KeyError:
            item_type = self._model.item_type
            self._view.item_not_found(item_type, item_name)
        else:
            item_type = self._model.item_type
            self._view.show_item_information(item_type, item_name, item_info)


if __name__ == '__main__':
    model = ProductModel()
    view = ConsoleView()
    controller = ItemController(model, view)
    controller.show_items()
    controller.show_item_information('cheese')
    controller.show_item_information('eggs')
    controller.show_item_information('milk')
    controller.show_item_information('arepas')


### OUTPUT ###
# PRODUCT LIST:
# cheese
# eggs
# milk
#
# PRODUCT INFORMATION:
# Name: Cheese, Price: 2.00, Quantity: 10
#
# PRODUCT INFORMATION:
# Name: Eggs, Price: 0.20, Quantity: 100
#
# PRODUCT INFORMATION:
# Name: Milk, Price: 1.50, Quantity: 10
#
# That product "arepas" does not exist in the records