import functools
from typing import Optional
# from SinglyLinkedList import *
from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

"""
 Floyd’s Cycle-Finding Algorithm 
Write a program that takes the head of a singly linked list and returns null if there does not exist
a cycle, and returns the node at the start of the cycle in case the cycle is there

Simplest approach is to explore the nodes via a next field starting from head, and storing the visited nodes 
ian a hash table. Space complexity is O(n).
If space is an issue then go with below code
Logic: Slow iterator and fast iterator ( Floyd’s Cycle-Finding Algorithm )
https://media.geeksforgeeks.org/wp-content/cdn-uploads/20190621160855/Detect-loop-in-a-linked-list.png
Time: Let F be number of nodes to the start of the Cycle, C be the number of nodes in the Cycle, and n the total nodes. 
Then time = O(F) + O(C) = O(n) - O(F)"
For explanation https://www.geeksforgeeks.org/find-first-node-of-loop-in-a-linked-list/
"""
# Floyd’s Cycle-Finding Algorithm 
def has_cycle_original(head: ListNode) -> Optional[ListNode]:
    def cycle_len(end):#count the  number of nodes before ending up back at that node
        start, step = end, 0
        while True:
            step += 1
            start = start.next
            if start is end:
                return step

    fast = slow = head
    while fast and fast.next:#making sure fast is not None or neither fast.next is None, if None then no cycle
        slow, fast = slow.next, fast.next.next#fast makes two jumps
        if slow is fast:#reasoning: if the fast iterator jumps over the slow iterator then
            #the slow iterator will equal the fast iterator in next steps
            # Finds the start of the cycle.
            cycle_len_advanced_iter = head
            for _ in range(cycle_len(slow)):#the number of nodes in the range function
                cycle_len_advanced_iter = cycle_len_advanced_iter.next#gets the node responsible for causing the cycle
            
            it = head
            # Both iterators advance in tandem.
            while it is not cycle_len_advanced_iter:
                it = it.next
                cycle_len_advanced_iter = cycle_len_advanced_iter.next
            return it  # iter is the start of cycle.
    return None  # No cycle.

"""
https://www.geeksforgeeks.org/find-first-node-of-loop-in-a-linked-list/
1. If a loop is found, initialize a slow pointer to head, let fast pointer be at its position. 
2. Move both slow and fast pointers one node at a time. 
3. The point at which they meet is the start of the loop.
Key here is moving at twice the speed. Think ofr formula 1 track, faster car will cover race twice while slower car
covers track one time. assume m is 0, then k is also zero
m + k is always integer multiple of loop length l
m + k = intMulti*l
you can subtract k from both side to get analogy of formula one track. since equation still stands
"""
# https://www.youtube.com/watch?v=apIw0Opq5nk&ab_channel=IDeserve
def has_cycle(head: ListNode) -> Optional[ListNode]:
    fast = slow= head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:#cycle present
            #tries to find the start of the cycle
            slow = head
            #both pointers advance at the same time
            while slow is not fast:
                slow, fast = slow.next, fast.next
            return slow # slow is the start of the cycle
    return None

#brute force using hash (set)
def has_cycle_simple(head):
    s = set()
    temp = head
    while (temp):

        # If we have already has
        # this node in hashmap it
        # means their is a cycle
        # (Because we encountered
        # the node second time).
        if (id(temp) in s):#using id, since node cant be hashed
            # print(temp.data)
            return temp

        # If we are seeing the node for
        # the first time, insert it in hash
        s.add(id(temp))

        temp = temp.next
    return None

# def has_cycle(head):# it is destructive, since it starts to unravel the next
#     temp = ListNode(-100)
#     tail = head
#     while (tail):
#         print(tail.data)
#         if (tail.next == None):
#             return None
#         if(tail.next == temp):
#             return tail
#         next = tail.next
#         tail.next = temp
#         tail = next

#     return None

@enable_executor_hook
def has_cycle_wrapper(executor, head, cycle_idx):
    cycle_length = 0
    if cycle_idx != -1:
        if head is None:
            raise RuntimeError('Can\'t cycle empty list')
        cycle_start = None
        cursor = head
        while cursor.next is not None:
            if cursor.data == cycle_idx:
                cycle_start = cursor
            cursor = cursor.next
            cycle_length += 1 if cycle_start is not None else 0

        if cursor.data == cycle_idx:
            cycle_start = cursor
        if cycle_start is None:
            raise RuntimeError('Can\'t find a cycle start')
        cursor.next = cycle_start
        cycle_length += 1

    result = executor.run(functools.partial(has_cycle, head))

    if cycle_idx == -1:
        if result is not None:
            raise TestFailure('Found a non-existing cycle')
    else:
        if result is None:
            raise TestFailure('Existing cycle was not found')
        cursor = result
        while True:
            cursor = cursor.next
            cycle_length -= 1
            if cursor is None or cycle_length < 0:
                raise TestFailure(
                    'Returned node does not belong to the cycle or is not the closest node to the head'
                )
            if cursor is result:
                break

    if cycle_length != 0:
        raise TestFailure(
            'Returned node does not belong to the cycle or is not the closest node to the head'
        )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('7-03-is_list_cyclic.py',
                                       'is_list_cyclic.tsv',
                                       has_cycle_wrapper))
