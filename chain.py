# http://www.testingperspective.com/wiki/doku.php/collaboration/chetan/designpatternsinpython/chain-of-responsibilitypattern


class Handler:
    def successor(self, successor):
        self.successor = successor


class ConcreteHandler1(Handler):
    def handle(self, request):
        if 0 < request <= 10:
            print("in handler1")
        else:
            self.successor.handle(request)


class ConcreteHandler2(Handler):
    def handle(self, request):
        if 10 < request <= 20:
            print("in handler2")
        else:
            self.successor.handle(request)


class ConcreteHandler3(Handler):
    def handle(self, request):
        if 20 < request <= 30:
            print("in handler3")
        else:
            print('end of chain, no handler for {}'.format(request))


class Client:
    def __init__(self):
        h1 = ConcreteHandler1()
        h2 = ConcreteHandler2()
        h3 = ConcreteHandler3()

        h1.successor(h2)
        h2.successor(h3)

        self.handlers = (h1,h2,h3)

    def delegate(self, requests):
        for request in requests:
            self.handlers[0].handle(request)


if __name__ == "__main__":
    client = Client()
    requests = [2, 5, 14, 22, 18, 3, 35, 27, 20]
    client.delegate(requests)
