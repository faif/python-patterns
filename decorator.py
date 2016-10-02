#!/usr/bin/env python
"""
Reference: https://en.wikipedia.org/wiki/Decorator_pattern
"""


class TextTag(object):
    """Represents a base text tag"""
    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


class BoldWrapper(object):
    """Wraps a tag in <b>"""
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<b>{}</b>".format(self._wrapped.render())


class ItalicWrapper(object):
    """Wraps a tag in <i>"""
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<i>{}</i>".format(self._wrapped.render())

if __name__ == '__main__':
    simple_hello = TextTag("hello, world!")
    special_hello = ItalicWrapper(BoldWrapper(simple_hello))
    print("before:", simple_hello.render())
    print("after:", special_hello.render())

### OUTPUT ###
# before: hello, world!
# after: <i><b>hello, world!</b></i>
