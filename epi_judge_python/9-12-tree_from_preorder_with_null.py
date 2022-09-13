import functools
from typing import List

# from binary_tree_node import BinaryTreeNode
import importlib 
bt= importlib.import_module("9-00-tree_traversal")
BinaryTreeNode = bt.BinaryTreeNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

"""
Logic:
    recognize that first node in the sequence is the root, and the sequence  for the root's left subtree appears
    before all the nodes in the root's right subtree. It is not easy too see where the left subtree ends, but, if we solve the problem
    recursively, we can assume rthat the routine correctlty computes left subtree, which will aso tell where the right subtree begins
    To understand it better, jst mentally run example 9.5 diagram. Left tree will halt by itself
Time: O(n)
"""

def reconstruct_preorder_v2(preorder: List[int]) -> BinaryTreeNode:
    def reconstruct_preorder_helper(preorder_iter):
        subtree_key = next(preorder_iter)
        if subtree_key is None:
            return None

        # Note that reconstruct_preorder_helper updates preorder_iter. So the
        # order of following two calls are critical.
        left_subtree = reconstruct_preorder_helper(preorder_iter)
        right_subtree = reconstruct_preorder_helper(preorder_iter)
        return BinaryTreeNode(subtree_key, left_subtree, right_subtree)

    return reconstruct_preorder_helper(iter(preorder))

#a bit simple
# from binarytree import Node
# BinaryTreeNode = Node #creating synonym
def reconstruct_preorder_v3(preorder: List[int]) -> BinaryTreeNode:
    def reconstruct_preorder_helper(preorder_iter):
        subtree_key = next(preorder_iter) #using iter, interesting
        if subtree_key is None:
            return None

        # Note that reconstruct_preorder_helper updates preorder_iter. So the
        # order of following two calls are critical.
        node = BinaryTreeNode(subtree_key)
        node.left = reconstruct_preorder_helper(preorder_iter)
        node.right  = reconstruct_preorder_helper(preorder_iter)
        return node

    return reconstruct_preorder_helper(iter(preorder))

# print(reconstruct_preorder(['H', 'B', 'F', None, None, 'E', 'A', None, None, None, 'C', None, 'C', None, 'G', 'I', None, None, None]))

# this without iterator
def reconstruct_preorder_v4(preorder: List[int]) -> BinaryTreeNode:
    def reconstruct_preorder_helper(preorder_iter, index): # you need to make sure that index is kept trac, because subtrees can go deep and deep
        # subtree_key = next(preorder_iter) #using iter, interesting
        index = index + 1
        subtree_key = preorder_iter[index]
        if subtree_key is None:
            return None, index

        # Note that reconstruct_preorder_helper updates preorder_iter. So the
        # order of following two calls are critical.
        node = BinaryTreeNode(subtree_key)
        node.left, index = reconstruct_preorder_helper(preorder_iter, index)
        node.right, index  = reconstruct_preorder_helper(preorder_iter, index)
        return node, index

    return reconstruct_preorder_helper(preorder, -1)[0]
# better
def reconstruct_preorder(preorder: List[int]) -> BinaryTreeNode:
    index = -1
    def reconstruct_preorder_helper(): # you need to make sure that index is kept trac, because subtrees can go deep and deep
        nonlocal index
        index = index + 1
        # subtree_key = next(preorder_iter) #using iter, interesting
        subtree_key = preorder[index]
        if subtree_key is None:
            # index = index + 1
            return None

        # Note that reconstruct_preorder_helper updates preorder_iter. So the
        # order of following two calls are critical.
        node = BinaryTreeNode(subtree_key)
        # index = index + 1
        node.left = reconstruct_preorder_helper()
        node.right  = reconstruct_preorder_helper()
        return node
    return reconstruct_preorder_helper()


# variant 1, do it now with postorder
"""
I think you should move in reverse or use pop and start constructing right subtree first
"""
def reconstruct_postorder(postorder: List[int]) -> BinaryTreeNode:
    def reconstruct_postorder_helper(preorder_iter):
        subtree_key = preorder_iter.pop() #using iter, interesting
        if subtree_key is None:
            return None

        # Note that reconstruct_preorder_helper updates preorder_iter. So the
        # order of following two calls are critical.
        node = BinaryTreeNode(subtree_key)
        node.right  = reconstruct_postorder_helper(preorder_iter)
        node.left = reconstruct_postorder_helper(preorder_iter)
        return node

    return reconstruct_postorder_helper(postorder)

print(reconstruct_postorder([None, None, 'F', None, None, 'A', None, 'E', 'B', None, None, None, None, 'I', None, 'G', 'D', 'C', 'H']))

@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('9-12-tree_from_preorder_with_null.py',
                                       'tree_from_preorder_with_null.tsv',
                                       reconstruct_preorder_wrapper))
