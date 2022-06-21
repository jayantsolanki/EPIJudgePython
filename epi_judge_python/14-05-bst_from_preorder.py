from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test

"""
Check Euler Tour Algo similar to Preorder postorder and Inorder
Reconstruct a BST from preorder traversal, given that each elements are distinct.
Each BST has distinct preorder and postorder traversal. But no distinct inorder traversal (see  bst for [1, 2, 3], there are 5)
Logic:
    Using BST proprty then right subtree always greater than root and left sub tree smaller than root, partition
    the traversal array based on this this logic 
    First key always corresponds to root, then the next subsequent key which begins next to first key and ends at
    the last key less than first key, belongs to left subtree. Remaining subsequent keys (if any) will be always greater then 
    root (first key) and belong to right subtree. 
    Recursively construct the tree by working working on thise subtrees
Complexity: Time: worst O(n2), because we repeatedly have to search for the keys belonging to right subtree, 
    so in case of left skewed tree, there are none. W(n) = W(n - 1) + O(n), that solves to O(n2)
    Best case corresponds to right skewed tree, and corresponding time complexity is O(n)
    For balanced BST: B(n) = 2B(n/2) + O(n), that solves to O(nlogn), conceptually, you need to find root in middle points
    for right subtrees, which gets halved on every recursion
"""
#method 1
# problem with this approach is that we repeatedly scan same nodes multiple times
def rebuild_bst_from_preorder_ori(preorder_sequence: List[int]
                              ) -> Optional[BstNode]:

    if not preorder_sequence:
        return None

    transition_point = next(
        (i
         for i, a in enumerate(preorder_sequence) if a > preorder_sequence[0]),
        len(preorder_sequence))
    return BstNode(
        preorder_sequence[0],
        rebuild_bst_from_preorder_ori(preorder_sequence[1:transition_point]),
        rebuild_bst_from_preorder_ori(preorder_sequence[transition_point:]))

#simple way
def rebuild_bst_from_preorder_simple(preorder_sequence: List[int]
                              ) -> Optional[BstNode]:

    if not preorder_sequence: #no nodes left
        return None
    root = preorder_sequence[0]
    #now find the index of the first element which is greater than root, it will go to right subtree
    index = len(preorder_sequence) #in case no right subtree exits, then return the len(A), important
    for i, val in enumerate(preorder_sequence):
        
        if val > root: #keys are unique 
            index = i
            break
    left = rebuild_bst_from_preorder_simple(preorder_sequence[1:index])
    right = rebuild_bst_from_preorder_simple(preorder_sequence[index:])
    return BstNode(root, left, right)

rebuild_bst_from_preorder_ori([43, 23, 37, 29, 31, 41, 47, 53])


#method two
"""
We directly recuse on the array with the lower and upper constraints, this will help us to filter out elements
which doesnt belong in those subtrees.
Time: Worst case O(n)
Mentally run the following preorder example: [43, 23, 37, 29, 31, 41, 47, 53]
Tree is build from the leaves first (bottom up approach)
"""
def rebuild_bst_from_preorder(preorder_sequence: List[int]
                              ) -> Optional[BstNode]:
    def rebuild_bst_from_preorder_on_value_range(lower_bound, upper_bound):
        if root_idx[0] == len(preorder_sequence):#leaves reached
            return None
        
        root = preorder_sequence[root_idx[0]]
        if not lower_bound <= root <= upper_bound: #check if the node should belong to that subtree, if not reject
            return None
        root_idx[0] += 1 #this keeps on incrementing on every recursion call

        # Note that rebuild_bst_from_preorder_on_value_range updates root_idx[0]
        # So the order of following two calls are critical
        left_subtree = rebuild_bst_from_preorder_on_value_range(lower_bound, root)
        right_subtree = rebuild_bst_from_preorder_on_value_range(root, upper_bound)

        return BstNode(root, left_subtree, right_subtree)

    root_idx = [0] #tracks current subtree, it goes from first node to last node, globally shared with left and right subtrees
    return rebuild_bst_from_preorder_on_value_range(float('-Inf'), float('Inf'))

#variants 1:
#postorder traversal
"""
A reverse preordering is the reverse of a preordering, i.e. a list of the vertices in the opposite order of their first visit. Reverse preordering is not the same as postordering. A reverse postordering is the reverse of a postordering,
[43, 23, 37, 29, 31, 41, 47, 53] preorder
[31, 29, 41, 37, 23, 53, 47, 43] postorder
"""
# method 1
def rebuild_bst_from_postorder_simple(postorder_sequence: List[int]
                              ) -> Optional[BstNode]:

    if not postorder_sequence: #no nodes left
        return None
    root = postorder_sequence[-1]
    #now find the index of the first element which is greater than root, it will go to right subtree
    index = len(postorder_sequence) - 1 #in case no right subtree exits, then return the len(preorder_sequence)  - 1, important
    for i, val in enumerate(postorder_sequence):
        if val > root: #keys are unique 
            index = i
            break
    left = rebuild_bst_from_postorder_simple(postorder_sequence[:index]) 
    right = rebuild_bst_from_postorder_simple(postorder_sequence[index:-1])#minus 1 because you need to exclude the root
    return BstNode(root, left, right)

rebuild_bst_from_postorder_simple([31, 29, 41, 37, 23, 53, 47, 43])
#["43", "23", "47", null, "37", null, "53", "29", "41", null, null, null, "31"] preorder
# ["43", "23", "47", null, "37", null, "53", "29", "41", null, null, null, "31"] postorder

#method 2
def rebuild_bst_from_postorder(postorder_sequence: List[int]
                              ) -> Optional[BstNode]:
    def rebuild_bst_from_postorder_on_value_range(lower_bound, upper_bound):
        if root_idx[0] == -1 :#leaves reached
            return None
        
        root = postorder_sequence[root_idx[0]]
        if not lower_bound <= root <= upper_bound: #check if the node should belong to that subtree, if not reject
            return None
        root_idx[0] -= 1 #this keeps on incrementing on every recursion call

        # Note that rebuild_bst_from_postorder_on_value_range updates root_idx[0]
        # So the order of following two calls are critical
        right_subtree = rebuild_bst_from_postorder_on_value_range(root, upper_bound) #order important, since right subtree enountered first, when moving backwards
        left_subtree = rebuild_bst_from_postorder_on_value_range(lower_bound, root)

        return BstNode(root, left_subtree, right_subtree)

    root_idx = [len(postorder_sequence) - 1] #tracks current subtree, it goes from last node to first node, globally shared with left and right subtrees
    return rebuild_bst_from_postorder_on_value_range(float('-Inf'), float('Inf'))

rebuild_bst_from_postorder([31, 29, 41, 37, 23, 53, 47, 43])
#["43", "23", "47", null, "37", null, "53", "29", "41", null, null, null, "31"] #pre
#["43", "23", "47", null, "37", null, "53", "29", "41", null, null, null, "31"] #post

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('14-05-bst_from_preorder.py',
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
