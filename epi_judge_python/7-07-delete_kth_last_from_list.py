from typing import Optional

from list_node import ListNode
from test_framework import generic_test

"""
Given a singly linked list and an integer k, write a program to remove the kth last node from the list.
In particular you cannot assume that it is possible to record the length of the list.
"""
# Assumes L has at least k nodes, deletes the k-th last node in L.
# we use two iterators to traverse the list
# first iterator is k steps ahead of second iterator, after that they advance in tandem
# when first iterator reaches the tail, the second iterator is at k+1th last node, there it can 
# delete the kth node easily
#time: O(n)
def remove_kth_last_ori(L: ListNode, k: int) -> Optional[ListNode]:

    dummy_head = ListNode(0, L)#this is an extra node, hence k + 1
    first = dummy_head.next
    for _ in range(k):#advance by k nodes
        first = first.next #after finishing it will be at k + 1 node from beginning

    second = dummy_head#important
    while first:#stop when tail reached, tail is always None
        first, second = first.next, second.next
    # second points to the (k + 1)-th last node, deletes its successor.
    second.next = second.next.next
    return dummy_head.next

#better
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    dummy_head = ListNode(0, L)
    first, second = dummy_head, dummy_head #previous code had first = dummy_head.next
    for _ in range(k):
        first = first.next
    while first.next: #now reach last node
        first, second = first.next, second.next
    # when the above loop ends, first would be last node and second will be k nodes behind first, that is second is (k+1)th last node
    second.next = second.next.next
    return dummy_head.next
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('7-07-delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
