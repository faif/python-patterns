"""
*TL;DR
Separates presentation, application processing, and data management functions.
"""

from typing import Dict, KeysView, Optional, Type, TypeVar, Union

T = TypeVar("T")


class Data:
    """ Data Store Class """

    products = {
        "milk": {"price": 1.50, "quantity": 10},
        "eggs": {"price": 0.20, "quantity": 100},
        "cheese": {"price": 2.00, "quantity": 10},
    }

    def __get__(
        self, obj: Optional[T], klas: Type[T]
    ) -> Dict[str, Dict[str, Dict[str, Union[int, float]]]]:

        print("(Fetching from Data Store)")
        return {"products": self.products}


class BusinessLogic:
    """ Business logic holding data store instances """

    data = Data()

    def product_list(self) -> KeysView[str]:
        return self.data["products"].keys()

    def product_information(
        self, product: str
    ) -> Optional[Dict[str, Union[int, float]]]:
        return self.data["products"].get(product, None)


class Ui:
    """ UI interaction class """

    def __init__(self) -> None:
        self.business_logic = BusinessLogic()

    def get_product_list(self) -> None:
        print("PRODUCT LIST:")
        for product in self.business_logic.product_list():
            print(product)
        print("")

    def get_product_information(self, product: str) -> None:
        product_info = self.business_logic.product_information(product)
        if product_info:
            print("PRODUCT INFORMATION:")
            print(
                f"Name: {product.title()}, "
                + f"Price: {product_info.get('price', 0):.2f}, "
                + f"Quantity: {product_info.get('quantity', 0):}"
            )
        else:
            print(f"That product '{product}' does not exist in the records")


def main():
    ui = Ui()
    ui.get_product_list()
    ui.get_product_information("cheese")
    ui.get_product_information("eggs")
    ui.get_product_information("milk")
    ui.get_product_information("arepas")


if __name__ == "__main__":
    main()

### OUTPUT ###
# PRODUCT LIST:
# (Fetching from Data Store)
# cheese
# eggs
# milk
#
# (Fetching from Data Store)
# PRODUCT INFORMATION:
# Name: Cheese, Price: 2.00, Quantity: 10
# (Fetching from Data Store)
# PRODUCT INFORMATION:
# Name: Eggs, Price: 0.20, Quantity: 100
# (Fetching from Data Store)
# PRODUCT INFORMATION:
# Name: Milk, Price: 1.50, Quantity: 10
# (Fetching from Data Store)
# That product "arepas" does not exist in the records
