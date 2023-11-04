from typing import Optional

from list_node import ListNode
from test_framework import generic_test

"""
Write a program that computes the even-odd merge.
Consider the nodes are number from 0. 0 is even.
"""
#time is: O(n)
#leetcode: https://leetcode.com/problems/odd-even-linked-list
def even_odd_merge(L: ListNode) -> Optional[ListNode]:

    if L is None:
        return L

    even_dummy_head, odd_dummy_head = ListNode(0), ListNode(0)
    tails, turn = [even_dummy_head, odd_dummy_head], 0
    while L:#starts with even, since turn is 0 first
        tails[turn].next = L#assign odd or even
        L = L.next #move to next node in list
        tails[turn] = tails[turn].next #move to assigned node
        turn ^= 1  # Alternate between even and odd.
    tails[1].next = None#marking odd tail as none#doing this for odd, since odd go to last
    tails[0].next = odd_dummy_head.next#assigning odd to the tail of even
    return even_dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('7-10-even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
