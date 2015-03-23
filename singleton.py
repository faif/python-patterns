"""https://en.wikipedia.org/wiki/Singleton_pattern"""
"""In software engineering, the singleton pattern is a design pattern 
   that restricts the instantiation of a class to one object. This is 
   useful when exactly one object is needed to coordinate actions across 
   the system. The concept is sometimes generalized to systems that operate 
   more efficiently when only one object exists, or that restrict the 
   instantiation to a certain number of objects. The term comes from the 
   mathematical concept of a singleton."""


class C:
    instance = None
    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(C, cls).__new__(cls)
        return cls.instance

c = C()
b = C()
print(c is b)  # True