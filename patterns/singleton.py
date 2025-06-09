"""
Singleton Pattern Example
Ensures a class has only one instance and provides a global point of access to it.
"""

class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

if __name__ == "__main__":
    obj1 = Singleton()
    obj2 = Singleton()
    print("Are obj1 and obj2 the same?", obj1 is obj2)