#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""http://www.testingperspective.com/wiki/doku.php/collaboration/chetan/designpatternsinpython/chain-of-responsibilitypattern"""

class Handler:
    def __init__(self,successor):
        self._successor = successor;
    def handle(self,request):
        i = self._handle(request)
        if  not i:
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


class Client:
    def __init__(self):
        self.handler = ConcreteHandler1(ConcreteHandler3(ConcreteHandler2(DefaultHandler(None))))
    def delegate(self, requests):
        for request in requests:
            self.handler.handle(request)


if __name__ == "__main__":
    client = Client()
    requests = [2, 5, 14, 22, 18, 3, 35, 27, 20]
    client.delegate(requests)

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
