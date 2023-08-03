from typing import Optional

from list_node import ListNode
from test_framework import generic_test

"""
Leetcode 2: https://leetcode.com/problems/add-two-numbers/
Add list based integer
Write a program which takes two single linkedList of digits and returns the list corresponding to the sum of the
integers they represent.
Note: Least significant digits comes first, unlike normal representation of a number, here it is backward
Logic:
    We mimic grade school arithmatic.  Add each digits one by one and carry over the extra
Time: O(n+m), Space: O(max(m, n)), m and n length of both linked lists
"""
def add_two_numbers(L1: ListNode, L2: ListNode) -> Optional[ListNode]:

    place_iter = dummy_head = ListNode()
    carry = 0
    while L1 or L2 or carry:
        val = carry + (L1.data if L1 else 0) + (L2.data if L2 else 0)
        L1 = L1.next if L1 else None
        L2 = L2.next if L2 else None
        place_iter.next = ListNode(val % 10)
        carry, place_iter = val // 10, place_iter.next
    return dummy_head.next

def add_two_numbers_simple(l1: ListNode, l2: ListNode) -> Optional[ListNode]:
    
    dummy_head = tail = ListNode()
    carry = 0
    while l1 or l2:
        
        val = carry + (l1.data if l1 else 0) + (l2.data if l2 else 0)
        tail.next = ListNode(val % 10)
        carry = val // 10
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        tail = tail.next
    
    if carry:
        tail.next = ListNode(carry)
    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('7-13-int_as_list_add.py',
                                       'int_as_list_add.tsv', add_two_numbers))
