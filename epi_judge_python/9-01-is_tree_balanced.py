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
#postorder needed, becasue you need to check left and right subtree, before going up
# A binary tree is balanced, if, for every node, the heights of its left and right children differ by at most 1.
#logic: so traverse in postorder, as soon as you get the false for any node, propogate that false all the way to root
# Note
#if recursive calls before conditional check, then its bottom up. If recursive call after conditional check, its top down
# post order traversal indicates bottom up, pre order traversal indicates top down
def is_balanced_binary_treed(tree: BinaryTreeNode) -> bool:

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
        # the corresponding right subtree
        if not left_result.balanced:#only run when not height balanced, else return before visting the other side
            return left_result#return false if not balanced, propogate the result to the parent

        right_result = check_balanced(tree.right)
        if not right_result.balanced:#return false if not balanced
            return right_result

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1 # you have to always pick the max height
        return BalancedStatusWithHeight(is_balanced, height)

    return check_balanced(tree).balanced
#simple one, without named tuple
def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    def check_balanced(tree):
        if not tree:
            return (True, -1)#node of leaves are always None hence set to -1
        #post order implemeentation
        left_result = check_balanced(tree.left)
        #if any left subtree is not height balanced we do not need to visit
        # he corresponding right subtree
        if not left_result[0]:#only run when not height balanced, else return before visting the other side
            return left_result#return false if not balanced, propogate the result to the parent

        right_result = check_balanced(tree.right)
        if not right_result[0]:#return false if not balanced
            return right_result

        is_balanced = abs(left_result[1] - right_result[1]) <= 1
        height = max(left_result[1], right_result[1]) + 1 # you have to always pick the max height
        return (is_balanced, height)
    return check_balanced(tree)[0]

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

# def is_full_binary_tree(tree):
#     if tree is None:#leaf nodes
#         return True

#     count = (0 if not tree.left else 1) + (0 if not tree.right else 1)
#     print(count)
#     #go down to children only if current node as 0 or 2 else return false
#     return count!= 1 and is_full_binary_tree(tree.left) and is_full_binary_tree(tree.right)
#use bfs
def is_full_binary_tree(tree):
    if not tree:
        return True
    node_deque = collections.deque([tree])#insert the root
    while node_deque:
        current_node = node_deque.popleft()
        if (not current_node.left and current_node.right) or (current_node.left and not current_node.right):#check if the current node has only one child:
            return False
        if current_node.left and current_node.right:
            node_deque.append(current_node.left)
            node_deque.append(current_node.right)
    return True



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

def is_complete_binary_tree(tree):
    if not tree:
        return True
    node_deque = collections.deque([tree])#insert the root
    while node_deque:
        current_node = node_deque.popleft()
        if (not current_node.left and current_node.right):#check if the current node has only one child:
            return False
        if current_node.left and current_node.right:
            node_deque.append(current_node.left)
            node_deque.append(current_node.right)
    return True
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
print(is_complete_binary_tree(root))
print(root)


#variant 1
"""
Note: Main root has to be part of the subtree
Write a program that returns the size of largest subtree that is complete
Complete tree: A complete binary tree is a binary tree where nodes are filled in from left to right.
A complete binary tree is a binary tree in which all the levels are completely filled 
except the last level, and all the nodes are as far left as possible
https://stackoverflow.com/questions/33842493/largest-complete-subtree-in-a-binary-tree
https://www.geeksforgeeks.org/find-the-largest-complete-subtree-in-a-given-binary-tree/
Logic: IF a node at depth L is incomplete, than it must be complete at L - 1. IF doing this in BFS
So, keep on enquing and as soon as you find anomalous node stop
"""
# return (is_complete, max_height_so_far, is_perfect)
def complete_subtree_depth(tree):
    if not tree:
        return 0
    depth = 1
    node_deque = collections.deque([(depth, tree)])#insert the root
    while node_deque:
        depth, current_node = node_deque.popleft()
        if (not current_node.left and current_node.right):#check if the current node has only one child:
            return depth
        if current_node.left and current_node.right:
            node_deque.append((depth + 1, current_node.left))
            node_deque.append((depth + 1, current_node.right))
    return depth - 1


root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.left.left.left = BinaryTreeNode(8)
root.left.left.right = BinaryTreeNode(9)
root.left.right.right = BinaryTreeNode(10)
print(complete_subtree_depth(root))
print(root)

## Variant 2 k balanced tree
"""
Return the node whose subtree is hieght balanced
"""
def is_kth_balanced_binary_tree(tree: BinaryTreeNode, k: int) -> bool:

    BalancedStatusWithHeight = collections.namedtuple(
        'BalancedStatusWithHeight', ('node', 'balanced', 'height')) # this is important

    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(node = None, balanced=True, height=-1)#children of leaves are always None hence set to -1
        #post order implemeentation
        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            return left_result

        right_result = check_balanced(tree.right)
        if not right_result.balanced:#return false if not balanced
            return right_result

        is_balanced = abs(left_result.height - right_result.height) < k#break when k value encountered
        height = max(left_result.height, right_result.height) + 1 # you have to always pick the max height
        return BalancedStatusWithHeight(tree, is_balanced, height)

    return check_balanced(tree).node.val
root = BinaryTreeNode(314)
root.left = BinaryTreeNode(6)
root.right = BinaryTreeNode(6)
root.right.left = BinaryTreeNode(2)
root.right.right = BinaryTreeNode(271)
root.left.left = BinaryTreeNode(271)
root.left.right = BinaryTreeNode(561)
root.left.left.left = BinaryTreeNode(28)
root.left.left.right = BinaryTreeNode(0)
root.left.right.right = BinaryTreeNode(3)
root.left.right.right.left = BinaryTreeNode(17)
root.right.right.right = BinaryTreeNode(28)
root.right.left.right = BinaryTreeNode(1)
root.right.left.right.left = BinaryTreeNode(401)
root.right.left.right.right = BinaryTreeNode(257)
root.right.left.right.left.right = BinaryTreeNode(641)
print(root)
print(is_kth_balanced_binary_tree(root, 3))



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('9-01-is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
