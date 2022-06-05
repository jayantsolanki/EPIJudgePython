# from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from binarytree import Node
BinaryTreeNode = Node #creating synonym

#no need to create mirror tree, just find out that the subtreees are mirror or not
# as soon as one fails exit
#time : O(n), space O(h)
#logic BFS aka level order traversal
def is_symmetric(tree: BinaryTreeNode) -> bool:
    def check_symmetric(subtree_0, subtree_1):
        if not subtree_0 and not subtree_1:
            return True
        elif subtree_0 and subtree_1:
            return (subtree_0.data == subtree_1.data
                    and check_symmetric(subtree_0.left, subtree_1.right)
                    and check_symmetric(subtree_0.right, subtree_1.left))
        # One subtree is empty, and the other is not.
        return False

    return not tree or check_symmetric(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('9-02-is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
