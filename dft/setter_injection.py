#!/usr/bin/python
# -*- coding : utf-8 -*-
import datetime

"""
Port of the Java example of "Setter Injection" in
"xUnit Test Patterns - Refactoring Test Code" by Gerard Meszaros
(ISBN-10: 0131495054, ISBN-13: 978-0131495050) accessible in outdated version on
http://xunitpatterns.com/Dependency%20Injection.html.

production code which is untestable:

class TimeDisplay(object):

    def __init__(self):
        self.time_provider = datetime.datetime

    def get_current_time_as_html_fragment(self):
        current_time = self.time_provider.now()
        current_time_as_html_fragment = "<span class=\"tinyBoldText\">{}</span>".format(current_time)
        return current_time_as_html_fragment
"""


class TimeDisplay(object):

    def __init__(self):
        pass

    def set_time_provider(self, time_provider):
        self.time_provider = time_provider

    def get_current_time_as_html_fragment(self):
        current_time = self.time_provider.now()
        current_time_as_html_fragment = "<span class=\"tinyBoldText\">{}</span>".format(current_time)
        return current_time_as_html_fragment


class ProductionCodeTimeProvider(object):
    """
    Production code version of the time provider (just a wrapper for formatting
    datetime for this example).
    """

    def now(self):
        current_time = datetime.datetime.now()
        current_time_formatted = "{}:{}".format(current_time.hour,
                                                current_time.minute)
        return current_time_formatted


class MidnightTimeProvider(object):
    """
    Class implemented as hard-coded stub (in contrast to configurable stub).
    """

    def now(self):
        current_time_is_always_midnight = "24:01"
        return current_time_is_always_midnight
