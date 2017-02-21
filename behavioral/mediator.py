#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""http://web.archive.org/web/20120309135549/http://dpip.testingperspective.com/?p=28"""

import random
import time


class TC:

    def __init__(self):
        self._tm = None
        self._bProblem = 0

    def setup(self):
        print("Setting up the Test")
        time.sleep(0.1)
        self._tm.prepareReporting()

    def execute(self):
        if not self._bProblem:
            print("Executing the test")
            time.sleep(0.1)
        else:
            print("Problem in setup. Test not executed.")

    def tearDown(self):
        if not self._bProblem:
            print("Tearing down")
            time.sleep(0.1)
            self._tm.publishReport()
        else:
            print("Test not executed. No tear down required.")

    def setTM(self, tm):
        self._tm = tm

    def setProblem(self, value):
        self._bProblem = value


class Reporter:

    def __init__(self):
        self._tm = None

    def prepare(self):
        print("Reporter Class is preparing to report the results")
        time.sleep(0.1)

    def report(self):
        print("Reporting the results of Test")
        time.sleep(0.1)

    def setTM(self, tm):
        self._tm = tm


class DB:

    def __init__(self):
        self._tm = None

    def insert(self):
        print("Inserting the execution begin status in the Database")
        time.sleep(0.1)
        # Following code is to simulate a communication from DB to TC
        if random.randrange(1, 4) == 3:
            return -1

    def update(self):
        print("Updating the test results in Database")
        time.sleep(0.1)

    def setTM(self, tm):
        self._tm = tm


class TestManager:

    def __init__(self):
        self._reporter = None
        self._db = None
        self._tc = None

    def prepareReporting(self):
        rvalue = self._db.insert()
        if rvalue == -1:
            self._tc.setProblem(1)
            self._reporter.prepare()

    def setReporter(self, reporter):
        self._reporter = reporter

    def setDB(self, db):
        self._db = db

    def publishReport(self):
        self._db.update()
        self._reporter.report()

    def setTC(self, tc):
        self._tc = tc


if __name__ == '__main__':
    reporter = Reporter()
    db = DB()
    tm = TestManager()
    tm.setReporter(reporter)
    tm.setDB(db)
    reporter.setTM(tm)
    db.setTM(tm)
    # For simplification we are looping on the same test.
    # Practically, it could be about various unique test classes and their
    # objects
    for i in range(3):
        tc = TC()
        tc.setTM(tm)
        tm.setTC(tc)
        tc.setup()
        tc.execute()
        tc.tearDown()

### OUTPUT ###
# Setting up the Test
# Inserting the execution begin status in the Database
# Executing the test
# Tearing down
# Updating the test results in Database
# Reporting the results of Test
# Setting up the Test
# Inserting the execution begin status in the Database
# Reporter Class is preparing to report the results
# Problem in setup. Test not executed.
# Test not executed. No tear down required.
# Setting up the Test
# Inserting the execution begin status in the Database
# Executing the test
# Tearing down
# Updating the test results in Database
# Reporting the results of Test
