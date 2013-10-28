# http://stackoverflow.com/questions/3118929/implementing-the-decorator-pattern-in-python


class foo_decorator(object):
    def __init__(self, decoratee):
        self._decoratee = decoratee

    def f1(self):
        print("decorated f1")
        self._decoratee.f1()

    def __getattr__(self, name):
        return getattr(self._decoratee, name)


class undecorated_foo(object):
    def f1(self):
        print("original f1")

    def f2(self):
        print("original f2")


@foo_decorator
class decorated_foo(object):
    def f1(self):
        print("original f1")

    def f2(self):
        print("original f2")


def main():
    u = undecorated_foo()
    v = foo_decorator(u)
    # The @foo_decorator syntax is just shorthand for calling
    # foo_decorator on the decorated object right after its
    # declaration.

    v.f1()
    v.f2()

if __name__ == '__main__':
    main()
