#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Gordeev Andrey <gordeev.and.and@gmail.com>

*TL;DR80
Provides recombination business logic by chaining together using boolean logic.
"""

from abc import abstractmethod


class Specification(object):
    def and_specification(self, candidate):
        raise NotImplementedError()

    def or_specification(self, candidate):
        raise NotImplementedError()

    def not_specification(self):
        raise NotImplementedError()

    @abstractmethod
    def is_satisfied_by(self, candidate):
        pass


class CompositeSpecification(Specification):
    @abstractmethod
    def is_satisfied_by(self, candidate):
        pass

    def and_specification(self, candidate):
        return AndSpecification(self, candidate)

    def or_specification(self, candidate):
        return OrSpecification(self, candidate)

    def not_specification(self):
        return NotSpecification(self)


class AndSpecification(CompositeSpecification):
    _one = Specification()
    _other = Specification()

    def __init__(self, one, other):
        self._one = one
        self._other = other

    def is_satisfied_by(self, candidate):
        return bool(self._one.is_satisfied_by(candidate) and self._other.is_satisfied_by(candidate))


class OrSpecification(CompositeSpecification):
    _one = Specification()
    _other = Specification()

    def __init__(self, one, other):
        self._one = one
        self._other = other

    def is_satisfied_by(self, candidate):
        return bool(self._one.is_satisfied_by(candidate) or self._other.is_satisfied_by(candidate))


class NotSpecification(CompositeSpecification):
    _wrapped = Specification()

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def is_satisfied_by(self, candidate):
        return bool(not self._wrapped.is_satisfied_by(candidate))


class User(object):
    def __init__(self, super_user=False):
        self.super_user = super_user


class UserSpecification(CompositeSpecification):
    def is_satisfied_by(self, candidate):
        return isinstance(candidate, User)


class SuperUserSpecification(CompositeSpecification):
    def is_satisfied_by(self, candidate):
        return getattr(candidate, 'super_user', False)


def main():
    print('Specification')
    andrey = User()
    ivan = User(super_user=True)
    vasiliy = 'not User instance'

    root_specification = UserSpecification().and_specification(SuperUserSpecification())

    print(root_specification.is_satisfied_by(andrey))
    print(root_specification.is_satisfied_by(ivan))
    print(root_specification.is_satisfied_by(vasiliy))


if __name__ == '__main__':
    main()


OUTPUT = """
Specification
False
True
False
"""
