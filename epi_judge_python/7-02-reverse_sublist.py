from typing import Optional

from list_node import ListNode
from SinglyLinkedList import *
from test_framework import generic_test

# this problem is concerned with reversing a sublist within a list
#reverse a single sublist
#numbering begins from 1, do not allocate additional node
#focus on successor field which have to be updated
"""
WAP  which takes a Singly Linked List L and two integers s and f as arguments, and reverses the order of the nodes from the sth node to
fth node, inclusive. The numbering begins at 1. Do not allocate additional nodes.
https://leetcode.com/problems/reverse-linked-list-ii/ 
92. Reverse Linked List II

We identify the start of sublist  by using iteration to get the sth node and its predecessor.
Once we reach the sth node, we start the process of reversing the links and keep counting.
When we reach the fth node, we stop the reversion, and link the reverted section with unreverted section
Time: O(f)
Time complexity is dominated by the search of the fth node.
"""
def reverse_sublist_or(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:

    dummy_head = sublist_head = ListNode(0, L)
    for _ in range(1, start):#finding predecessor to node at start
        sublist_head = sublist_head.next

    # Reverses sublist.
    #start reversing the link from position s untill position f, then relink the node before s to node on f, and node s to node after f
    sublist_iter = sublist_head.next #getting the node at position s
    #in the end of loop sublist_head.next points to node at position f and node s (sublist_iter) points to node after f
    # for _ in range(start, finish): #this also works
    for _ in range(finish - start):#basically track two consecutive nodes, point the next of second node to first node, then move ahead
        #follow this analogy
        # next_temp = curr.next , curr is sublist_iter, next_temp is temp, prev is sublist_head
        # curr.next = prev
        # prev = curr
        # curr = next_temp
        temp = sublist_iter.next#getting node next to position s
        #in below code sublist_iter.next is pointing to one node ahead, temp.next point to one node behind, sublist_head.next 
        #point to temp
        #basically the loop needs to remap sublist head.next to node at f and sublist_iter.next should be mapped to node after f
        #sublist_iter.next moves from one node to another
        # sublist_head.next tracks the node behind temp
        sublist_iter.next, temp.next, sublist_head.next = (temp.next,
                                                           sublist_head.next,
                                                           temp)
        # so overall, sublist_iter.next move to next node, temp stores that node, temp.next point to node behind
        # that is stored in sublist_head.next, then sublist_head.next moves to temp
        # at the end of the loop next attribute of node at start (sublist_iter.next) points to node after finish
        # and next attribute of node before start(sublist_head.next) points to node at finish
    return dummy_head.next
#a bit simple
def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:

    dummy_head = sublist_head = ListNode(0, L)
    for _ in range(1, start):#finding predecessor to node at start
        sublist_head = sublist_head.next

    # Reverses sublist.
    #start reversing the link from position s until position f, then relink the node before s to node on f, and node s to node after f
    # sublist_iter = sublist_head.next #getting the node at position s
    #in the end of loop sublist_head.next points to node at position f and node s (sublist_iter) points to node after f
    # for _ in range(start, finish): #this also works
    # prev = sublist_head
    # prev = curr = sublist_head.next
    curr = sublist_head.next
    #idea is to get the second node and point it towards previous node, and have the sublist_head.next point towars the node after f
    for _ in range(finish - start):#basically track two consecutive nodes, point the next of second node to first node, then move ahead
        temp = curr.next
        curr.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp
        # sublist_head.next = prev
        #above or below
        #curr.next, temp.next, sublist_head.next = temp.next, sublist_head.next, temp 

    return dummy_head.next


def reverse_sublist_full(L: SinglyListNode, start: int,
                    finish: int):

    if(L is None):
        return None
    if(finish - start <= 0):
        return L
    
    dummy_head = sublist_head = SinglyListNode(0, L.head)
    for _ in range(1, start):#finding predecessor to node at start
        sublist_head = sublist_head.next

    sublist_iter = sublist_head.next #getting the node at position s
    #basically track two consecutive nodes, point the next of second node to first node, then move ahead
    for _ in range(finish - start):
        temp = sublist_iter.next#getting node next to position s

        sublist_iter.next, temp.next, sublist_head.next = (temp.next,
                                                           sublist_head.next,
                                                           temp)

    return dummy_head.next


#variant 1
"""
write a program that reverses a list
"""

def reverse_list(L: SinglyListNode):
    if(L is None):
        return None

    dummy_head = sublist_head = SinglyListNode(0, L.head)
    sublist_iter = sublist_head.next
    while(sublist_iter.next):
        temp = sublist_iter.next#getting node next to position s

        sublist_iter.next, temp.next, sublist_head.next = (temp.next,
                                                           sublist_head.next,
                                                           temp)

    return dummy_head.next
#another algo, i like this much more
def reverse(L):
    prev = None
    current = L.head
    while(current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev
#more better
def reverse_v2(head: ListNode) -> ListNode:
    current = head
    prev = None
    while current:
        current.next, current, prev= prev, current.next, current
    return prev

# variant 2
"""
https://www.geeksforgeeks.org/reverse-a-list-in-groups-of-given-size/
Write a program which takes as input a singly list L, and a nonnegative integer k, and reverses the 
list k nodes at a time. If the number of nodes n in the list is not a multiple of k,
leave the last n mod k nodes unchanged. Do not change the data stored within a node.
Logic: Basically, run the reverse sublist code with changing limits, call it repeatedly

"""
#little bit bad on time complexity
def reverse_sublist_knodes(L1, k):
    lenList = 0
    tail = L1.head
    while tail:
        lenList += 1
        tail = tail.next
    print(lenList)
    def reverse_sublist_nodes(L: SinglyListNode, start: int,
                    finish: int):

        if(L is None):
            return None
        if(finish - start <= 0):
            return L
        
        dummy_head = sublist_head = SinglyListNode(0, L)
        for _ in range(1, start):#finding predecessor to node at start
            sublist_head = sublist_head.next

        sublist_iter = sublist_head.next #getting the node at position s
        #basically track two consecutive nodes, point the next of second node to first node, then move ahead
        for _ in range(finish - start):
            temp = sublist_iter.next#getting node next to position s

            sublist_iter.next, temp.next, sublist_head.next = (temp.next,
                                                            sublist_head.next,
                                                            temp)

        return dummy_head.next
    temp = L1.head#temp will always be the same, pointing to node at kth place from left
    for i in range(1, lenList + 1 - (lenList%k), k):
        temp = reverse_sublist_nodes(temp, i, i + k - 1)#k nodes including i, hence -1
        # break
    return temp
#better, time complexity n
def reverse_sublist_knodes_variant2(L1, k):
    lenList = 0
    tail = L1
    while tail:
        lenList += 1
        tail = tail.next
    # print(lenList)
    def reverse_knodes(head, k, remainingLength):# this reverses all except the last sublist which is less than k
        
        if head == None:
            return None
        if remainingLength < k:
            return head # no need to reverse remainings
        current = head
        next = None
        prev = None
        count = 0

        # Reverse first k nodes of the linked list
        while(current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

        # next is now a pointer to (k+1)th node
        # recursively call for the list starting
        # from current. And make rest of the list as
        # next of first node
        #ater end of every looop, prev points to kth node, hence head.next should point to prev after every recursion
        if next is not None:
            # if none is returned from prev it means end of the list has been reached
            head.next = reverse_knodes(next, k, remainingLength-k)

        # prev is new head of the input list
        return prev
    return reverse_knodes(L1, k, lenList)

"""
Reverse the first sub-list of size k. While reversing keep track of the next node and previous node.
Let the pointer to the next node be next and pointer to the previous node be prev. See this post for reversing a linked list.
head->next = reverse(next, k) ( Recursively call for rest of the list and link the two sub-lists )
Return prev ( prev becomes the new head of the list (see the diagrams of an iterative method of this post )
"""
# https://pythontutor.com/visualize.html to visualize
#logic: jayant: basically you need to return the new head after reversal of each sublist in 
# the end, which in this case is the prev in subsequent recursive call, prev is return and is 
# connected to head.next, the first prev is return as head
def reverse_knodes(head, k):# this reverses all
    
    if head == None:
        return None
    current = head
    next = None
    prev = None
    count = 0

    # Reverse first k nodes of the linked list
    while(current is not None and count < k):
        next = current.next
        current.next = prev
        prev = current
        current = next
        count += 1

    # next is now a pointer to (k+1)th node
    # recursively call for the list starting
    # from current. And make rest of the list as
    # next of first node
    if next is not None:
        # if none is returned from prev it means end of the list has been reached
        head.next = reverse_knodes(next, k)

    # prev is new head of the input list
    return prev


def main_run():
    L1 = SinglyLinkedList()
    #  Insert following linked list nodes
    L1.insert(1)
    L1.insert(3)
    L1.insert(5)
    L1.insert(7)
    L1.insert(17)
    L1.insert(19)
    # L = reverse_sublist_v2(L1.head, 2, 6)
    L = reverse_list(L1) # variant 1
    # L = reverse_sublist_knodes(L1, 4)
    # L = reverse_sublist_knodes_variant2(L1.head, 35) # variant 2
    #  Display all node
    tail = L
    # print(tail.next.next.next.next.next.next.data)
    print("\n")
    while tail:
        print("  ", tail.data, end = "")
        tail = tail.next
    print("\n")

main_run()#run


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('7-02-reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
