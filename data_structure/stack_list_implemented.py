

class stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print self.items

    def popitem(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items)-1]

    def isEmpty(self):
        return True if len(self.items) == 0 else False


s = stack()
print "Empty : ", s.isEmpty()
s.push('Cool')
s.push('Job')
print "Items ", s.push('Done')
print "size : ", s.size()
print "peek is : ", s.peek()
print "Empty : ", s.isEmpty()

