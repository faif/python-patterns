import weakref


class FlyweightMeta(type):
    def __new__(mcs, name, parents, dct):
        """
        Set up object pool

        :param name: class name
        :param parents: class parents
        :param dct: dict: includes class attributes, class methods,
        static methods, etc
        :return: new class
        """
        dct["pool"] = weakref.WeakValueDictionary()
        return super().__new__(mcs, name, parents, dct)

    @staticmethod
    def _serialize_params(cls, *args, **kwargs):
        """
        Serialize input parameters to a key.
        Simple implementation is just to serialize it as a string. ``repr`` keeps
        ``("1", "0")``, ``("10",)`` and ``(1,)`` apart, and sorting the keyword
        arguments makes the key independent of their order.
        """
        return repr((cls.__name__, args, sorted(kwargs.items())))

    def __call__(cls, *args, **kwargs):
        key = FlyweightMeta._serialize_params(cls, *args, **kwargs)
        pool = getattr(cls, "pool", {})

        instance = pool.get(key)
        if instance is None:
            instance = super().__call__(*args, **kwargs)
            pool[key] = instance
        return instance


class Card2(metaclass=FlyweightMeta):
    def __init__(self, *args, **kwargs):
        # print('Init {}: {}'.format(self.__class__, (args, kwargs)))
        pass


if __name__ == "__main__":
    instances_pool = getattr(Card2, "pool")
    cm1 = Card2("10", "h", a=1)
    cm2 = Card2("10", "h", a=1)
    cm3 = Card2("10", "h", a=2)

    assert (cm1 == cm2) and (cm1 != cm3)
    assert (cm1 is cm2) and (cm1 is not cm3)
    assert len(instances_pool) == 2

    del cm1
    assert len(instances_pool) == 2

    del cm2
    assert len(instances_pool) == 1

    del cm3
    assert len(instances_pool) == 0
