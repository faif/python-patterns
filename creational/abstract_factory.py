#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*What is this pattern about?
The Abstract Factory Pattern serves to provide an interface for
creating related/dependent objects without need to specify their
actual class.
The idea is to abstract the creation of objects depending on business
logic, platform choice, etc.

*What does this example do?
This particular implementation abstracts the creation of a pet and
does so depending on the AnimalFactory we chose (Dog or Cat)
This works because both Dog/Cat and their factories respect a common
interface (.speak(), get_pet() and get_food()).
Now my application can create pets (and feed them) abstractly and decide later,
based on my own criteria, dogs over cats.
The second example allows us to create pets based on the string passed by the
user, using cls.__subclasses__ (the list of sub classes for class cls)
and  sub_cls.__name__ to get its name.

*Where is the pattern used practically?

*References:
https://sourcemaking.com/design_patterns/abstract_factory
http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/

*TL;DR80
Provides a way to encapsulate a group of individual factories.
"""


import six
import abc
import random


class PetShop(object):

    """A pet shop"""

    def __init__(self, animal_factory=None):
        """pet_factory is our abstract factory.  We can set it at will."""

        self.pet_factory = animal_factory

    def show_pet(self):
        """Creates and shows a pet using the abstract factory"""

        pet = self.pet_factory.get_pet()
        print("We have a lovely {}".format(pet))
        print("It says {}".format(pet.speak()))
        print("We also have {}".format(self.pet_factory.get_food()))


# Stuff that our factory makes

class Dog(object):

    def speak(self):
        return "woof"

    def __str__(self):
        return "Dog"


class Cat(object):

    def speak(self):
        return "meow"

    def __str__(self):
        return "Cat"


# Factory classes

class DogFactory(object):

    def get_pet(self):
        return Dog()

    def get_food(self):
        return "dog food"


class CatFactory(object):

    def get_pet(self):
        return Cat()

    def get_food(self):
        return "cat food"


# Create the proper family
def get_factory():
    """Let's be dynamic!"""
    return random.choice([DogFactory, CatFactory])()


# Implementation 2 of an abstract factory
@six.add_metaclass(abc.ABCMeta)
class Pet(object):

    @classmethod
    def from_name(cls, name):
        for sub_cls in cls.__subclasses__():
            if name == sub_cls.__name__.lower():
                return sub_cls()

    @abc.abstractmethod
    def speak(self):
        """"""


class Kitty(Pet):
    def speak(self):
        return "Miao"


class Duck(Pet):
    def speak(self):
        return "Quak"


# Show pets with various factories
if __name__ == "__main__":
    for i in range(3):
        shop = PetShop(get_factory())
        shop.show_pet()
        print("=" * 20)

    for name0 in ["kitty", "duck"]:
        pet = Pet.from_name(name0)
        print("{}: {}".format(name0, pet.speak()))

### OUTPUT ###
# We have a lovely Cat
# It says meow
# We also have cat food
# ====================
# We have a lovely Dog
# It says woof
# We also have dog food
# ====================
# We have a lovely Cat
# It says meow
# We also have cat food
# ====================
# kitty: Miao
# duck: Quak
