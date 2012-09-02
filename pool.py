'''http://stackoverflow.com/questions/1514120/python-implementation-of-the-object-pool-design-pattern'''

class qObj():   
    _q = None   
    o = None    

    def __init__(self, dQ, autoGet = False):       
        self._q = dQ        
        
        if autoGet == True:           
            self.o = self._q.get()    

    def __enter__(self):       
        if self.o == None:           
            self.o = self._q.get()           
        return self.o     

    def __exit__(self, type, value, traceback):       
        if self.o != None:           
            self._q.put(self.o)           
            self.o = None    

    def __del__(self):       
        if self.o != None:           
            self._q.put(self.o)           
            self.o = None   

if __name__ == "__main__":
    try:
        import queue as Queue
    except:                     # python 2.x compatibility
        import Queue

    def testObj(Q):       
        someObj = qObj(Q, True)        
        print('Inside func: {}'.format(someObj.o))    

    aQ = Queue.Queue()
    aQ.put("yam")    

    with qObj(aQ) as obj:       
        print("Inside with: {}".format(obj))    

    print('Outside with: {}'.format(aQ.get()))

    aQ.put("sam")
    testObj(aQ)

    print('Outside func: {}'.format(aQ.get()))

    if not aQ.empty():
        print(aQ.get())
