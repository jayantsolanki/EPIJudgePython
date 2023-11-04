import functools
from typing import Optional
from binarytree import Node
BinaryTreeNode = Node #creating synonym
from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

"""
Given two nodes in a binary tree, design an algorithm that computes their LCA. Assume that each node has a parent pointer
"""
#logic: get to the level, after traversing the one which is already deeper, and then do tandem traversing
#leetcode https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/, 1650
#until common node found
#time O(h), space O(1)
def lca(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    def get_depth(node):
        depth = 0
        while node.parent:
            depth += 1
            node = node.parent
        return depth

    depth0, depth1 = map(get_depth, (node0, node1))# cool
    # Makes node0 as the deeper node in order to simplify the code.
    # this makes sure we use node0 in the rest of the code, see line 38
    if depth1 > depth0:
        node0, node1 = node1, node0

    # Ascends from the deeper node.
    depth_diff = abs(depth0 - depth1)
    while depth_diff:
        node0 = node0.parent
        depth_diff -= 1

    # Now ascends both nodes until we reach the LCA.
    while node0 is not node1:
        node0, node1 = node0.parent, node1.parent
    return node0

#brute force, time and space O(h)
def lca_naive(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    
    nodeMap = set ()
    while node0:
        nodeMap.add(node0)
        node0 = node0.parent
    while node1:
        if(node1 in nodeMap):
            return node1
        node1 = node1.parent
    return None


    
@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('9-04-lowest_common_ancestor_with_parent.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
