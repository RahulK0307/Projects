

def add(a,b):
    return a+b

def sub(b,c):
    return b-c

class total:
    def use(self):
        return "i am in my own class"

    def done(self):
        return "my work is done"

t = total()
print "hahha"
function = {'a': add(4,5),
            'b': sub(10, 5),
            'c': t.use(),
            'd': t.done()}
print function

for k, v in function.items():

    print k,  ":",  v
