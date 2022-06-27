from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
# we use tweo iterators to traverse the list
# first iterator is k steps ahead of second iterator, after that they advance in tandem
# when first iterator reaches the tail, the second iterator is at k+1 node, there it can 
# delete the kth node easily
#time: O(n)
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:

    dummy_head = ListNode(0, L)#this is an extra node, hence k + 1
    first = dummy_head.next
    for _ in range(k):#advance by k nodes
        first = first.next 

    second = dummy_head#important
    while first:#stop when tail reached, tail is always None
        first, second = first.next, second.next
    # second points to the (k + 1)-th last node, deletes its successor.
    second.next = second.next.next
    return dummy_head.next

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('7-07-delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
