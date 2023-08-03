import functools
from typing import Optional
import collections
from binarytree import Node
BinaryTreeNode = Node #creating synonym
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# Leetcode: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
#compared to one on the leetcode, this one has O(h) space complexity. I prefer that leetcode one, but leetcode has p!=q (node0 != node1)
#below approach go for postorder, makes sense, because we need to check for both branches of a node first
#here p can be same as q
def lca_ori(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:

    Status = collections.namedtuple('Status', ('num_target_nodes', 'ancestor'))

    # Returns an object consisting of an int and a node. The int field is 0,
    # 1, or 2 depending on how many of {node0, node1} are present in tree. If
    # both are present in tree, when ancestor is assigned to a non-null value,
    # it is the LCA.
    def lca_helper(tree, node0, node1):
        if tree is None:
            return Status(num_target_nodes=0, ancestor=None)

        left_result = lca_helper(tree.left, node0, node1)
        if left_result.num_target_nodes == 2:
            # Found both nodes in the left subtree.
            return left_result
        right_result = lca_helper(tree.right, node0, node1)
        if right_result.num_target_nodes == 2:
            # Found both nodes in the right subtree.
            return right_result
        #check if left_result 0, 1, or 2, same for right_result, and also check if root(tree) is same as p or q or both
        num_target_nodes = (left_result.num_target_nodes +
                            right_result.num_target_nodes +
                            (node0, node1).count(tree)) #(node0, node1).count(tree) checks if current node (tree) is same node0 or node1 or both, if both value will be two, if with of them then 1, since node0 can be same as node1
        return Status(num_target_nodes,
                      tree if num_target_nodes == 2 else None)

    return lca_helper(tree, node0, node1).ancestor

def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:

    Status = collections.namedtuple('Status', ('num_target_nodes', 'ancestor'))

    # Returns an object consisting of an int and a node. The int field is 0,
    # 1, or 2 depending on how many of {node0, node1} are present in tree. If
    # both are present in tree, when ancestor is assigned to a non-null value,
    # it is the LCA.
    #this one allws duplicates
    def lca_helper(tree, node0, node1):
        if tree is None:
            return Status(num_target_nodes=0, ancestor=None)

        left_result = lca_helper(tree.left, node0, node1)
        if left_result.num_target_nodes >= 2:
            # Found both nodes in the left subtree.
            return left_result
        right_result = lca_helper(tree.right, node0, node1)
        if right_result.num_target_nodes >= 2:
            # Found both nodes in the right subtree.
            return right_result
        mid = node0 == tree #check if tree is same node 0 and node 1,   corner cases
        mid += node1 == tree
        num_target_nodes = mid +  left_result.num_target_nodes + right_result.num_target_nodes
        return Status(num_target_nodes,
                      tree if num_target_nodes >= 2 else None)

    return lca_helper(tree, node0, node1).ancestor


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('9-03-lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
