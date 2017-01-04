#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Eugene Duboviy <eugene.dubovoy@gmail.com> | github.com/duboviy

In Blackboard pattern several specialised sub-systems (knowledge sources)
assemble their knowledge to build a possibly partial or approximate solution.
In this way, the sub-systems work together to solve the problem,
where the solution is the sum of its parts.

https://en.wikipedia.org/wiki/Blackboard_system
"""

import abc
import random


class Blackboard(object):

    def __init__(self):
        self.experts = []
        self.common_state = {
            'problems': 0,
            'suggestions': 0,
            'contributions': [],
            'progress': 0   # percentage, if 100 -> task is finished
        }

    def add_expert(self, expert):
        self.experts.append(expert)


class Controller(object):

    def __init__(self, blackboard):
        self.blackboard = blackboard

    def run_loop(self):
        while self.blackboard.common_state['progress'] < 100:
            for expert in self.blackboard.experts:
                if expert.is_eager_to_contribute:
                    expert.contribute()
        return self.blackboard.common_state['contributions']


class AbstractExpert(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, blackboard):
        self.blackboard = blackboard

    @abc.abstractproperty
    def is_eager_to_contribute(self):
        raise NotImplementedError('Must provide implementation in subclass.')

    @abc.abstractmethod
    def contribute(self):
        raise NotImplementedError('Must provide implementation in subclass.')


class Student(AbstractExpert):

    @property
    def is_eager_to_contribute(self):
        return True

    def contribute(self):
        self.blackboard.common_state['problems'] += random.randint(1, 10)
        self.blackboard.common_state['suggestions'] += random.randint(1, 10)
        self.blackboard.common_state['contributions'] += [self.__class__.__name__]
        self.blackboard.common_state['progress'] += random.randint(1, 2)


class Scientist(AbstractExpert):

    @property
    def is_eager_to_contribute(self):
        return random.randint(0, 1)

    def contribute(self):
        self.blackboard.common_state['problems'] += random.randint(10, 20)
        self.blackboard.common_state['suggestions'] += random.randint(10, 20)
        self.blackboard.common_state['contributions'] += [self.__class__.__name__]
        self.blackboard.common_state['progress'] += random.randint(10, 30)


class Professor(AbstractExpert):

    @property
    def is_eager_to_contribute(self):
        return True if self.blackboard.common_state['problems'] > 100 else False

    def contribute(self):
        self.blackboard.common_state['problems'] += random.randint(1, 2)
        self.blackboard.common_state['suggestions'] += random.randint(10, 20)
        self.blackboard.common_state['contributions'] += [self.__class__.__name__]
        self.blackboard.common_state['progress'] += random.randint(10, 100)


if __name__ == '__main__':
    blackboard = Blackboard()

    blackboard.add_expert(Student(blackboard))
    blackboard.add_expert(Scientist(blackboard))
    blackboard.add_expert(Professor(blackboard))

    c = Controller(blackboard)
    contributions = c.run_loop()

    from pprint import pprint
    pprint(contributions)

### OUTPUT ###
# ['Student',
#  'Student',
#  'Scientist',
#  'Student',
#  'Scientist',
#  'Student',
#  'Scientist',
#  'Student',
#  'Scientist',
#  'Student',
#  'Scientist',
#  'Professor']
