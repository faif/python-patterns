#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*What is this pattern about?
This patterns aims to reduce the number of classes required by an
application. Instead of relying on subclasses it creates objects by
copying a prototypical instance at run-time.

This is useful as it make it easier to derive new kinds of objects,
when instances of the class have only a few different combinations of
state, and when instantiation is expensive.

*What does this example do?
When the number of prototypes in an application can vary, it can be
useful to keep a Dispatcher (aka, Registry or Manager). This allows
clients to query the Dispatcher for a prototype before cloning a new
instance.

Below provides an example of such Dispatcher, which contains three
copies of the prototype: 'default', 'objecta' and 'objectb'.

*TL;DR80
Creates new object instances by cloning prototype.
"""


class Prototype(object):

    value = 'default'

    def clone(self, **attrs):
        """Clone a prototype and update inner attributes dictionary"""
        # Python in Practice, Mark Summerfield
        obj = self.__class__()
        obj.__dict__.update(attrs)
        return obj


class PrototypeDispatcher(object):
    def __init__(self):
        self._objects = {}

    def get_objects(self):
        """Get all objects"""
        return self._objects

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]


def main():
    dispatcher = PrototypeDispatcher()
    prototype = Prototype()

    d = prototype.clone()
    a = prototype.clone(value='a-value', category='a')
    b = prototype.clone(value='b-value', is_checked=True)
    dispatcher.register_object('objecta', a)
    dispatcher.register_object('objectb', b)
    dispatcher.register_object('default', d)
    print([{n: p.value} for n, p in dispatcher.get_objects().items()])


if __name__ == '__main__':
    main()

### OUTPUT ###
# [{'objectb': 'b-value'}, {'default': 'default'}, {'objecta': 'a-value'}]
