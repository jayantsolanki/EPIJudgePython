import functools
from typing import Optional

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, size=None):
        self.data = data
        self.left = left
        self.right = right
        self.size = size
"""
Write a prgoram to compute kth node appearing in inordeer
"""
#uses size to fine numbers of child nodes in current node
def find_kth_node_binary_tree(tree: BinaryTreeNode,
                              k: int) -> Optional[BinaryTreeNode]:

    while tree:
        left_size = tree.left.size if tree.left else 0
        if left_size + 1 < k:  # k-th node must be in right subtree of tree.
            k -= left_size + 1
            tree = tree.right
        elif left_size == k - 1:  # k-th is iter itself.
            return tree
        else:  # k-th node must be in left subtree of iter.
            tree = tree.left
    return None  # If k is between 1 and the tree size, this is unreachable.

#naive solution, doesn use size, time: O(k)
def find_kth_node_binary_tree_naive(tree: BinaryTreeNode,
                              k: int) -> Optional[BinaryTreeNode]:
    counter = 0
    in_process = [(tree, False)]#initial node
    while in_process:#run while stack is not empty
        node, children_added = in_process.pop()
        if node:
            if children_added:#if node just popped is not False then add it to result
                counter = counter + 1
                if counter == k:
                    return node
            else:
                in_process.append((node.right, False))
                in_process.append((node, True))
                in_process.append((node.left, False))
    return None

@enable_executor_hook
def find_kth_node_binary_tree_wrapper(executor, tree, k):
    def init_size(node):
        if not node:
            return 0
        node.size = 1 + init_size(node.left) + init_size(node.right)
        return node.size

    init_size(tree)

    result = executor.run(functools.partial(find_kth_node_binary_tree, tree,
                                            k))

    if not result:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('9-08-kth_node_in_tree.py',
                                       'kth_node_in_tree.tsv',
                                       find_kth_node_binary_tree_wrapper))
