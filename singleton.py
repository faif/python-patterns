class Singleton(object):
    """A singleton class. For easier memory management

    Examples
    --------
    >>> a = Singleton()
    >>> b = Singleton()
    >>> a is b
    True
    """
    __singleton = None

    def __new__(cls, *args, **kws):
        instance = super(Singleton, cls).__new__(cls, *args, **kws)
        if Singleton.__singleton:
            return Singleton.__singleton
        else:
            Singleton.__singleton = instance
            return instance
