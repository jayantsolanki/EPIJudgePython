from multiprocessing import dummy
from typing import Optional

from numpy import linspace

from list_node import ListNode
# # from sorted_lists_merge import merge_two_sorted_lists
# import importlib
# merge_two_sorted_lists = importlib.import_module("7-01-sorted_lists_merge")
# merge_two_sorted_lists = merge_two_sorted_lists.merge_two_sorted_lists
from test_framework import generic_test

"""
Implement a routine which sorts lists efficiently. It should be a stable sort that is, the relative positions of equal 
elements must remain unchanged.
"""
#first method 
"""
This is a brute force effort
We repeatedly reorder smallest nodes encountered
"""
#time O(n2), Space O(1), worst case O(n2), if whole list was reversed initially

def insertion_sort(L: ListNode) -> ListNode:
    dummy_head = ListNode(0, L)
    # The sublist consisting of nodes up to and including iter is sorted in
    # increasing order. We need to ensure that after we move to L.next this 
    # proprty continues to hold. We do this by swapping L.next with its
    # predecessors in the list till it's in the right place.

    while L and L.next:
        #first go until where incoming node is smaller than current one
        #as soon as you encounter the next node (target node) is smaller, you will try to find its correct place in the previous nodes
        #that you can do by start searching from dumm_head always, as soon as you find the node(pre.next) which is greater than target node,
        # you simply squeeze the target node before that node. Then point the L.next to target.next, and target.next to node (pre.next)
        if L.data > L.next.data:
            target, pre = L.next, dummy_head
            L.next = target.next #move the pointer to target's next node
            #below loop finds which node is greater than target node, condition makes sure that stablity is maintained, hence we omitted <=
            #start searching from beginning for node greater than target
            while pre.next.data < target.data:
                pre = pre.next
            target.next, pre.next = pre.next, target
        else:
            L = L.next
    return dummy_head.next



#method 2
"""
This is using merge sorting technique
We repeatedly reorder smallest nodes encountered
see this image https://leetcode.com/problems/sort-list/Figures/148/topDown_merge_sort.png
Time: O(nlogn), Space O(logn), stack depth
"""
def merge_two_sorted_lists(L1: Optional[ListNode], L2: Optional[ListNode]) -> Optional[ListNode]:

    # Creates a placeholder for the result.
    dummy_head = tail = ListNode()#you will use head to access the whole list
    #above is a sentinel node, removes us from the burden to check if a list is empty
    #you only move the tail, head will remain as it is, the start of the node
    while L1 and L2:#if either of these are None or become None then stop the loop
        if L1.data <= L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next#move the tail to next node

    # Appends the remaining nodes of L1 or L2
    # tail.next = L1 or L2
    if L1:
        tail.next = L1
    else:
        tail.next = L2
    return dummy_head.next
 
def stable_sort_list(L: ListNode) -> Optional[ListNode]:

    # Base cases: L is empty or a single node, nothing to do.
    if L is None or L.next is None: #if only one node left or none left
        return L

    # Find the midpoint of L using a slow and a fast pointer.
    pre_slow, slow, fast = None, L, L
    while fast and fast.next:
        pre_slow = slow
        fast, slow = fast.next.next, slow.next

    if pre_slow:
        pre_slow.next = None  # Splits the list into two equal-sized lists.
    return merge_two_sorted_lists(stable_sort_list(L), stable_sort_list(slow)) #notice the L here, it has been cut at half, slow contain
    #second half


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('13-11-sort_list.py', 'sort_list.tsv',
                                       stable_sort_list))
