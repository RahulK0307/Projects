# Implementing the Binary tree using python

class Binary_Tree():
    def __init__ (self, newNode):
        self.right = None
        self.left = None
        self.root = newNode

    def getrightNode(self):
        return self.right

    def getleftNode(self):
        return self.left

    def setrootNode(self, nodeId):
        self.root = nodeId

    def getrootNode(self):
        return self.root

    def setleftNode(self, node):
        if self.left == None:
            self.left = Binary_Tree(node)
        else:
            tree = Binary_Tree(node)
            self.left = tree
            tree.left = self.left

    def setrightNode(self, node):
        if self.right == None:
            self.right = Binary_Tree(node)
        else:
            tree = Binary_Tree(node)
            tree.right = self.right
            self.right = tree
            

    
def printTree(tree):
    if tree != None:
        printTree(tree.getleftNode())
        print(tree.getrootNode)
        printTree(tree.getrightNode())
        


if __name__ == '__main__':
    myTree = Binary_Tree('A')
    myTree.setleftNode('B')
    myTree.setrightNode('C')
    myTree.setrightNode('D')
    printTree(myTree)
