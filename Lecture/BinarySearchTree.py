from TreeNode import TreeNode

class BinarySearchTree:
    def __init__(self):
        self.root = None # A BST just needs a reference to a root node
        self.size = 0 # Keeps track of number of nodes

    def length(self):
        return self.size

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
        
    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)
        
    #return payload for key if it exists
    def get(self,key):
        if self.root:
            #returns node wiht key if it exists, None otherwise
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
        
    # Used to remove Node and account for BST deletion cases
    def remove(self, currentNode):
        #Case 1: Node to remove is the leaf
        if currentNode.isLeaf():
            if currentNode == currentNode.parentleftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild - None
            
        #Case 3: Node to remove has both children
        elif currentNode.hasBothChildren():
            pass
        #Case 2: Node to remove has one child
        else:
            #Node has a leftChild
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightchild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else: #currentNode is the root
                    currentNode.replaceNodeData(currentNode.leftChild.key, currentNode.leftChild.payload, currentNode.leftChild.leftChild, currentNode.leftChild.rightChild)
            #Node has a rightChild
            else:
                if currentNode.lsleftChild():
                    currentNode.isrightChild.parent - currentNode.parent
                    currentNode.parent.leftchild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentnode.rightChild.parent - currentNode.parent
                    currentnode.parent.isrightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key, currentNode.rightChild.payload, currentNode.rightChild.leftChild, currentNode.rightChild.rightChild)
                    
    def delete(self,key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
            else:
                raise KeyError("Error, key not in tree")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
            
        else:
            raise KeyError('Error, key not in tree')

    def inOrder(self, node):
        ret = ""
        if node != None:
            ret += self.inOrder(node.leftChild)
            ret += str(node.key)
            ret += self.inOrder(node.rightChild)
        return ret

