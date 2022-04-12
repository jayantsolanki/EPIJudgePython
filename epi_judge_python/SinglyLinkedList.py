class SinglyListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        # Creates a placeholder for the result.
        self.head = None
	
    #  Insert new node at end position
    def insert(self, value):
        #  Create a node
        node = SinglyListNode(data = value)#create node, assign the data
        if (self.head == None):#chain it now
            #  Add first node
            self.head = node
            return
        #if list not empty
        tail = self.head#create a tracker/tail and loop through list
        #  Find last node
        while (tail.next != None):#dont use tail!=None, you need to find the last node, hence using tail.next!= None
            #  Visit to next node
            tail = tail.next
        
        #  Add node at the end position
        tail.next = node
	
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