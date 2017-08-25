# Memoization in python... There are many wasy to work on that..


def memoize(f):
    cache = {}
    def call(a):
        if a not in cache:
            cache[a] = f(a)
        else:
            return cache[a]
    return call


@memoize
def add_to(a):
    print "Adding the two values in "
    print a


a = input("First : ")

print add_to(a)

print '*'*100

def func_to_memoize(n, memo={}):
    if n in memo:
        ans = memo[n]
    elif n <= 2:
        ans = 1
        memo[n] = ans

    else:
        ans = func_to_memoize(n-2) + func_to_memoize(n-1)
        memo[n] = ans
    return ans

b = input("Input for facto : ")
print func_to_memoize(b)

print '*'*100
