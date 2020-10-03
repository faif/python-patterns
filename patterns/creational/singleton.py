"""*What is this pattern about?
A Singleton is an object for restricting the instantiation of a class to one "single" instance.

*What does this example do?
the code shows how to create the singleton class which is sun and use it .

*Where can the pattern be used practically?
is pattern is commonly implemented in features that require control over access to a shared resource such as a database
connection or a file. By ensuring that a class can only be used to create a single instance and providing a single
global access point, access to the shared resource can be restricted and integrity can be maintained.

"""


class Sun(object):
    """ this class is used to access sun data and methods as singleton """

    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            # If __instance has no value, assign a value to the __instance variable
            cls.__instance = object.__new__(cls)

            return cls.__instance
        else:
            # If __instance has a value, return directly.
            return cls.__instance


if __name__ == "__main__":
    # sun and sun1 have the same id value
    sun = Sun()
    print(id(sun))
    sun1=Sun()
    print(id(sun1))


OUTPUT = """
139919126109152
139919126109152
"""  # noqa
