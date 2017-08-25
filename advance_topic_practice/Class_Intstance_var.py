class Apple:
    A = 5
    def __init__(self, b):
        self.b = b
        self.a = 6
        self.v = 5
        # self.A = 290
        
    def values(self):
        print self.v, '+', self.b

    def add(self, c):
        self.c = c
        print self.c

class Orange:
    def __init__(self):
        print 'cool'

    def called_every(self, val):
        app = Apple(val)
        print "app", app.__dict__
        if val == 0:
            print 'app.v ', app.b

        else:
            print "cool bro", app.b
            print "cool bro", app.a
            print "cool bro", app.v
            print "cool bro", app.A
            print "app", app.__dict__
            app.add(4567)
            print "cool bro", app.c

d = Apple(567)
print d.__dict__
print "cool bro", d.b
print "cool bro", d.a
print "cool bro", d.v
print "cool bro", d.A
d.add(5)
print "cool bro", d.v
print "cool bro", d.c
print d.__dict__

print "Classsss ", Apple.A
print "Classsss ", Apple.__dict__
o = Orange()
o.called_every(6789)





