import functools
from typing import List, Optional

# from binary_tree_node import BinaryTreeNode
from binarytree import Node
BinaryTreeNode = Node #creating synonym

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


#this code generates right skewed tree first, then slowly move towards left skewed
#Bottom up approach
def generate_all_binary_trees(num_nodes: int
                              ) -> List[Optional[BinaryTreeNode]]:
    print(num_nodes)
    if num_nodes == 0:  # Empty tree, add as a None.
        return [None]

    result: List[Optional[BinaryTreeNode]] = []
    for num_left_tree_nodes in range(num_nodes):
        num_right_tree_nodes = num_nodes - 1 - num_left_tree_nodes
        left_subtrees = generate_all_binary_trees(num_left_tree_nodes)
        print("left", left_subtrees)
        right_subtrees = generate_all_binary_trees(num_right_tree_nodes)
        print("right", right_subtrees)
        # Generates all combinations of left_subtrees and right_subtrees.
        result += [
            BinaryTreeNode(0, left, right) for left in left_subtrees
            for right in right_subtrees
        ]
    return result

    
generate_all_binary_trees(3)
for i in generate_all_binary_trees(2):
    print(i)

def serialize_structure(tree):
    result = []
    q = [tree]
    while q:
        a = q.pop(0)
        result.append(0 if not a else 1)
        if a:
            q.append(a.left)
            q.append(a.right)
    return result


@enable_executor_hook
def generate_all_binary_trees_wrapper(executor, num_nodes):
    result = executor.run(
        functools.partial(generate_all_binary_trees, num_nodes))

    return sorted(map(serialize_structure, result))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('15-09-enumerate_trees.py',
                                       'enumerate_trees.tsv',
                                       generate_all_binary_trees_wrapper))
