
class Awesome:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print "Hello ! ", self.a, self.b

    def __add__(self, other):
        print "I am inside the add "
        print self.a + other.a
        print self.b + other.b

    def __div__(self, other):
        print self.a / other.a

    def __sub__(self, other):
        print self.b - other.b

    def __mul__(self, other):
        print self.b * other.b

    def __eq__(self, other):
        print self.a , other.b
        print self.b, other.a
        if self.a == other.a:
            return "Awes"
        else:
            return "Cool"

    def __le__(self, other):
        if self.a > other.a:
            print "Cool man"
        else:
            print "Not done yet"


an = Awesome(5, 3)
bn = Awesome(6, 2)
cn = Awesome(9000, 3000)
an.__add__(cn)
an - bn
an / bn
an * bn
an >= bn
an == bn
