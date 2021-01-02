"""
*TL;DR
Separates data in GUIs from the ways it is presented, and accepted.
"""

from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def get(self, item):
        """Returns an object with a .items() call method
        that iterates over key,value pairs of its information."""
        pass

    @property
    @abstractmethod
    def item_type(self):
        pass


class ProductModel(Model):
    class Price(float):
        """A polymorphic way to pass a float with a particular
        __str__ functionality."""

        def __str__(self):
            return f"{self:.2f}"

    products = {
        "milk": {"price": Price(1.50), "quantity": 10},
        "eggs": {"price": Price(0.20), "quantity": 100},
        "cheese": {"price": Price(2.00), "quantity": 10},
    }

    item_type = "product"

    def __iter__(self):
        yield from self.products

    def get(self, product):
        try:
            return self.products[product]
        except KeyError as e:
            raise KeyError(str(e) + " not in the model's item list.")


class View(ABC):
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


class ConsoleView(View):
    def show_item_list(self, item_type, item_list):
        print(item_type.upper() + " LIST:")
        for item in item_list:
            print(item)
        print("")

    @staticmethod
    def capitalizer(string):
        return string[0].upper() + string[1:].lower()

    def show_item_information(self, item_type, item_name, item_info):
        print(item_type.upper() + " INFORMATION:")
        printout = "Name: %s" % item_name
        for key, value in item_info.items():
            printout += ", " + self.capitalizer(str(key)) + ": " + str(value)
        printout += "\n"
        print(printout)

    def item_not_found(self, item_type, item_name):
        print(f'That {item_type} "{item_name}" does not exist in the records')


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_items(self):
        items = list(self.model)
        item_type = self.model.item_type
        self.view.show_item_list(item_type, items)

    def show_item_information(self, item_name):
        try:
            item_info = self.model.get(item_name)
        except Exception:
            item_type = self.model.item_type
            self.view.item_not_found(item_type, item_name)
        else:
            item_type = self.model.item_type
            self.view.show_item_information(item_type, item_name, item_info)


def main():
    """
    >>> model = ProductModel()
    >>> view = ConsoleView()
    >>> controller = Controller(model, view)

    >>> controller.show_items()
    PRODUCT LIST:
    milk
    eggs
    cheese
    <BLANKLINE>

    >>> controller.show_item_information("cheese")
    PRODUCT INFORMATION:
    Name: cheese, Price: 2.00, Quantity: 10
    <BLANKLINE>

    >>> controller.show_item_information("eggs")
    PRODUCT INFORMATION:
    Name: eggs, Price: 0.20, Quantity: 100
    <BLANKLINE>

    >>> controller.show_item_information("milk")
    PRODUCT INFORMATION:
    Name: milk, Price: 1.50, Quantity: 10
    <BLANKLINE>

    >>> controller.show_item_information("arepas")
    That product "arepas" does not exist in the records
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
