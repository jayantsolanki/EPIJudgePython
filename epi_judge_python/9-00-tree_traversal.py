from logging import RootLogger


class BinaryTreeNode:
    def __init__(self, data = None, left = None, right = None) -> None:
        self.data = data
        self.left = left
        self.right = right

#time complexity: O(n), space O(h)
def tree_traversal(root: BinaryTreeNode):
    if root:
        # preorder: processess the root before the traversals of left and right
        #children
        print('Preorder: %d' % root.data)
        tree_traversal(root.left)
        # inorder: Processes the root after the traversal of left child 
        # and before the traversal of right child
        print('Inorder: %d' % root.data)
        tree_traversal(root.right)
        # Postorder: Processes the root after the traversals of left and right children
        print('Postorder: %d' % root.data)

## separated 
# A function to do inorder tree traversal
def printInorder(root):
 
    if root:
 
        # First recur on left child
        printInorder(root.left)
 
        # then print the data of node
        print(root.data),
 
        # now recur on right child
        printInorder(root.right)
 
 
# A function to do postorder tree traversal
def printPostorder(root):
 
    if root:
 
        # First recur on left child
        printPostorder(root.left)
 
        # the recur on right child
        printPostorder(root.right)
 
        # now print the data of node
        print(root.data),
 
 
# A function to do preorder tree traversal
def printPreorder(root):
 
    if root:
 
        # First print the data of node
        print(root.data),
 
        # Then recur on left child
        printPreorder(root.left)
 
        # Finally recur on right child
        printPreorder(root.right)

# Driver code
if __name__ == '__main__':
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    tree_traversal(root)
    print ("Preorder traversal of binary tree is")
    printPreorder(root)
    
    print ("\nInorder traversal of binary tree is")
    printInorder(root)
    
    print ("\nPostorder traversal of binary tree is")
    printPostorder(root)