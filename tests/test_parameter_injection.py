#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from dft.parameter_injection import TimeDisplay, MidnightTimeProvider, ProductionCodeTimeProvider, datetime

"""
Port of the Java example of "Parameter Injection" in
"xUnit Test Patterns - Refactoring Test Code" by Gerard Meszaros
(ISBN-10: 0131495054, ISBN-13: 978-0131495050) accessible in outdated version on
http://xunitpatterns.com/Dependency%20Injection.html.

Test code which will almost always fail (if not exactly 12:01) when untestable
production code (have a look into constructor_injection.py) is used:

    def test_display_current_time_at_midnight(self):
        class_under_test = TimeDisplay()
        expected_time = "24:01"
        result = class_under_test.get_current_time_as_as_html_fragment()
        self.assertEqual(result, expected_time)
"""

class ParameterInjectionTest(unittest.TestCase):

    def test_display_current_time_at_midnight(self):
        """
        Would almost always fail (despite of right at/after midnight) if
        untestable production code would have been used.
        """
        time_provider_stub = MidnightTimeProvider()
        class_under_test = TimeDisplay()
        expected_time = "<span class=\"tinyBoldText\">24:01</span>"
        self.assertEqual(class_under_test.get_current_time_as_html_fragment(time_provider_stub), expected_time)

    def test_display_current_time_at_current_time(self):
        """
        Just as justification for working example with the time provider used in
        production. (Will always pass.)
        """
        production_code_time_provider = ProductionCodeTimeProvider()
        class_under_test = TimeDisplay()
        current_time = datetime.datetime.now()
        expected_time = "<span class=\"tinyBoldText\">{}:{}</span>".format(current_time.hour, current_time.minute)
        self.assertEqual(class_under_test.get_current_time_as_html_fragment(production_code_time_provider), expected_time)

