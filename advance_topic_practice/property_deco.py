class Person():
    def __init__(self):
        self.emp = 23

    def fget(self):
        return self.emp

    def fset(self, value):
        self.emp = value
        return self.emp

    def fdel(self):
        print 'deleting'
        del self.emp
        
    name = property(fget=None, fset=None, fdel=None, doc="Cool Bro, now u got it")


p = Person()
p.name = 34
print p.name
del p.name
print 'done'
