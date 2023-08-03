from typing import List

# from binary_tree_with_parent_prototype import BinaryTreeNode

from binarytree import Node
BinaryTreeNode = Node #creating synonym

from test_framework import generic_test

"""
#Note that nodes have Parent field
Write a program to get inorder in constant space:
One way is to use previous program, start from the left_most node and keep calling
that program on each successive node.
Below program's logic:
    We need to know when we return to a parent if the just completed subtree was
    the parent's left child (then we need to visit the parent and then traverse the right subtree)
    or a right subtree (in which case we have completed trasversing the parent). We achieve this by recording
    the subtree's root before we move to parent. We can compare the subtree's root with the parent's left child.
"""
def inorder_traversal(tree: BinaryTreeNode) -> List[int]:

    prev, result = None, []
    while tree:
        if prev is tree.parent:
            # We came down to tree from prev.
            if tree.left:  # Keep going left.
                next = tree.left
            else:
                result.append(tree.data)
                # Done with left, so go right if right is not empty. Otherwise,
                # go up.
                next = tree.right or tree.parent#left most node can also have a right child, so we need to visit that
        elif tree.left is prev:# moved up from left side
            #inorder is like left, root, right
            # We came up to tree(parent) from its left child.
            result.append(tree.data)#puts the parent in the result
            # Done with left, so go right if right is not empty. Otherwise, go
            # up.
            next = tree.right or tree.parent
        else:  # moved up from right child
            #Done with both children, so move up.
            next = tree.parent

        prev, tree = tree, next #storing parent
    return result

#alternative solution
def inorder_traversal_alt(tree: BinaryTreeNode) -> List[int]:
    result = []
    if not tree:
        return result
    def find_successor(node: BinaryTreeNode):
        #think in terms of how an inorder works
        if node.right:#this is the first thing you should, a successor aslways belongs to right subtree
            # Successor is the leftmost element in node's right subtree.
            node = node.right
            while node.left:#check until the left node has no left child
                node = node.left
            return node
        #exceptions, in case no right child was there
        if node.parent:
            #if parent's left child is node than parent is the successor
            #else keep moving up until you find a parent which has node has its left child
            while node.parent:
                if node.parent.left is node:#keep checking if node is the left child of node.parent
                    break
                node = node.parent
        # A return value of None means node does not have successor, i.e., node is
        # the rightmost node in the tree.
        return node.parent

    while tree.left:#reach out to the leftmost child
        tree=tree.left
    while True:
        result.append(tree.data)
        successNode = find_successor(tree)
        if not successNode:
            break
        tree = successNode
    return result

"""
Variant 1, perform preorder iteratively using O(1) space
"""

def preorder_traversal(tree: BinaryTreeNode) -> List[int]:

    prev, result = None, []
    while tree:
        if prev is tree.parent:
            result.append(tree.data)
            # next = tree.left or tree.right
            # We came down to tree from prev.
            if tree.left:  # Keep going left.
                next = tree.left
            else:
                next = tree.right or tree.parent#left most node can also have a right child, so we need to visit that
        elif tree.left is prev:
            # We came up to tree(parent) from its left child.
            # result.append(tree.data)#puts the parent in the result
            # Done with left, so go right if right is not empty. Otherwise, go
            # up.
            next = tree.right or tree.parent
        else:  # Done with both children, so move up.
            next = tree.parent

        prev, tree = tree, next
    return result

"""
Variant 2, perform postorder iteratively using O(1) space
"""
#this seems wrong
def postorder_traversal_wrong(tree: BinaryTreeNode) -> List[int]:

    prev, result = None, []
    while tree:
        if prev is tree.parent:
            # next = tree.left or tree.right
            # We came down to tree from prev.
            if tree.left:  # Keep going left.
                next = tree.left
            else:
                result.append(tree.data) #this is the reason, cant add this, as I have to also checkf for right node 
                next = tree.right or tree.parent#left most node can also have a right child, so we need to visit that
        elif tree.left is prev:#
            next = tree.right or tree.parent
        else: #coming up from right
            # Done with both children, add the tree node (parent) to result and move up.
            result.append(tree.data)
            next = tree.parent
        prev, tree = tree, next
    return result

#i think this is correct, run the tree mentioned in this link:
#  https://www.geeksforgeeks.org/post-order-traversal-of-binary-tree-in-on-using-o1-space/#
# Input:   1 
#        /   \
#      2       3
#     / \     / \
#    4   5   6   7
#   / \
#  8   9
# Output: 8 9 4 5 2 6 7 3 1
def postorder_traversal(tree: BinaryTreeNode) -> List[int]:

    prev, result = None, []
    while tree:
        if tree.parent == prev:
            if tree.left:
                next = tree.left
            elif tree.right:
                next = tree.right
            else:
                result.append(tree.data)
                next = tree.parent
        elif tree.left == prev:#came from left so check right
            if tree.right:
                next = tree.right
            else:
                result.append(tree.data)
                next = tree.parent
        else:#came from tree.right
            result.append(tree.data)
            next = tree.parent        
        prev, tree = tree, next
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('9-10-tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
