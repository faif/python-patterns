#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Person(object):

    def __init__(self, name, action):
        self.name = name
        self.action = action

    def do_action(self):
        print(self.name, self.action.name, end=' ')
        return self.action

class Action(object):

    def __init__(self, name):
        self.name = name

    def amount(self, val):
        print(val, end=' ')
        return self

    def stop(self):
        print('then stop')

if __name__ == '__main__':

    move = Action('move')
    person = Person('Jack', move)
    person.do_action().amount('5m').stop()

### OUTPUT ###
# Jack move 5m then stop
