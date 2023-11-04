from typing import Optional

from list_node import ListNode
from test_framework import generic_test


"""
WAP that takes as input a singly linked list of integers in sorted order, and removes duplicates from it. The list should be sorted.
Time O(n), Constant Space
"""
#https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/?envType=list&envId=9fmel2q1

#Leetcode: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
#leetcode: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

def remove_duplicates(L: ListNode) -> Optional[ListNode]:

    it = L
    while it:
        # Uses next_distinct to find the next distinct value.
        next_distinct = it.next #start from second node and see if it is same as it.data
        while next_distinct and next_distinct.data == it.data:
            next_distinct = next_distinct.next
        it.next = next_distinct
        it = next_distinct
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            '7-08-remove_duplicates_from_sorted_list.py',
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
