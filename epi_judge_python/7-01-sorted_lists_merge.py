from typing import Optional

from list_node import ListNode
from test_framework import generic_test

"""
Traverse the two lists, always choosing the node containing the smaller key to continue traversing
Get the sentinel tail, and start moving it based on the smallest node found
Time: O(m+n)
"""
def merge_two_sorted_lists(L1: Optional[ListNode], L2: Optional[ListNode]) -> Optional[ListNode]:

    # Creates a placeholder for the result.
    dummy_head = tail = ListNode()#you will use head to access the whole list
    #above is a sentinel node, removes us from the burden to check if a list is empty
    #you only move the tail, head will remain as it is, the start of the node
    while L1 and L2:#if either of these are None or become None then stop the loop
        if L1.data <= L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next#move the tail to next node

    # Appends the remaining nodes of L1 or L2
    # tail.next = L1 or L2
    if L1:
        tail.next = L1
    else:
        tail.next = L2
    return dummy_head.next

#full version of above including the linkedList class
class SinglyListNode:
    def __init__(self, data=0, prev = None, next=None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        # Creates a placeholder for the result.
        self.head = None
        self.tail = None
	
    #  Insert new node at end position
    def insert(self, value):
        #  Create a node
        node = SinglyListNode(data = value)#create node, assign the data
        if (self.head == None):#chain it now
            #  Add first node
            self.head = node
            self.tail = node
            return
        #if list not empty
        # tail = self.head#create a tracker/tail and loop through list
        #  Find last node
        # while (tail.next != None):#don use tail!=None, you need to find the last node, hence using tail.next!= None
        #     #  Visit to next node
        #     tail = tail.next
        self.tail.next = node
        self.tail = self.tail.next
        
        #  Add node at the end position
        # tail.next = node
	
    #  Display node element of doubly linked list
    def display(self):
        if (self.head == None):
            print("Empty Linked List")
        else :
            #  Get first node of linked list
            tail = self.head
            #  iterate linked list 
            while (tail != None):
                #  Display node value
                print("  ", tail.data, end = "")
                #  Visit to next node
                tail = tail.next
            
def merge_two_sorted_linkedlists(L1: Optional[SinglyListNode], L2: Optional[SinglyListNode]) -> Optional[SinglyListNode]:

    # Creates a placeholder for the result.
    if(L1 is None or L2 is None):
        return (L1 or L2).head
    #get first nodes of each Linked List
    L1 = L1.head
    L2 = L2.head
    
    #initial assigning of head and tail
    if(L1.data <= L2.data):
        head = tail = L1
        L1 = L1.next#move the pointer since first one has been assigned
    else:
        head = tail = L2
        L2 = L2.next#move the pointer since first one has been assigned
    
    while(L1 != None and L2!= None):#start merging
        if L1.data <= L2.data:
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L2.next
        #move the tail to next node
        tail = tail.next
    if(L1 is not None):# or just L1
        tail.next = L1
    else:
        tail.next = L2
    return head

def main_run():
    L1 = SinglyLinkedList()
    L2 = SinglyLinkedList()
    #  Insert following linked list nodes
    L1.insert(1)
    L1.insert(3)
    L1.insert(5)
    L1.insert(7)
    L1.insert(17)
    #  Insert second linked list elements
    L2.insert(2)
    L2.insert(4)
    L2.insert(64)
    L2.insert(82)
    print("Before Sorted Merge")
    #  Display all node
    print("L1 :")
    L1.display()
    print("\nL2 :")
    L2.display()
    print("\n")
    print("\n\nAfter Sorted Merge", end = "")
    L = merge_two_sorted_linkedlists(L1, L2)
    #  Display all node
    tail = L
    print("\n")
    while tail:
        print("  ", tail.data, end = "")
        tail = tail.next
    print("\n")

main_run()#run

#variant 2
"""
Merge two sorted doubly linked list
"""
#https://kalkicode.com/sorted-merge-of-two-sorted-doubly-linked-lists-in-python
class DoublyListNode:
    def __init__(self, data=0, prev = None, next=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        # Creates a placeholder for the result.
        self.head = None
	
    #  Insert new node at end position
    def insert(self, value):
        #  Create a node
        node = DoublyListNode(data = value)
        if (self.head == None):
            #  Add first node
            self.head = node
            return
        #if list not empty
        tail = self.head
        #  Find last node
        while (tail.next != None):#not tail!=None, you need to find the last node, hence using tail.next!= None
            #  Visit to next node
            tail = tail.next
        
        #  Add node at the end position
        tail.next = node
        node.prev = tail#since it is a doublelinkedList
	
    #  Display node element of doubly linked list
    def display(self):
        if (self.head == None):
            print("Empty Linked List")
        else :
            #  Get first node of linked list
            tail = self.head
            #  iterate linked list 
            while (tail != None):
                #  Display node value
                print("  ", tail.data, end = "")
                #  Visit to next node
                tail = tail.next
            
        

    #  Combine two sorted Doubly Linked List into single from sorted order
def mergeDoublyLinkedList(first=None, second=None) :
    if (first.head == None or second == None or 
        second.head == None or first.head == second.head) :
        # (head==null or second.head==null)
        #  That means one of linked list are empty
        #  when second ==null , that means invalid object
        #  when head==second.head, means same linked list object
        return (first or second).head
    
    #get first nodes of both lists
    l1 = first.head
    l2 = second.head
    tail = None
    if (l1.data > l2.data) :
        #  Decide new head
        #  In this case when need to change new head
        # self.head = l2#final result will get stored in first list
        head = tail = l2
        l2 = l2.next
    else:
        head = tail = l1
        l1 = l1.next
    
    while (l1 != None and l2 != None):#traverse until one of the linkedlist in done
        if (l1.data >= l2.data) :
            #  Add l2 node in resultant list
            # if (tail != None) :#checking so that prev can be used
            #     #  When resultant list not empty
            #     #  Add new node
            tail.next = l2
            #  connection to previous node   
            l2.prev = tail
            
            #  Visit to next node for l2
            l2 = l2.next
            #  Get new resultant node
            tail = tail.next
        else :
            #  Add l1 node in resultant list
            tail.next = l1
            #  connection to previous node   
            l1.prev = tail
            
            #  Visit to next node for l2
            l1 = l1.next
            #  Get new resultant node
            tail = tail.next

            # if (tail != None) :
            #     #  When resultant list not empty
            #     #  Add new node
            #     tail.next = l1
            #     #  connection to previous node
            #     l1.prev = tail
            
            # #  Get new resultant node
            # tail = l1
            # #  Visit to next node
            # l1 = l1.next
        
    
    if (l1 != None) :
        tail.next = l1
        l1.prev = tail
    
    if (l2 != None) :
        tail.next = l2
        l2.prev = tail
    
    return head
        
        # #  After merging delete the link to second linked list
        # second.head = None

def main() :
    dll1 = DoublyLinkedList()
    dll2 = DoublyLinkedList()
    #  Insert following linked list nodes
    dll1.insert(1)
    dll1.insert(3)
    dll1.insert(5)
    dll1.insert(7)
    dll1.insert(17)
    #  Insert second linked list elements
    dll2.insert(2)
    dll2.insert(4)
    dll2.insert(64)
    dll2.insert(82)
    print("Before Sorted Merge")
    #  Display all node
    print("dll1 :")
    dll1.display()
    print("\ndll2 :")
    dll2.display()
    print("\n\nAfter Sorted Merge", end = "")
    L = mergeDoublyLinkedList(dll1, dll2)
    #  Display all node
    tail = L
    print("\n")
    while(tail):
        print("  ", tail.data, end = "")
        tail=tail.next
    print("\n")

main()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('7-01-sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
