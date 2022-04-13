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