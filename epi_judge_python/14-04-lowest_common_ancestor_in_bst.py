import functools
from typing import Optional

from bst_node import BstNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

"""
Design an algo to find lowest common ancestor in a BST of the given two nodes. Assume all the keys are distinct
Rememebr an LCA in binary key has this property : s <= node <= b. s and b are two nodes and node is the LCA
So basically we strive to find this interval, by moving left or right based on the value of s and b
Exploit the property of BST
Logic:
    Let s and b the two nodes under consideration for LCA. Assume s is smaller than b. There are 4 possibilities
    1 - If the root  is one of the node than root is LCA
    2 - if s value is smaller than root, and b value is greater than root, then root is LCA
    3 - if s and b both are smaller than root, then search is left subtree of root
    4 -  if both s and b are greater than root, then search in right subtree of the root
Time: O(h), if it was not a bst, then it would have been O(n)
"""
# Input nodes are nonempty and the key at s is less than or equal to that at b.

def find_lsca(tree: BstNode, s: BstNode, b: BstNode) -> Optional[BstNode]:

    while tree.data < s.data or tree.data > b.data: #this will be false once s.data < tree.data < b.data, and that the answer
        # Keep searching since tree is outside of [s, b].
        while tree.data < s.data:
            tree = tree.right  # LCA must be in tree's right child.
        while tree.data > b.data:
            tree = tree.left  # LCA must be in tree's left child.
    # Now, s.data <= tree.data && tree.data <= b.data.
    return tree

#my take
def find_lca(tree: BstNode, s: BstNode, b: BstNode) -> Optional[BstNode]:
    if s.data > b.data:  #important
        s, b = b, s
    while True:
        if s.data <=  tree.data <= b.data:
            break
        if tree.data < s.data:
            tree = tree.right
        if tree.data > b.data:
            tree = tree.left
    return tree


@enable_executor_hook
def lca_wrapper(executor, tree, s, b):
    result = executor.run(
        functools.partial(find_lca, tree, must_find_node(tree, s),
                          must_find_node(tree, b)))
    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('14-04-lowest_common_ancestor_in_bst.py',
                                       'lowest_common_ancestor_in_bst.tsv',
                                       lca_wrapper))
