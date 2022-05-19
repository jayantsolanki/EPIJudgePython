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
get nodes on the path from root to leftmost leaf, and leaves in the left subtree in on traversal. After that, find leaves in right sub tree follwed by nodes from rightmost leaf to root
Time: O(n)
"""
def exterior_binary_tree(tree: BinaryTreeNode) -> List[BinaryTreeNode]:

    # Computes the nodes from the root to the leftmost leaf.
    def left_boundary(subtree):
        if not subtree or (not subtree.left and not subtree.right):#also bypass leaf
            return
        exterior.append(subtree)
        if subtree.left:
            left_boundary(subtree.left)
        else:#sometime moving left, you may find the path chanign towards rightusb c to hdmi
            left_boundary(subtree.right)

    # Computes the nodes from the rightmost leaf to the root.
    def right_boundary(subtree):
        if not subtree or (not subtree.left and not subtree.right):
            return
        if subtree.right:
            right_boundary(subtree.right)
        else:
            right_boundary(subtree.left)
        exterior.append(subtree)# this lines makes the depth first addition, last one is added once all have been added

    # Compute the leaves in left-to-right order.
    def leaves(subtree):
        if not subtree:
            return
        if not subtree.left and not subtree.right:
            exterior.append(subtree)
            return
        leaves(subtree.left)
        leaves(subtree.right)

    if not tree:
        return []

    exterior = [tree]
    left_boundary(tree.left)
    leaves(tree.left)
    leaves(tree.right)
    right_boundary(tree.right)
    return exterior


def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]



@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('9-14-tree_exterior.py', 'tree_exterior.tsv',
                                       create_output_list_wrapper))
