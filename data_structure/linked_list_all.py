import sys

class Node:
    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next_node
    def set_data(self, d):
        self.data = d
    def set_next(self, n):
        self.next_node = n

class LinkedList:
    def __init__(self, r=None):
        self.root = r
        self.size = 0
    def get_size(self):
        return self.size

    def push(self, data):
        node = Node(data, self.root)
        self.root = node
        self.size += 1

    def find(self, d):
        node = self.root
        while node:
            if node.get_data() == d:
                return d
            else:
                node = node.get_next()
        return None

    def all_data(self):
        node = self.root
        while node != None:
            print node.get_data()
            node = node.get_next()

    def swapNodes(self, p, r):
        if p == r:
            print "Both the data are same ... Operation wont work."
            return

        currX = self.root
        prevX = None
        while currX != None and currX.get_data() != p:
            prevX = currX
            currX = currX.get_next()

        currY = self.root
        prevY = None
        while currY != None and currY.get_data() != r:
            prevY = currY
            currY = currY.get_next()

        if currX == None or currY == None:
            return
        
        if prevX != None:
            prevX.set_next(currY)
        else:
            self.root = currY

        if prevY != None:
            prevY.set_next(currX)
        else:
            self.root = currX
        
        temp = currY.get_next()
        currY.set_next(currX.get_next())
        currX.set_next(temp)

    def reverse(self):
        self.prev = None
        node = self.root
        while node != None:
            temp = node.get_next()
            node.set_next(self.prev)
            self.prev = node
            node = temp
        self.root = self.prev

    def remove(self, d):
        self.prev = None
        node = self.root
        while node != None:
            if node.get_data() == d:
                if self.prev:
                    self.prev.set_next(node.get_next())
                else:
                    self.root = node.get_next()
                self.size -= 1
                return True
            else:
                self.prev = node
                node = node.get_next()
        return False

    # sorted linked list
    def sorted_data(self):
        node = self.root
        if node == None:
            return
        while node != None:
            new = node.get_next()
            if new == None:
                return
            if node.get_data() == new.get_data():
                self.remove(node.get_data())
            node = node.get_next()

    # unsorted data in linked list
    def unsorted_data(self):
        node = self.root
        while node != None:
            node1 = node.get_next()
            while node1 != None:
                if node.get_data() == node1.get_data():
                    self.remove(node.get_data())
                node1 = node1.get_next()
            node = node.get_next()
            
            
    def last_to_first(self):
        node = self.root
        self.prev = None
        if node == None or node.get_next() == None:
            return

        while node.get_next() != None:
            self.prev = node
            node = node.get_next()

        print self.prev.get_data(), '1'
        print self.root.get_data(), '6'
        self.prev.set_next(None)
        print node.get_data()
        node.set_next(self.root)
        self.root = node
            
    def identical_data(self, obj, obj1):
        node = obj.root
        node1 = obj1.root

        while node != None and node1 != None:
            if node.get_data() != node1.get_data():
                return False
            node = node.get_next()
            node1 = node1.get_next()

        return True

    def isPalindrome(self, word):
        return word == word[::-1]

    def palindrome(self):
        node = self.root
        temp = []
        while node != None:
            temp.append(node.get_data())
            node = node.get_next()

        data = ''.join(temp)
        if self.isPalindrome(data):
            print "It is Palindrome"
        else:
            print "Nope.."
    
        
n = LinkedList()
n.push(1)
n.push(2)
n.push(3)
n.push(2)
n.push(4)
n.push(6)
n.push(5)
n.push(6)

n1 = LinkedList()
n1.push(1)
n1.push(2)
n1.push(3)
n1.push(2)
n1.push(4)
n1.push(9)
n1.push(5)
n1.push(6)

n2 = LinkedList()
n2.push('a')
n2.push('a')
n2.push('a')
n2.push('b')
n2.push('b')
n2.push('a')
n2.push('a')
n2.push('a')

print n2.get_size()
print 'all values : ', n2.all_data()

n2.palindrome()
#print n2.identical_data(n, n1)
#n.last_to_first()
#print 'all values : ', n.all_data()
#p = input("Enter two values to swap ")
#r = input("Enter two values to swap ")
# n.swapNodes(p, r)
# n.sorted_data()
#n.unsorted_data()
#print n.get_size()
#print 'all values : ', n.all_data()
#print n.reverse()
# print 'ending : ',n.all_data()
# q = input("Enter value to delete : ")
# print n.remove(q)
#while True:
#    m = input("Enter ur value to check : ")
 #   if m == 0:
  #      sys.exit()
   # print n.find(m)


