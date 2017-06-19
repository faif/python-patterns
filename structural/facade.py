#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*What is this pattern about?
The Facade pattern is a way to provide a simpler unified interface to
a more complex system. It provides an easier way to access functions
of the underlying system by providing a single entry point.
This kind of abstraction is seen in many real life situations. For
example, we can turn on a computer by just pressing a button, but in
fact there are many procedures and operations done when that happens
(e.g., loading programs from disk to memory). In this case, the button
serves as an unified interface to all the underlying procedures to
turn on a computer.

*What does this example do?
The code defines three classes (TC1, TC2, TC3) that represent complex
parts to be tested. Instead of testing each class separately, the
TestRunner class acts as the facade to run all tests with only one
call to the method runAll. By doing that, the client part only needs
to instantiate the class TestRunner and call the runAll method.
As seen in the example, the interface provided by the Facade pattern
is independent from the underlying implementation. Since the client
just calls the runAll method, we can modify the classes TC1, TC2 or
TC3 without impact on the way the client uses the system.

*Where is the pattern used practically?
This pattern can be seen in the Python standard library when we use
the isdir function. Although a user simply uses this function to know
whether a path refers to a directory, the system makes a few
operations and calls other modules (e.g., os.stat) to give the result.

*References:
https://sourcemaking.com/design_patterns/facade
https://fkromer.github.io/python-pattern-references/design/#facade
http://python-3-patterns-idioms-test.readthedocs.io/en/latest/ChangeInterface.html#facade
"""


from __future__ import print_function
import time

SLEEP = 0.1


# Complex Parts
class TC1:

    def run(self):
        print(u"###### In Test 1 ######")
        time.sleep(SLEEP)
        print(u"Setting up")
        time.sleep(SLEEP)
        print(u"Running test")
        time.sleep(SLEEP)
        print(u"Tearing down")
        time.sleep(SLEEP)
        print(u"Test Finished\n")


class TC2:

    def run(self):
        print(u"###### In Test 2 ######")
        time.sleep(SLEEP)
        print(u"Setting up")
        time.sleep(SLEEP)
        print(u"Running test")
        time.sleep(SLEEP)
        print(u"Tearing down")
        time.sleep(SLEEP)
        print(u"Test Finished\n")


class TC3:

    def run(self):
        print(u"###### In Test 3 ######")
        time.sleep(SLEEP)
        print(u"Setting up")
        time.sleep(SLEEP)
        print(u"Running test")
        time.sleep(SLEEP)
        print(u"Tearing down")
        time.sleep(SLEEP)
        print(u"Test Finished\n")


# Facade
class TestRunner:

    def __init__(self):
        self.tc1 = TC1()
        self.tc2 = TC2()
        self.tc3 = TC3()
        self.tests = [self.tc1, self.tc2, self.tc3]

    def runAll(self):
        [i.run() for i in self.tests]


# Client
if __name__ == '__main__':
    testrunner = TestRunner()
    testrunner.runAll()

### OUTPUT ###
# ###### In Test 1 ######
# Setting up
# Running test
# Tearing down
# Test Finished
#
# ###### In Test 2 ######
# Setting up
# Running test
# Tearing down
# Test Finished
#
# ###### In Test 3 ######
# Setting up
# Running test
# Tearing down
# Test Finished
#
