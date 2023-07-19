import collections
# from typing import Deque

#this implementation is done using collections
#time for enqueue and dequeue are O(1), for max O(n)
class Queue:
    def __init__(self) -> None:
        self._data = collections.deque()
        # self._data: Deque[int] = collections.deque()

    def enqueue(self, x: int) -> None:
        self._data.append(x)
    
    def dequeue(self) -> int:
        return self._data.popleft()
    
    def first(self):
        return self._data[0]

    def last(self):
        return self._data[-1]
    
    def max(self) -> int:
        return max(self._data)

ja = Queue()
ja.enqueue(1)
ja.enqueue(6)
ja.enqueue(5)
ja.enqueue(4)
ja.enqueue(2)
ja.dequeue()
print(ja)
print(ja.max())
print(ja.first())
print(ja.last())



# Python3 program to demonstrate linked list
# based implementation of queue
 
# A linked list (LL) node
# to store a queue entry
 
 
class Node:
 
    def __init__(self, data):
        self.data = data
        self.next = None
 
# A class to represent a queue
 
# The queue, front stores the front node
# of LL and rear stores the last node of LL
 
 
class LLQueue:
 
    def __init__(self):
        self.front = self.rear = None
 
    def isEmpty(self):
        return self.front == None
 
    # Method to add an item to the queue
    def EnQueue(self, item):
        temp = Node(item)
 
        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp
 
    # Method to remove an item from queue
    def DeQueue(self):
 
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next
 
        if(self.front == None):
            self.rear = None