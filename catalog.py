"""
A class that uses different static function depending of a parameter passed in init
Note the use of a single dictionnary instead of multiple conditions
"""
__author__ = "Ibrahim Diop <http://ibrahim.zinaria.com>"
__gist__ = "<https://gist.github.com/diopib/7679559>"

class Catalog():
    """
    catalog of multiple static methods that are executed depending on an init parameter
    """

    def __init__(self, param):

        # dictionary that will be used to determine which static method is to be executed but
        # that will be also used to store possible param value
        self.static_method_choices = {'param_value_1': self.static_method_1, 'param_value_2': self.static_method_2}

        # simple test to validate param value
        if param in self.static_method_choices.keys():
            self.param = param
        else:
            raise Exception("Invalid Value for Param: {0}".format(param))

    @staticmethod
    def static_method_1():
        print("executed method 1!")

    @staticmethod
    def static_method_2():
        print("executed method 2!")

    def main_method(self):
        """
        will execute either static_method_1 or static_method_2
        depending on self.param value
        """
        self.static_method_choices[self.param]()


def main():
    """
    >>> c = Catalog('param_value_1').main_method()
    executed method 1!
    >>> Catalog('param_value_2').main_method()
    executed method 2!
    """

    test = Catalog('param_value_2')
    test.main_method()

if __name__ == "__main__":
    main()
