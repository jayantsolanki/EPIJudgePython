import functools
from typing import Optional, Set

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

"""
Find lowest common ancestor using Hashtable
    Logic:
        we alternatively move from parent to parent, storing the node encounterered into the hashtable
        if before adding that node, we check its presence, if it is there, we return that as LCA
Time and Space: O(D0 + D1), D0 is number of nodes needed to reach node0 from LCA and D1 same for node1
Solution in Binary Tree chaper P4 problem is O(h) time and O(1) space, h is the depth of tree
Here we traded space for time. So this algo is only beneficial when LCA is very close to node1 and node0, else just stick
to other solution
"""
def lca(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:

    iter0, iter1 = node0, node1
    nodes_on_path_to_root: Set[BinaryTreeNode] = set() #hashtable, using set because we only need to store the key
    #not using list, because lookup will be O(n)
    while iter0 or iter1:#it will continue untill both are None
        # Ascend tree in tandem for these two nodes.
        if iter0:
            if iter0 in nodes_on_path_to_root:
                return iter0
            nodes_on_path_to_root.add(iter0)
            iter0 = iter0.parent
        if iter1:
            if iter1 in nodes_on_path_to_root:
                return iter1
            nodes_on_path_to_root.add(iter1)
            iter1 = iter1.parent
    raise ValueError('node0 and node1 are not in the same tree')
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
        generic_test.generic_test_main(
            '12-04-lowest_common_ancestor_close_ancestor.py',
            'lowest_common_ancestor.tsv', lca_wrapper))
