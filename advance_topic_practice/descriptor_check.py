# descriptors that will hep to understand the concept of the same

class Active_class(object):
    '''class with get and return the calus as per the request'''
    def __init__(self, initval=None, name="var"):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print "retirving the value : ", self.name
        return self.val

    def __set__(self, obj, val):
        print "anem is ", self.name
        self.val = val


class CheckFunction(object):
    active = Active_class(10, "cool RK")
    print active.__weakref__
    def __init__(self):
        print "i have been called so many times..."


c = CheckFunction()
print c.__dict__
print c.__weakref__
print c.active
print dir(c)
