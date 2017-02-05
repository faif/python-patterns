#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A class that uses different static function depending of a parameter passed in
init. Note the use of a single dictionary instead of multiple conditions
"""
__author__ = "Ibrahim Diop <http://ibrahim.zinaria.com>"
__gist__ = "<https://gist.github.com/diopib/7679559>"


class Catalog(object):
    """catalog of multiple static methods that are executed depending on an init

    parameter
    """

    def __init__(self, param):

        # dictionary that will be used to determine which static method is
        # to be executed but that will be also used to store possible param
        # value
        self._static_method_choices = {'param_value_1': self._static_method_1,
                                       'param_value_2': self._static_method_2}

        # simple test to validate param value
        if param in self._static_method_choices.keys():
            self.param = param
        else:
            raise ValueError("Invalid Value for Param: {0}".format(param))

    @staticmethod
    def _static_method_1():
        print("executed method 1!")

    @staticmethod
    def _static_method_2():
        print("executed method 2!")

    def main_method(self):
        """will execute either _static_method_1 or _static_method_2

        depending on self.param value
        """
        self._static_method_choices[self.param]()


# Alternative implementation for different levels of methods
class CatalogInstance(object):

    """catalog of multiple methods that are executed depending on an init

    parameter
    """

    def __init__(self, param):
        self.x1 = 'x1'
        self.x2 = 'x2'
        # simple test to validate param value
        if param in self._instance_method_choices:
            self.param = param
        else:
            raise ValueError("Invalid Value for Param: {0}".format(param))

    def _instance_method_1(self):
        print("Value {}".format(self.x1))

    def _instance_method_2(self):
        print("Value {}".format(self.x2))

    _instance_method_choices = {'param_value_1': _instance_method_1,
                                'param_value_2': _instance_method_2}

    def main_method(self):
        """will execute either _instance_method_1 or _instance_method_2

        depending on self.param value
        """
        self._instance_method_choices[self.param].__get__(self)()


class CatalogClass(object):

    """catalog of multiple class methods that are executed depending on an init

    parameter
    """

    x1 = 'x1'
    x2 = 'x2'

    def __init__(self, param):
        # simple test to validate param value
        if param in self._class_method_choices:
            self.param = param
        else:
            raise ValueError("Invalid Value for Param: {0}".format(param))

    @classmethod
    def _class_method_1(cls):
        print("Value {}".format(cls.x1))

    @classmethod
    def _class_method_2(cls):
        print("Value {}".format(cls.x2))

    _class_method_choices = {'param_value_1': _class_method_1,
                             'param_value_2': _class_method_2}

    def main_method(self):
        """will execute either _class_method_1 or _class_method_2

        depending on self.param value
        """
        self._class_method_choices[self.param].__get__(None, self.__class__)()


class CatalogStatic(object):

    """catalog of multiple static methods that are executed depending on an init

    parameter
    """

    def __init__(self, param):
        # simple test to validate param value
        if param in self._static_method_choices:
            self.param = param
        else:
            raise ValueError("Invalid Value for Param: {0}".format(param))

    @staticmethod
    def _static_method_1():
        print("executed method 1!")

    @staticmethod
    def _static_method_2():
        print("executed method 2!")

    _static_method_choices = {'param_value_1': _static_method_1,
                              'param_value_2': _static_method_2}

    def main_method(self):
        """will execute either _static_method_1 or _static_method_2

        depending on self.param value
        """
        self._static_method_choices[self.param].__get__(None, self.__class__)()


def main():
    """
    >>> c = Catalog('param_value_1').main_method()
    executed method 1!
    >>> Catalog('param_value_2').main_method()
    executed method 2!
    """

    test = Catalog('param_value_2')
    test.main_method()

    test = CatalogInstance('param_value_1')
    test.main_method()

    test = CatalogClass('param_value_2')
    test.main_method()

    test = CatalogStatic('param_value_1')
    test.main_method()

if __name__ == "__main__":
    main()

### OUTPUT ###
# executed method 2!
# Value x1
# Value x2
# executed method 1!
