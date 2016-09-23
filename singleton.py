#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Singleton(object):
    """
    Assume that only one instance should be created of this class and
    it is counting the users connected to the system.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        For each class, creating only one instance.
        If an instance has been created before, returns the created one.
        """
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)

            # your init codes here
            cls.user_count = 0
            # end of your init code

        return cls._instance

    def connect(self):
        self.user_count += 1

    def disconnect(self):
        self.user_count -= 1


if __name__ == '__main__':

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print "Same instances"
    else:
        print "Different instances"

    s1.connect()  # user count: 1
    s1.connect()  # user count: 2
    s2.connect()  # same instance with s1, so user count: 3 for s1 and s2
    s1.disconnect()  # same instance with s2, so user count: 2 for s1 and s2

    print s1.user_count
    print s2.user_count
