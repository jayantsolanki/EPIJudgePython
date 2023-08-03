from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# Leetcode: https://leetcode.com/problems/rotate-list/

def cyclically_right_shift_list_ori(L: ListNode, k: int) -> Optional[ListNode]:

    if L is None:
        return L

    # Computes the length of L and the tail., length is needed, top calculate k mod n
    tail, n = L, 1
    while tail.next:
        n += 1
        tail = tail.next

    k %= n
    if k == 0:
        return L

    tail.next = L  # Makes a cycle by connecting the tail to the head.
    steps_to_new_head, new_tail = n - k, tail
    while steps_to_new_head:
        steps_to_new_head -= 1
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None
    return new_head

#another way
"""
Logic:
    Since it is k right shift, 
    find the tail, it will point to head now
    find the kth last element. this will be the tail
    element next to k + 1th last element will become head
"""
def cyclically_right_shift_list_simple(L: ListNode, k: int) -> Optional[ListNode]:

    if L is None:
        return L
    tail, n = L, 1
    while tail.next:
        n += 1
        tail = tail.next

    k %= n
    if k == 0:
        return L
    it = L
    #first move the pointer forward by k steps then go in tandem in next loop
    for _ in range(k + 1):
        it = it.next
    second = L
    while it:
        it, second = it.next, second.next

    dummy_head = ListNode(0, second.next)
    second.next = None
    tail.next = L
    return dummy_head.next

#better, 24JUL2023
def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    if not L:
        return L
    dummy_head = first = second = tail = ListNode(0, L)
    n = 0
    while tail.next:
        n += 1
        tail = tail.next
    
    k %= n
    if k == 0:
        return L
    
    # now first moves by k position ahead
    for _ in range(k):
        first = first.next
    
    # now move first and second in tandem until first reaches tail ListNode
    while first.next:
        first, second = first.next, second.next
    #after end of above  loop, second is the k+1th last node
    #now sever the connect at second, rejoin head
    first.next = dummy_head.next
    dummy_head.next = second.next
    second.next = None

    return dummy_head.next




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('7-09-list_cyclic_right_shift.py',
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
