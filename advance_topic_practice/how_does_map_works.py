
def gmap(func, iterables):
    print func.__name__
    for item in iterables:
        print func(item)


def map(func, iterables):
    print func.__name__
    return list(gmap(func, iterables))


def adds(item):
    return item*2

print map(adds, [1,2,3,4,5])

