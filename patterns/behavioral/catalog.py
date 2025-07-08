"""
A class that uses different static function depending of a parameter passed in
init. Note the use of a single dictionary instead of multiple conditions
"""

__author__ = "Ibrahim Diop <ibrahim@sikilabs.com>"


class Catalog:
    """catalog of multiple static methods that are executed depending on an init

    parameter
    """

    def __init__(self, param: str) -> None:

        # dictionary that will be used to determine which static method is
        # to be executed but that will be also used to store possible param
        # value
        self._static_method_choices = {
            "param_value_1": self._static_method_1,
            "param_value_2": self._static_method_2,
        }

        # simple test to validate param value
        if param in self._static_method_choices.keys():
            self.param = param
        else:
            raise ValueError(f"Invalid Value for Param: {param}")

    @staticmethod
    def _static_method_1() -> None:
        print("executed method 1!")

    @staticmethod
    def _static_method_2() -> None:
        print("executed method 2!")

    def main_method(self) -> None:
        """will execute either _static_method_1 or _static_method_2

        depending on self.param value
        """
        self._static_method_choices[self.param]()


# Alternative implementation for different levels of methods
class CatalogInstance:
    """catalog of multiple methods that are executed depending on an init

    parameter
    """

    def __init__(self, param: str) -> None:
        self.x1 = "x1"
        self.x2 = "x2"
        # simple test to validate param value
        if param in self._instance_method_choices:
            self.param = param
        else:
            raise ValueError(f"Invalid Value for Param: {param}")

    def _instance_method_1(self) -> None:
        print(f"Value {self.x1}")

    def _instance_method_2(self) -> None:
        print(f"Value {self.x2}")

    _instance_method_choices = {
        "param_value_1": _instance_method_1,
        "param_value_2": _instance_method_2,
    }

    def main_method(self) -> None:
        """will execute either _instance_method_1 or _instance_method_2

        depending on self.param value
        """
        self._instance_method_choices[self.param].__get__(self)()  # type: ignore
        # type ignore reason: https://github.com/python/mypy/issues/10206


class CatalogClass:
    """catalog of multiple class methods that are executed depending on an init

    parameter
    """

    x1 = "x1"
    x2 = "x2"

    def __init__(self, param: str) -> None:
        # simple test to validate param value
        if param in self._class_method_choices:
            self.param = param
        else:
            raise ValueError(f"Invalid Value for Param: {param}")

    @classmethod
    def _class_method_1(cls) -> None:
        print(f"Value {cls.x1}")

    @classmethod
    def _class_method_2(cls) -> None:
        print(f"Value {cls.x2}")

    _class_method_choices = {
        "param_value_1": _class_method_1,
        "param_value_2": _class_method_2,
    }

    def main_method(self):
        """will execute either _class_method_1 or _class_method_2

        depending on self.param value
        """
        self._class_method_choices[self.param].__get__(None, self.__class__)()  # type: ignore
        # type ignore reason: https://github.com/python/mypy/issues/10206


class CatalogStatic:
    """catalog of multiple static methods that are executed depending on an init

    parameter
    """

    def __init__(self, param: str) -> None:
        # simple test to validate param value
        if param in self._static_method_choices:
            self.param = param
        else:
            raise ValueError(f"Invalid Value for Param: {param}")

    @staticmethod
    def _static_method_1() -> None:
        print("executed method 1!")

    @staticmethod
    def _static_method_2() -> None:
        print("executed method 2!")

    _static_method_choices = {
        "param_value_1": _static_method_1,
        "param_value_2": _static_method_2,
    }

    def main_method(self) -> None:
        """will execute either _static_method_1 or _static_method_2

        depending on self.param value
        """

        self._static_method_choices[self.param].__get__(None, self.__class__)()  # type: ignore
        # type ignore reason: https://github.com/python/mypy/issues/10206


def main():
    """
    >>> test = Catalog('param_value_2')
    >>> test.main_method()
    executed method 2!

    >>> test = CatalogInstance('param_value_1')
    >>> test.main_method()
    Value x1

    >>> test = CatalogClass('param_value_2')
    >>> test.main_method()
    Value x2

    >>> test = CatalogStatic('param_value_1')
    >>> test.main_method()
    executed method 1!
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
