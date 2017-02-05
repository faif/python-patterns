#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""http://www.dabeaz.com/coroutines/"""

from contextlib import contextmanager
import os
import sys
import time


class Handler(object):

    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        res = self._handle(request)
        if not res:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError('Must provide implementation in subclass.')


class ConcreteHandler1(Handler):

    def _handle(self, request):
        if 0 < request <= 10:
            print('request {} handled in handler 1'.format(request))
            return True


class ConcreteHandler2(Handler):

    def _handle(self, request):
        if 10 < request <= 20:
            print('request {} handled in handler 2'.format(request))
            return True


class ConcreteHandler3(Handler):

    def _handle(self, request):
        if 20 < request <= 30:
            print('request {} handled in handler 3'.format(request))
            return True


class DefaultHandler(Handler):

    def _handle(self, request):
        print('end of chain, no handler for {}'.format(request))
        return True


class Client(object):

    def __init__(self):
        self.handler = ConcreteHandler1(
            ConcreteHandler3(ConcreteHandler2(DefaultHandler())))

    def delegate(self, requests):
        for request in requests:
            self.handler.handle(request)


def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start


@coroutine
def coroutine1(target):
    while True:
        request = yield
        if 0 < request <= 10:
            print('request {} handled in coroutine 1'.format(request))
        else:
            target.send(request)


@coroutine
def coroutine2(target):
    while True:
        request = yield
        if 10 < request <= 20:
            print('request {} handled in coroutine 2'.format(request))
        else:
            target.send(request)


@coroutine
def coroutine3(target):
    while True:
        request = yield
        if 20 < request <= 30:
            print('request {} handled in coroutine 3'.format(request))
        else:
            target.send(request)


@coroutine
def default_coroutine():
    while True:
        request = yield
        print('end of chain, no coroutine for {}'.format(request))


class ClientCoroutine:

    def __init__(self):
        self.target = coroutine1(coroutine3(coroutine2(default_coroutine())))

    def delegate(self, requests):
        for request in requests:
            self.target.send(request)


def timeit(func):

    def count(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        count._time = time.time() - start
        return res
    return count


@contextmanager
def suppress_stdout():
    try:
        stdout, sys.stdout = sys.stdout, open(os.devnull, 'w')
        yield
    finally:
        sys.stdout = stdout


if __name__ == "__main__":
    client1 = Client()
    client2 = ClientCoroutine()
    requests = [2, 5, 14, 22, 18, 3, 35, 27, 20]

    client1.delegate(requests)
    print('-' * 30)
    client2.delegate(requests)

    requests *= 10000
    client1_delegate = timeit(client1.delegate)
    client2_delegate = timeit(client2.delegate)
    with suppress_stdout():
        client1_delegate(requests)
        client2_delegate(requests)
    # lets check what is faster
    print(client1_delegate._time, client2_delegate._time)

### OUTPUT ###
# request 2 handled in handler 1
# request 5 handled in handler 1
# request 14 handled in handler 2
# request 22 handled in handler 3
# request 18 handled in handler 2
# request 3 handled in handler 1
# end of chain, no handler for 35
# request 27 handled in handler 3
# request 20 handled in handler 2
# ------------------------------
# request 2 handled in coroutine 1
# request 5 handled in coroutine 1
# request 14 handled in coroutine 2
# request 22 handled in coroutine 3
# request 18 handled in coroutine 2
# request 3 handled in coroutine 1
# end of chain, no coroutine for 35
# request 27 handled in coroutine 3
# request 20 handled in coroutine 2
# (0.2369999885559082, 0.16199994087219238)
