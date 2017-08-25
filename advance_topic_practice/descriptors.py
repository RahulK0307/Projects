# going to define the way descriptors works and need to get it right

class Description:
    def __init__(self, name):
        self.name = name
        print "Descriptor *{}*  has been started ".format(self.name)

    def __get__(self):
        print "trying to get the value of the class"
        return self.name

    def __set__(self, value):
        self.name = value
        print "new name is %s" %(self.name)    

    def __delete__(self):
        del self.name
        print "value of name has been deleted successfully"



d = Description("Rahul")
print d.__get__()

print type(Description) , "Type of the class"

print "*"*50

print d.__set__('Kourav')


print d.__delete__()
