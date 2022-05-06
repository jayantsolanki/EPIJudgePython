# from binary_tree_node import BinaryTreeNode
from binarytree import Node
BinaryTreeNode = Node #creating synonym
from test_framework import generic_test


"""
traverse three trree, keeping trrack of difference of the root -to-node path sum and the target value
call this the remaining weight. As soon as we encounter a leaf and the remaining weight is equal to leaf data, we return true.
Short circuit evaluation of the check ensures that we donot processes additional leaves
"""
def has_path_sum(tree: BinaryTreeNode, remaining_weight: int) -> bool:

    if not tree:
        return False
    if not tree.left and not tree.right:  # Leaf.
        return remaining_weight == tree.data
    # Non-leaf.
    #short circuiting is done using OR, it iwill keep on travesing untill first leaf with True encountered
    return (has_path_sum(tree.left, remaining_weight - tree.data)
            or has_path_sum(tree.right, remaining_weight - tree.data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('9-06-path_sum.py', 'path_sum.tsv',
                                       has_path_sum))
