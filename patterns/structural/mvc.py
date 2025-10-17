"""
*TL;DR
Separates data in GUIs from the ways it is presented, and accepted.
"""

from abc import ABC, abstractmethod
from ProductModel import Price
from typing import Dict, List, Union, Any
from inspect import signature
from sys import argv


class Model(ABC):
    """The Model is the data layer of the application."""

    @abstractmethod
    def __iter__(self) -> Any:
        pass

    @abstractmethod
    def get(self, item: str) -> dict:
        """Returns an object with a .items() call method
        that iterates over key,value pairs of its information."""
        pass

    @property
    @abstractmethod
    def item_type(self) -> str:
        pass


class ProductModel(Model):
    """The Model is the data layer of the application."""

    class Price(float):
        """A polymorphic way to pass a float with a particular
        __str__ functionality."""

        def __str__(self) -> str:
            return f"{self:.2f}"

    products = {
        "milk": {"price": Price(1.50), "quantity": 10},
        "eggs": {"price": Price(0.20), "quantity": 100},
        "cheese": {"price": Price(2.00), "quantity": 10},
    }

    item_type = "product"

    def __iter__(self) -> Any:
        yield from self.products

    def get(self, product: str) -> dict:
        try:
            return self.products[product]
        except KeyError as e:
            raise KeyError(str(e) + " not in the model's item list.")


class View(ABC):
    """The View is the presentation layer of the application."""

    @abstractmethod
    def show_item_list(self, item_type: str, item_list: list) -> None:
        pass

    @abstractmethod
    def show_item_information(
        self, item_type: str, item_name: str, item_info: dict
    ) -> None:
        """Will look for item information by iterating over key,value pairs
        yielded by item_info.items()"""
        pass

    @abstractmethod
    def item_not_found(self, item_type: str, item_name: str) -> None:
        pass


class ConsoleView(View):
    """The View is the presentation layer of the application."""

    def show_item_list(self, item_type: str, item_list: list) -> None:
        print(item_type.upper() + " LIST:")
        for item in item_list:
            print(item)
        print("")

    @staticmethod
    def capitalizer(string: str) -> str:
        """Capitalizes the first letter of a string and lowercases the rest."""
        return string[0].upper() + string[1:].lower()

    def show_item_information(
        self, item_type: str, item_name: str, item_info: dict
    ) -> None:
        """Will look for item information by iterating over key,value pairs"""
        print(item_type.upper() + " INFORMATION:")
        printout = "Name: %s" % item_name
        for key, value in item_info.items():
            printout += ", " + self.capitalizer(str(key)) + ": " + str(value)
        printout += "\n"
        print(printout)

    def item_not_found(self, item_type: str, item_name: str) -> None:
        print(f'That {item_type} "{item_name}" does not exist in the records')


class Controller:
    """The Controller is the intermediary between the Model and the View."""

    def __init__(self, model_class: Model, view_class: View) -> None:
        self.model: Model = model_class
        self.view: View = view_class

    def show_items(self) -> None:
        items = list(self.model)
        item_type = self.model.item_type
        self.view.show_item_list(item_type, items)

    def show_item_information(self, item_name: str) -> None:
        """
        Show information about a {item_type} item.
        :param str item_name: the name of the {item_type} item to show information about
        """
        item_type: str = self.model.item_type
        try:
            item_info: dict = self.model.get(item_name)
        except Exception:
            self.view.item_not_found(item_type, item_name)
        else:
            self.view.show_item_information(item_type, item_name, item_info)


class Router:
    """The Router is the entry point of the application."""

    def __init__(self):
        self.routes = {}

    def register(
        self,
        path: str,
        controller_class: type[Controller],
        model_class: type[Model],
        view_class: type[View],
    ) -> None:
        model_instance: Model = model_class()
        view_instance: View = view_class()
        self.routes[path] = controller_class(model_instance, view_instance)

    def resolve(self, path: str) -> Controller:
        if self.routes.get(path):
            controller: Controller = self.routes[path]
            return controller
        else:
            raise KeyError(f"No controller registered for path '{path}'")


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
    router = Router()
    router.register("products", Controller, ProductModel, ConsoleView)
    controller: Controller = router.resolve(argv[1])

    action: str = str(argv[2]) if len(argv) > 2 else ""
    args: str = " ".join(map(str, argv[3:])) if len(argv) > 3 else ""

    if hasattr(controller, action):
        command = getattr(controller, action)
        sig = signature(command)

        if len(sig.parameters) > 0:
            if args:
                command(args)
            else:
                print("Command requires arguments.")
        else:
            command()
    else:
        print(f"Command {action} not found in the controller.")

    import doctest

    doctest.testmod()
