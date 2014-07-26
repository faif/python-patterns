#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Singleton(type):
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance

class MyClass(object):
    __metaclass__ = Singleton

# Test
if __name__ == '__main__':
    one = MyClass()
    two = MyClass()
    two.a = 123
    print(one.a)

    print('>>> one\'s id: ', id(one))
    print('>>> two\'s id: ', id(two))
    if one is two:
        print('Singletion implementation...')

### OUTPUT ###
# 123
# (">>> one's id: ", 140700252715024)
# (">>> two's id: ", 140700252715024)
# Singletion implementation...
