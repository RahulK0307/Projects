

def singleton(fn):
    cache = []
    def newfunc(*args, **kwargs):
        while len(cache) < 6:
            if fn not in cache:
                cache.append(fn(*args, **kwargs))
        return cache
    return newfunc


@singleton
class Myname():
    print "This is me bro"
    

m = Myname()
print m

n = Myname()
print n

p = Myname()
print p

q = Myname()
print q

r = Myname()
print r

s = Myname()
print s

t = Myname()
print t
