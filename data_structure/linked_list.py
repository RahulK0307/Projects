# nice way to interact with the data structure while writing small codes and
# get the idea to implement the same'

"""
We knows Linked list contains the Node and the next nodes value

 _______
| 1 | .-|----
|___|___|

"""

class Node:
    def __init__(self, contents=None, new=None):
        self.contents = contents
        self.new = new

    def getContents(self):
        return self.contents

    def __str__(self):
        return "Value of the Current node is  {}".format(self.contents)

def test_contents(node):
    while node:
        print node.getContents()
        print "Starting with the first value"
        node = node.new
    print "You came out !!  there is no value related to the Linked list. "


def main():
    node1 = Node('P')
    node2 = Node('Q')
    node3 = Node('R')

    node1.new = node2
    node2.new = node3

    test_contents(node1)


if __name__ == "__main__":
    main()
