#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
An example of the Template pattern in Python

*TL;DR80
Defines the skeleton of a base algorithm, deferring definition of exact 
steps to subclasses.
"""


def get_text():
    return "plain-text"


def get_pdf():
    return "pdf"


def get_csv():
    return "csv"


def convert_to_text(data):
    print("[CONVERT]")
    return "{} as text".format(data)


def saver():
    print("[SAVE]")


def template_function(getter, converter=False, to_save=False):
    data = getter()
    print("Got `{}`".format(data))

    if len(data) <= 3 and converter:
        data = converter(data)
    else:
        print("Skip conversion")

    if to_save:
        saver()

    print("`{}` was processed".format(data))


if __name__ == "__main__":
    template_function(get_text, to_save=True)
    print("-" * 30)
    template_function(get_pdf, converter=convert_to_text)
    print("-" * 30)
    template_function(get_csv, to_save=True)

### OUTPUT ###
# Got `plain-text`
# Skip conversion
# [SAVE]
# `plain-text` was processed
# ------------------------------
# Got `pdf`
# [CONVERT]
# `pdf as text` was processed
# ------------------------------
# Got `csv`
# Skip conversion
# [SAVE]
# `csv` was processed
