
# Python3 program to find the maximum depth of tree
 
# A binary tree node
class BinaryTreeNode:
    def __init__(self, data = None, left = None, right = None) -> None:
        self.data = data
        self.left = left
        self.right = right
 
# Compute the "maxDepth" of a tree -- the number of nodes
# along the longest path from the root node down to the
# farthest leaf node
#The basic computation is to compute the height of the each node starting from leaves, and proceeding
# upwards.
def maxDepth(node):
    if node is None:
        return -1 ;#child of leaf is none, hence -1 for that. leaf is 0
 
    else :
 
        # Compute the depth of each subtree, done in post order
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)
 
        # Use the larger one
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1
 
 
# Driver program to test above function
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
 
 
print ("Height of tree is %d" %(maxDepth(root)))