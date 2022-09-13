import functools
from typing import List
# from binary_tree_node import BinaryTreeNode
import importlib 
bt= importlib.import_module("9-00-tree_traversal")
BinaryTreeNode = bt.BinaryTreeNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

"""
Leaves should appear in left to right order
#form of inorder where you only need to append the leaves
Time: O(n)
"""
def create_list_of_leaves_v2(tree: BinaryTreeNode) -> List[BinaryTreeNode]:

    if not tree:#stopper
        return []
    if not tree.left and not tree.right:#check if it is a leaf
        return [tree]
    # First do the left subtree, and then do the right subtree.
    return create_list_of_leaves(tree.left) + create_list_of_leaves(tree.right)#indirectly appending the arrays

#using a global list
def create_list_of_leaves(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    result = []
    def create_list_of_leaves(tree):
        nonlocal result
        if not tree:#stopper
            return None
        if not tree.left and not tree.right:#check if it is a leaf
            return result.append(tree)

        create_list_of_leaves(tree.left)
        create_list_of_leaves(tree.right)

    create_list_of_leaves(tree)
    return result 



@enable_executor_hook
def create_list_of_leaves_wrapper(executor, tree):
    result = executor.run(functools.partial(create_list_of_leaves, tree))

    if any(x is None for x in result):
        raise TestFailure('Result list can\'t contain None')
    return [x.data for x in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('9-13-tree_connect_leaves.py',
                                       'tree_connect_leaves.tsv',
                                       create_list_of_leaves_wrapper))
