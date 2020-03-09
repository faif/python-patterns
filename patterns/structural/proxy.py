"""
*What is this pattern about?
Proxy is used in places where you want to add functionality to a class without changing its interface. The main class is called `Real Subject`. A client should use the proxy or the real subject without any code change, so both must have the same interface. Logging and controlling access to the real subject are some of the proxy pattern usages.

*References:
https://refactoring.guru/design-patterns/proxy/python/example
https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Fronting.html

*TL;DR
Provides an interface to resource that is expensive to duplicate.
"""

import time


class SalesManager:
    def talk(self):
        print("Sales Manager ready to talk")


class Proxy:
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


class NoTalkProxy(Proxy):
    def talk(self):
        print("Proxy checking for Sales Manager availability")
        time.sleep(0.1)
        print("This Sales Manager will not talk to you", "whether he/she is busy or not")


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
