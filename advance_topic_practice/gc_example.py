import gc


def con():
    l = []
    l.append(l)


def gc_func():
    collected = gc.collect()
    print "collected : ", collected

    for i in xrange(10):
        con()
    
    collected = gc.collect()
    print "collected ", collected


gc_func()
