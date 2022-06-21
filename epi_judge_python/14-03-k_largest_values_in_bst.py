from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils

"""
Write a pogram that takes as input a BST and an integer k, and returns the k largest elements in the BST in decreasing order.
Logic:
    To the inorder traversal, but in reverse, that is, first process right subtree, then root node than left subtree
Time O(h + k)
"""
def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    # TODO - you fill in here.
    result = []
    def inorder_reverse(subtree):
        if not subtree:
            return 
        else:
            inorder_reverse(subtree.right)
            if len(result) < k: #only append if length not achieved
                result.append(subtree.data) #now proceed
                # inorder_reverse(subtree.left)
            else:
                return
            inorder_reverse(subtree.left)
            
    inorder_reverse(tree)
    return result

#book method
def find_k_largest_ins_bst(tree: BstNode, k: int) -> List[int]:
    def find_k_largest_in_bst_helper(tree):
        # Perform reverse inorder traversal.
        if tree and len(k_largest_elements) < k:
            find_k_largest_in_bst_helper(tree.right)
            print(tree.data)
            if len(k_largest_elements) < k:
                k_largest_elements.append(tree.data)
                find_k_largest_in_bst_helper(tree.left)

    k_largest_elements: List[int] = []
    find_k_largest_in_bst_helper(tree)
    return k_largest_elements

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('14-03-k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
