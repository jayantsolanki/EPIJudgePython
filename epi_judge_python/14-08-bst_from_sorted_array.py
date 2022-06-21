import functools
from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test
from test_framework.binary_tree_utils import (binary_tree_height,
                                              generate_inorder)
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

"""
Build a balanced (min height) BST from a sorted array
Logic:
    Always pic the middle as the root and recurse on the subtrees
Time: O(n), any ways you are going to visit all the nodes
Space O(logn)
"""
def build_min_height_bst_from_sorted_array_ori(A: List[int]) -> Optional[BstNode]:
    def build_min_height_bst_from_sorted_subarray(start, end):
        if start >= end: #important
            return None
        # mid = (start + end) // 2
        mid = start  + (end - start) // 2 #use this to prevent overflow 
        return BstNode(A[mid],
                       build_min_height_bst_from_sorted_subarray(start, mid),
                       build_min_height_bst_from_sorted_subarray(mid + 1, end))

    return build_min_height_bst_from_sorted_subarray(0, len(A))

#other version, more undersandable, since using mid -1 and mid + 1
def build_min_height_bst_from_sorted_array(A: List[int]) -> Optional[BstNode]:
    def build_min_height_bst_from_sorted_subarray(start, end):
        if start > end: #important
            return None
        # mid = (start + end) // 2
        mid = start  + (end - start) // 2 #use this to prevent overflow 
        left = build_min_height_bst_from_sorted_subarray(start, mid - 1)
        right = build_min_height_bst_from_sorted_subarray(mid + 1, end)
        return BstNode(A[mid], left, right)

    return build_min_height_bst_from_sorted_subarray(0, len(A) - 1)


@enable_executor_hook
def build_min_height_bst_from_sorted_array_wrapper(executor, A):
    result = executor.run(
        functools.partial(build_min_height_bst_from_sorted_array, A))

    if generate_inorder(result) != A:
        raise TestFailure('Result binary tree mismatches input array')
    return binary_tree_height(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            '14-08-bst_from_sorted_array.py', 'bst_from_sorted_array.tsv',
            build_min_height_bst_from_sorted_array_wrapper))
