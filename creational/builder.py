#!/usr/bin/python
# -*- coding : utf-8 -*-

"""
*What is this pattern about?
It decouples the creation of a complex object and its representation,
so that the same process can be reused to build objects from the same
family.
This is useful when you must separate the specification of an object
from its actual representation (generally for abstraction).

*What does this example do?
This particular example uses a Director to abtract the
construction of a building. The user specifies a Builder (House or
Flat) and the director specifies the methods in the order necessary
creating a different building dependding on the sepcified
specification (through the Builder class).

@author: Diogenes Augusto Fernandes Herminio <diofeher@gmail.com>
https://gist.github.com/420905#file_builder_python.py

*Where is the pattern used practically?

*References:
https://sourcemaking.com/design_patterns/builder

"""


# Director
class Director(object):

    def __init__(self):
        self.builder = None

    def construct_building(self):
        self.builder.new_building()
        self.builder.build_floor()
        self.builder.build_size()

    def get_building(self):
        return self.builder.building


# Abstract Builder
class Builder(object):

    def __init__(self):
        self.building = None

    def new_building(self):
        self.building = Building()

    def build_floor(self):
        raise NotImplementedError

    def build_size(self):
        raise NotImplementedError

# Concrete Builder


class BuilderHouse(Builder):

    def build_floor(self):
        self.building.floor = 'One'

    def build_size(self):
        self.building.size = 'Big'


class BuilderFlat(Builder):

    def build_floor(self):
        self.building.floor = 'More than One'

    def build_size(self):
        self.building.size = 'Small'


# Product
class Building(object):

    def __init__(self):
        self.floor = None
        self.size = None

    def __repr__(self):
        return 'Floor: {0.floor} | Size: {0.size}'.format(self)


# Client
if __name__ == "__main__":
    director = Director()
    director.builder = BuilderHouse()
    director.construct_building()
    building = director.get_building()
    print(building)
    director.builder = BuilderFlat()
    director.construct_building()
    building = director.get_building()
    print(building)

### OUTPUT ###
# Floor: One | Size: Big
# Floor: More than One | Size: Small
