"""https://en.wikipedia.org/wiki/Decorator_pattern"""
"""In object-oriented programming, the decorator pattern (also known as Wrapper, 
   an alternative naming shared with the Adapter pattern) is a design pattern that 
   allows behavior to be added to an individual object, either statically or dynamically, 
   without affecting the behavior of other objects from the same class."""
"""Despite the name, Python decorators are not an implementation of the decorator pattern. 
   The decorator pattern is a design pattern used in statically typed object-oriented 
   programming languages to allow functionality to be added to objects at run time; 
   Python decorators add functionality to functions and methods at definition time, 
   and thus are a higher-level construct than decorator-pattern classes. The decorator 
   pattern itself is trivially implementable in Python, because the language is duck typed, 
   and so is not usually considered as such."""

from abc import ABCMeta, abstractmethod
 
class IOperator(metaclass=ABCMeta):
 
    @abstractmethod
    def operator(self):
        pass
 
 
class Component(IOperator):
    """Base component"""
    def operator(self):
        return 10.0
 
 
class Wrapper(IOperator):
    """Decorator"""
    def __init__(self, obj):
        self.obj = obj
 
    def operator(self):
        return self.obj.operator() + 5.0
 
 
comp = Component()
comp = Wrapper(comp)
print(comp.operator())  # 15.0
