from list_node import ListNode
from test_framework import generic_test
from DoublyLinkedList import *

"""
WAP that tests wheter a singly linked list in palindromic or not.
Time: O(n) and constant space
Logic:
Traverse the list forward and backward simultaneously. Do travedrse backward, reverse half of the linked list
"""

#leetcode: https://leetcode.com/problems/palindrome-linked-list/
def reverse_list_complex(head: ListNode) -> ListNode:
    dummy = ListNode(0)
    while head:
        dummy.next, head.next, head = head, dummy.next, head.next
    return dummy.next

def reverse_list(head: ListNode) -> ListNode:
    current = head
    prev = None
    while current:
        # next = current.next
        # current.next = prev
        # prev = current
        # current = next
        # prev, current.next, current= current, prev, current.next
        current.next, current, prev= prev, current.next, current
    return prev


#time: O(n)
# get the second half, reverse it and then check it with the first half
def is_linked_list_a_palindrome(L: ListNode) -> bool:

    # Finds the second half of L.
    slow = fast = L
    while fast and fast.next:#make double jumps for fast, by the time fast.next is None, slow will be at half way
        fast, slow = fast.next.next, slow.next

    # Compares the first half and the reversed second half lists.
    first_half_iter, second_half_iter = L, reverse_list(slow)
    while second_half_iter and first_half_iter:#second portion not necessary
        if second_half_iter.data != first_half_iter.data:
            return False
        second_half_iter, first_half_iter = (second_half_iter.next,
                                             first_half_iter.next)
    return True

#variant 1
#check if double linked list is a palindrome or not
# well, get the tail then walk backwards till half way to check it

def is_doublelinked_list_a_palindrome(left):
  
    if left == None:
        return True
 
    # Find rightmost node (tail)
    right = left
    while right.next:
        right = right.next
 
    # while left != right: # this also goes till half only if node count is odd
      
    #     if left.data != right.data:
    #         return False
 
    #     left = left.next
    #     right = right.prev
    fast = left
    while fast and fast.next:#goes till half
        fast = fast.next.next
        if left.data != right.data:
            return False
 
        left = left.next
        right = right.prev
      
    return True

def main_run():
    L1 = DoublyLinkedList()
    #  Insert following linked list nodes
    # L1.insert(1)
    # L1.insert(3)
    # L1.insert(5)
    # L1.insert(3)
    # L1.insert(1)

    L1.insert(1)
    L1.insert(3)
    L1.insert(5)
    L1.insert(5)
    L1.insert(3)
    L1.insert(1)
    print(is_doublelinked_list_a_palindrome(L1.head))

main_run()#run

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('7-11-is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
