from binarytree import Node
BinaryTreeNode = Node #creating synonym
from test_framework import generic_test

"""
we can compute the sum of all root  to leaf node as follows:
Each time visit a node, we compute the integer it encodes using the number for its prarent.
If node is a leaf, we return its integer, if it is not a leaf, we return the sum of the results from its left and right children
Time and space are O(n) and O(h)
#remember, addition will kick as soon as the leaf is encounterd, before that we will be just 
# creating the numbers
Kinda inorder traversal
"""
def sum_root_to_leaf_ori(tree: BinaryTreeNode) -> int:
    def sum_root_to_leaf_helper(tree, partial_path_sum=0):
        if not tree:
            return 0
        #creating the number
        # partial_path_sum = partial_path_sum * 2 + tree.data #or below
        partial_path_sum = (partial_path_sum << 1) | tree.data#absorb the digit from right, to create new
        if not tree.left and not tree.right:  # Leaf.
            return partial_path_sum # return number at leaf and sum those numbers at their parent
        # Non-leaf.
        return (sum_root_to_leaf_helper(tree.left, partial_path_sum) +
                sum_root_to_leaf_helper(tree.right, partial_path_sum))

    return sum_root_to_leaf_helper(tree)

#my another try
"""
idea is to reach the leaf, and pass the partially constrcuted number at every recursion.
#at the leaf, add partial sum to the final result
"""
def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    result = [0]
    def sum_root_to_leaf_helper(tree, partial_path_sum=0):
        if not tree:
            pass
        elif not tree.left and not tree.right: #leaf
            partial_path_sum = partial_path_sum * 2 + tree.data
            result[0] = result[0] + partial_path_sum
        else:
            partial_path_sum = partial_path_sum * 2 + tree.data
            sum_root_to_leaf_helper(tree.left, partial_path_sum)
            sum_root_to_leaf_helper(tree.right, partial_path_sum)

    sum_root_to_leaf_helper(tree, 0)
    return result[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('9-05-sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
