'''
BST Deletion
When the node to be deleted is a leaf node(no children)
When the node to be deleted has one child
When the node to be deleted has two children

Case 1: Leaf Node
- Traverse to the node
- Remove the parent's leftChild or rightChild reference to the node
to be deleted

Case 2: Deleting a node with one child
- Traverse to the node
- Connect the deleted node's parent reference and deleted node's
child reference together

Case 3: Deleting a node with two children
- Traverse to the node
- Find the node's successor, the next greatest node value(in the
right subtree for BST maintenance)- smallest val in right subtree
- Store the successor temporarily
- Delete the successor from the tree (Case 1 or Case 2)
- Replace the node to be deleted value with the successor
