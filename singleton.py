class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance


##Check if instance of singleton class is same. As singleton instance will be same always.
if __name__ == '__main__':
    
    instance1=Singleton()
    
    instance2=Singleton()
    
    if id(instance1) == id(instance2):
        print "Same"
    else:
        print "Different"
