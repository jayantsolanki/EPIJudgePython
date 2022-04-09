from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist_original(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:

    dummy_head = sublist_head = ListNode(0, L)
    for _ in range(1, start):#finding predecessor to node at start
        sublist_head = sublist_head.next

    # Reverses sublist.
    #start reversing the link from position s untill position f, then relink the node before s to node on f, and node s to node after f
    sublist_iter = sublist_head.next #getting the node at position s
    #in the end of loop sublist_head.next points to node at position f and node s (sublist_iter) points to node after f
    for _ in range(finish - start):#basically track two consecutive nodes, point the next of second node to first node, then move ahead
        temp = sublist_iter.next#getting node next to position s
        #in below code sublist_iter.next is pointing to one node ahead, temp.next point to one node behind, sublist_head.next 
        #point to temp
        #basically the loop needs to remap sublist head.next to node at f and node at s next should be mapped to node after f
        #sublist_iter moves from one node to another
        # sublist_head.next tracks the node behind temp
        sublist_iter.next, temp.next, sublist_head.next = (temp.next,
                                                           sublist_head.next,
                                                           temp)
        # so overall, sublist_iter.next move to next node, temp stores that node, temp.next point to node behind
        # that is stored in sublist_head.next, then sublist_head.next moves to temp
        # at the end of the loop next attribute of node at start (sublist_iter.next) points to node after finish
        # and next attribute of node before start(sublist_head.next) points to node at finish
    return dummy_head.next



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
