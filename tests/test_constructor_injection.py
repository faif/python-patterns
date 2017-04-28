#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from dft.constructor_injection import TimeDisplay, MidnightTimeProvider, ProductionCodeTimeProvider, datetime

"""
Port of the Java example of "Constructor Injection" in
"xUnit Test Patterns - Refactoring Test Code" by Gerard Meszaros
(ISBN-10: 0131495054, ISBN-13: 978-0131495050)

Test code which will almost always fail (if not exactly 12:01) when untestable
production code (production code time provider is datetime) is used:

    def test_display_current_time_at_midnight(self):
        class_under_test = TimeDisplay()
        expected_time = "24:01"
        result = class_under_test.get_current_time_as_as_html_fragment()
        self.assertEqual(result, expected_time)
"""

class ConstructorInjectionTest(unittest.TestCase):

    def test_display_current_time_at_midnight(self):
        """
        Will almost always fail (despite of right at/after midnight).
        """
        time_provider_stub = MidnightTimeProvider()
        class_under_test = TimeDisplay(time_provider_stub)
        expected_time = "<span class=\"tinyBoldText\">24:01</span>"
        self.assertEqual(class_under_test.get_current_time_as_html_fragment(), expected_time)

    def test_display_current_time_at_current_time(self):
        """
        Just as justification for working example. (Will always pass.)
        """
        production_code_time_provider = ProductionCodeTimeProvider()
        class_under_test = TimeDisplay(production_code_time_provider)
        current_time = datetime.datetime.now()
        expected_time = "<span class=\"tinyBoldText\">{}:{}</span>".format(current_time.hour, current_time.minute)
        self.assertEqual(class_under_test.get_current_time_as_html_fragment(), expected_time)

