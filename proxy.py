#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time


class SalesManager:
    def work(self):
        print("Sales Manager working...")

    def talk(self):
        print("Sales Manager ready to talk")


class Proxy:
    def __init__(self):
        self.busy = 'No'
        self.sales = None

    def work(self):
        print("Proxy checking for Sales Manager availability")
        if self.busy == 'No':
            self.sales = SalesManager()
            time.sleep(2)
            self.sales.talk()
        else:
            time.sleep(2)
            print("Sales Manager is busy")


class NoTalkProxy(Proxy):
    def __init__(self):
        Proxy.__init__(self)

    def work(self):
        print("Proxy checking for Sales Manager availability")
        time.sleep(2)
        print("This Sales Manager will not talk to you whether he/she is busy or not")


if __name__ == '__main__':
    p = Proxy()
    p.work()
    p.busy = 'Yes'
    p.work()
    p = NoTalkProxy()
    p.work()
    p.busy = 'Yes'
    p.work()

### OUTPUT ###
# Proxy checking for Sales Manager availability
# Sales Manager ready to talk
# Proxy checking for Sales Manager availability
# Sales Manager is busy
# Proxy checking for Sales Manager availability
# This Sales Manager will not talk to you whether he/she is busy or not
# Proxy checking for Sales Manager availability
# This Sales Manager will not talk to you whether he/she is busy or not
