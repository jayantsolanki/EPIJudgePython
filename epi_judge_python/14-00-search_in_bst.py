from typing import Optional

# from bst_node import BstNode
from test_framework import generic_test
#time O(n)
# https://leetcode.com/problems/search-in-a-binary-search-tree/
class BstNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right

    # def __eq__(self, other):
    #     return equal_binary_trees(self, other)

    # def __repr__(self):
    #     return str(binary_tree_to_string(self))

    # def __str__(self):
    #     return self.__repr__()

def search_bst_recursion(tree: BstNode, key: int) -> Optional[BstNode]:
    if not tree:
        return None
    if key == tree.data:
        return tree
    elif key < tree.data:
        return search_bst(tree.left, key)
    else:
        return search_bst(tree.right, key)

#iterative
def search_bst(tree: BstNode, key: int) -> Optional[BstNode]:
    while tree:
        if key == tree.data:
            return tree
        elif key < tree.data:
            tree = tree.left
        else:
            tree = tree.right

def search_bst_pythonic(tree: BstNode, key: int) -> Optional[BstNode]:

    return (tree if not tree or tree.data == key else search_bst(
        tree.left, key) if key < tree.data else search_bst(tree.right, key))

def search_bst_wrapper(tree, key):
    result = search_bst(tree, key)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('14-00-search_in_bst.py', 'search_in_bst.tsv',
                                       search_bst_wrapper))
