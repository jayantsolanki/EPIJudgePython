import collections
from typing import List

from bst_node import BstNode
from test_framework import generic_test


"""
Range lookup problem

Write a program that takes as input a BST and an interval and returns the BST keys that lie in that interval.
Logic:
    You can use brute force traversal such as inorder, postorder or rpeorder, and get the values in O(n) time, but
    this doesnt exploit the BST proprties.

    Use BST property to trim down the traversal
    -   if root is less then left endpoint then the left subtree of that root wont contain any elements for that interval
    -   if root > right endpoint, than right subtree out of scope
    -   otherwise root holds a key, and it is possible for both left and right subtree to contains values that lie in
        the given interval
Time: O(m + h), m is numbers of keys in the interval found, and h is the depth of tree. You can say that max it will go the 
depth of h to find the min and max, then findout the m elements belong under the intervals
"""
Interval = collections.namedtuple('Interval', ('left', 'right'))
def range_lookup_in_bst(tree: BstNode, interval: Interval) -> List[int]:
    def range_lookup_in_bst_helper(tree):
        if tree is None:
            return

        if interval.left <= tree.data <= interval.right:
            # tree.data lies in the interval.
            #this is just like inorder
            range_lookup_in_bst_helper(tree.left)#this goes and find the minimum value then start adding it
            result.append(tree.data)
            range_lookup_in_bst_helper(tree.right)#now increment towards higher value under the interval
        elif interval.left > tree.data:
            range_lookup_in_bst_helper(tree.right)
        else:  # interval.right > tree.data
            range_lookup_in_bst_helper(tree.left)

    result: List[int] = []
    range_lookup_in_bst_helper(tree)
    return result

def range_lookup_in_bst_wrapper(tree, i):
    return range_lookup_in_bst(tree, Interval(*i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('14-10-range_lookup_in_bst.py',
                                       'range_lookup_in_bst.tsv',
                                       range_lookup_in_bst_wrapper))
