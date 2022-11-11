class TreeNode:
    def __init__(self,key,val,left=None,right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = \
                TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = \
                TreeNode(key,val,parent=currentNode)

    def descendingInOrder(self, currentNode):
        ret = []
        if currentNode != None:
            ret += self.descendingInOrder(currentNode.rightChild)
            ret += self.root
            ret += self.descendingInOrder(currentNode.leftChild)
        return ret

BST1 = BinarySearchTree()
assert BST1.descendingInOrder(BST1.root) == []
BST1.put(5, "five")
BST1.put(4, "four")
BST1.put(1, "one")
BST1.put(10, "ten")
assert BST1.descendingInOrder(BST1.root) == [10,5,4,1]
BST1.put(3, "three")
BST1.put(6, "six")
BST1.put(9, "nine")
BST1.put(12, "twelve")
BST1.put(11, "eleven")
BST1.put(13, "thirteen")
assert BST1.descendingInOrder(BST1.root) == \
        [13,12,11,10,9,6,5,4,3,1]