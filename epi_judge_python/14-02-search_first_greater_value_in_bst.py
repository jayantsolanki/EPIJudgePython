from typing import Optional

from bst_node import BstNode
from test_framework import generic_test

"""
Find the first key greater than a given value in BST
Write a program that takes as input a BST and a value, and return the first key  that woulld appear in an inorder traversal which
is greater than the input value.
Logic:
    Use Binary Search logic, and keep updating the result with any greater value encountered.  As soon as we encounter the first
    greater value, the correct answer will be definitely wihtin that tree whose root is that greater key.
    Dont use the inorder traversal since it is not using the BST property
Time: O(h), Space is O(1)
"""
def find_first_greater_than_k(tree: BstNode, k: int) -> Optional[BstNode]:

    subtree, first_so_far = tree, None
    while subtree:
        if subtree.data > k:
            first_so_far, subtree = subtree, subtree.left
        else:  # Root and all keys in left subtree are <= k, so skip them.
            subtree = subtree.right
    return first_so_far


#variant 1
"""
Write a program that takes as input a BST and a value, and return the node whose key equals the input and appears first in inorder traversal of the BST. 
Logic: Just follow above logic
"""
def find_first_equal_to_k(tree: BstNode, k: int) -> Optional[BstNode]:

    subtree, first_so_far = tree, None
    while subtree:
        if subtree.data == k:
            first_so_far, subtree = subtree, subtree.left
        elif subtree.data > k:
            subtree = subtree.left
        else: #subtree.data < k
            subtree = subtree.right
    return first_so_far

def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            '14-02-search_first_greater_value_in_bst.py',
            'search_first_greater_value_in_bst.tsv',
            find_first_greater_than_k_wrapper))
