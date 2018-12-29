"""
*What is this pattern about?

The pattern is about making sure that there is only one instance of a class.
you cant make another object of the singelton class, and you can get the only object that exist by using static function

*What does this example do?

The example shows a Configuration object, which we can have only one instnace of the class,
our configuration is that we are using windows as our operation system, and we cannot have another 
configuration object, beacuse we are only using windows.
The example show what happend if we would try creating another instance of Configuration,
it is also show how to get the only instance that exsits.

*Where is the pattern used practically?
Facade objects are often singletons because only one facade object is required.
State objects are often singletons.

*References:
https://en.wikipedia.org/wiki/Singleton_pattern

*TL;DR80
Provides a way to limit the number of instances of a class.
"""

class Configuration(object):
    instance = None # at the start there is no instance of the Singelton class
    
    @staticmethod
    def getInstance():
        if Configuration.instance == None:
            return Configuration("")
        else:
            return Configuration.instance
    
    def __init__(self, configuration):
        if Configuration.instance != None:
            raise Exception("There is already configuration in the system")
        else:
            self.config = configuration
            Configuration.instance = self
            
    def getConfig(self):
        return self.config
            
if __name__ == "__main__":
    config = "The Operating System you are using is Windows"
    
    c = Configuration(config)
    
    print(c.getConfig())
    print
    
    try:
        c2 = Configuration("another configuration")
    except Exception as e:
        print(e)
        
    print
    
    c3 = Configuration.getInstance()
    print(c3.getConfig())
### OUTPUT ###
#The Operating System you are using is Windows
#
#There is already configuration in the system
#
#The Operating System you are using is Windows
    
