#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

class AbstractSales:
    def talk(self):
        raise NotImplementEderror


class SalesManager(AbstractSales):
    def talk(self):
        print("Sales Manager ready to talk")


class Proxy(AbstractSales):
    def __init__(self):
        self.busy = 'No'
        self.sales = None

    def talk(self):
        print("Proxy checking for Sales Manager availability")
        if self.busy == 'No':
            self.sales = SalesManager()
            time.sleep(0.1)
            self.sales.talk()
        else:
            time.sleep(0.1)
            print("Sales Manager is busy")


class NoTalkProxy(AbstractSales):
    def __init__(self):
        self.busy = 'No'
        self.sales = None

    def talk(self):
        print("Proxy checking for Sales Manager availability")
        time.sleep(0.1)
        print("This Sales Manager will not talk to you whether he/she is busy or not")


if __name__ == '__main__':
    p = Proxy()
    p.talk()
    p.busy = 'Yes'
    p.talk()
    p = NoTalkProxy()
    p.talk()
    p.busy = 'Yes'
    p.talk()

### OUTPUT ###
# Proxy checking for Sales Manager availability
# Sales Manager ready to talk
# Proxy checking for Sales Manager availability
# Sales Manager is busy
# Proxy checking for Sales Manager availability
# This Sales Manager will not talk to you whether he/she is busy or not
# Proxy checking for Sales Manager availability
# This Sales Manager will not talk to you whether he/she is busy or not
