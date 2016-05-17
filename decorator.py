#!/usr/bin/env python
"""https://docs.python.org/2/library/functools.html#functools.wraps"""
"""https://stackoverflow.com/questions/739654/how-can-i-make-a-chain-of-function-decorators-in-python/739665#739665"""

from functools import wraps


def makebold(fn):
    return getwrapped(fn, "b")


def makeitalic(fn):
    return getwrapped(fn, "i")


def getwrapped(fn, tag):
    @wraps(fn)
    def wrapped():
        return "<%s>%s</%s>" % (tag, fn(), tag)
    return wrapped


@makebold
@makeitalic
def hello():
    """a decorated hello world"""
    return "hello world"

if __name__ == '__main__':
    print('result:{}   name:{}   doc:{}'.format(hello(), hello.__name__, hello.__doc__))

### OUTPUT ###
# result:<b><i>hello world</i></b>   name:hello   doc:a decorated hello world
