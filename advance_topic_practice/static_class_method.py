# it will have a class , static and a normal method that will work as expected

class AllinOne(object):
    ''' This i my Class representation'''
    
    def __init__(self):
        print "Hello rahul this is me"

    def normal_method(self, x):
        return "the value of %s and %s "%(self, x)
    
    @classmethod
    def class_method(cls, x):
        return "the value of %s and %s "%(cls, x)

    @staticmethod
    def static_method(x):
        return "the value of %s "%x


a = AllinOne()

print "first ", AllinOne().normal_method(2)

##print "first second ", AllinOne.normal_method(2)

##print 'normal method', a.normal_method(57)
##print 'dir is ', dir(a)
##print 'class method is', AllinOne.class_method(45)
##print 'Statis method is ', a.static_method(47)
##print 'class statis method', AllinOne.static_method(89)
print 'main ', AllinOne.class_method(34)
print 'main 2 ', AllinOne().class_method(45)
print 'main 3', a.class_method(56)
print "="*100
print 'static ', AllinOne.class_method(34)
print 'staic 2 ', AllinOne().class_method(45)
print 'static  3', a.class_method(56)
print "="*100
print 'docs  -->>', a.__doc__
print 'dict  -->>', a.__dict__
print 'class  -->>', a.__class__
print 'hash  -->>', a.__hash__
print 'repr  -->>', a.__repr__
print 'str  -->>', a.__str__
print 'sizeof  -->>', a.__sizeof__()
print 'new  -->>', a.__new__
print 'module  -->>', a.__module__
print 'reduce  -->>', a.__reduce__
print 'mro  -->>', isinstance(a, AllinOne)
print 'docs  -->>', issubclass(AllinOne, AllinOne)
