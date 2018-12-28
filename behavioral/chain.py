#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*What is this pattern about?

The Chain of responsibility is an object oriented version of the
`if ... elif ... elif ... else ...` idiom, with the
benefit that the condition–action blocks can be dynamically rearranged
and reconfigured at runtime.

This pattern aims to decouple the senders of a request from its
receivers by allowing request to move through chained
receivers until it is handled.

Request receiver in simple form keeps a reference to a single successor.
As a variation some receivers may be capable of sending requests out
in several directions, forming a `tree of responsibility`.

*TL;DR80
Allow a request to pass down a chain of receivers until it is handled.
"""

import abc


class Handler(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, request):
        """
        Handle request and stop.
        If can't - call next handler in chain.

        As an alternative you might even in case of success
        call the next handler.
        """
        res = self.compare(request)
        if not res and self.successor:
            self.successor.handle(request)

    @abc.abstractmethod
    def compare(self, request):
        """Compare passed value to predefined interval"""


class ConcreteHandler0(Handler):
    def compare(self, request):
        if 0 <= request < 10:
            print('request {} handled in handler 0'.format(request))
            return True


class ConcreteHandler1(Handler):
    def compare(self, request):
        if 10 <= request < 20:
            print('request {} handled in handler 1'.format(request))
            return True


class ConcreteHandler2(Handler):
    def compare(self, request):
        if 20 <= request < 30:
            print('request {} handled in handler 2'.format(request))
            return True


class DefaultHandler(Handler):
    def compare(self, request):
        print('end of chain, no handler for {}'.format(request))
        return False


if __name__ == "__main__":
    h0 = ConcreteHandler0()
    h1 = ConcreteHandler1()
    h2 = ConcreteHandler2(DefaultHandler())
    h0.successor = h1
    h1.successor = h2

    requests = [2, 5, 14, 22, 18, 3, 35, 27, 20]
    for request in requests:
        h0.handle(request)

### OUTPUT ###
# request 2 handled in handler 0
# request 5 handled in handler 0
# request 14 handled in handler 1
# request 22 handled in handler 2
# request 18 handled in handler 1
# request 3 handled in handler 0
# end of chain, no handler for 35
# request 27 handled in handler 2
# request 20 handled in handler 2
