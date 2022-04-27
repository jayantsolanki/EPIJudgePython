# from binary_tree_node import BinaryTreeNode
import collections
from test_framework import generic_test
from binarytree import Node

# class BinaryTreeNode:
#     def __init__(self, data = None, left = None, right = None) -> None:
#         self.data = data
#         self.left = left
#         self.right = right
#using binarytree lib for visualizing the tree 

BinaryTreeNode = Node #creating synonym

#O(h) space and O(n) time
# A binary tree is balanced, if, for every node, the heights of its left and right children differ by at most 1.
#logic: so traverse in postorder, as soon as you get the false for any node, propogate that false all the way to root
def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:

    BalancedStatusWithHeight = collections.namedtuple(
        'BalancedStatusWithHeight', ('balanced', 'height')) # this is important

    # First value of the return value indicates if tree is balanced, and if
    # balanced the second value of the return value is the height of tree.
    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(balanced=True, height=-1)#node of leaves are always None hence set to -1
        #post order implemeentation
        left_result = check_balanced(tree.left)
        #if any left subtree is not height balanced we do not need to visit
        # he corresponding right subtree
        if not left_result.balanced:#only run when not height balanced, else return before visting the other side
            return left_result#return false if not balanced

        right_result = check_balanced(tree.right)
        if not right_result.balanced:#return false if not balanced
            return right_result

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1 # you have to always pick the max height
        return BalancedStatusWithHeight(is_balanced, height)

    return check_balanced(tree).balanced

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
print(is_balanced_binary_tree(root))

print(root)

#another test
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.right.left = BinaryTreeNode(3)
root.right.left.left = BinaryTreeNode(3)
root.right.left.right = BinaryTreeNode(3)
root.right.left.left.left = BinaryTreeNode(8)
root.right.left.left.right = BinaryTreeNode(9)
root.right.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
# root.left.right.left = BinaryTreeNode(11)
# root.left.right.right = BinaryTreeNode(12)
root.left.left.left = BinaryTreeNode(6)
root.left.left.right = BinaryTreeNode(7)
# root.left.left.left.left = BinaryTreeNode(8)
# root.left.left.left.right = BinaryTreeNode(9)
print(is_balanced_binary_tree(root))
print(root)


#variant 0 Full binary tree check
"""
Find if the tree is full binary or not
Definition: The tree is full if all nodes have either 0 or two children.
Logic: return 0 or 2, if 1 then not a full binary tree, exit then
Idea here is to start from root, and check if contains left and right child together or not, if not then exit
"""

def is_full_binary_tree(tree):
    if tree is None:#leaf nodes
        return True

    count = (0 if not tree.left else 1) + (0 if not tree.right else 1)
    print(count)
    #go down to children only if current node as 0 or 2 else return false
    return count!= 1 and is_full_binary_tree(tree.left) and is_full_binary_tree(tree.right)
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.left.left.left = BinaryTreeNode(8)
root.left.left.right = BinaryTreeNode(9)
# root.left.right.left = BinaryTreeNode(10)
print(is_full_binary_tree(root))
print(root)

#variant 1
"""
Write a program that returns the size of larg: est subtree that is complete
Complete tree: A complete binary tree is a binary tree where nodes are filled in from left to right.
A complete binary tree is a binary tree in which all the levels are completely filled 
except the last level, and all the nodes are as far left as possible
https://www.programiz.com/dsa/complete-binary-tree
https://www.interviewcake.com/concept/java/complete-binary-tree
Logic: Simply look for subtree where only leftmost leaves are there, and caluclate their max depth
"""
# return (is_complete, max_height_so_far, is_perfect)
def is_complete_tree(node):
    # null
    if not node:
        return (True, -1, True)

    left_subtree = is_complete_tree(node.left)
    right_subtree = is_complete_tree(node.right)

    # if any of subtrees isn't complete, current tree is not complete
    if not left_subtree[0] or not right_subtree[0]:
        return (False, max(left_subtree[1], right_subtree[1]), False)

    # if both subtrees are complete, there are 2 cases in order for current tree to be complete
    # case 1: subtrees with same height
    # left subtree must be perfect
    if left_subtree[1] == right_subtree[1] and left_subtree[2]:
        return (True, left_subtree[1] + 1, right_subtree[2])

    # case 2: left subtree taller by 1
    # right subtree must be perfect
    if left_subtree[1] == right_subtree[1] + 1 and right_subtree[2]:
        return (True, left_subtree[1] + 1, False)

    # otherwise not complete
    return (False, max(left_subtree[1], right_subtree[1]), False)

#test, below is a complete binary tree
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.left.left.left = BinaryTreeNode(8)
root.left.left.right = BinaryTreeNode(9)
root.left.right.left = BinaryTreeNode(10)
# root.left.left.left.right = BinaryTreeNode(9)
print(is_complete_tree(root))
print(root)

#test, below is not a complete binary tree
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.left.right.left = BinaryTreeNode(10)
# root.left.left.left.right = BinaryTreeNode(9)
print(is_complete_tree(root))
print(root)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('9-01-is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
