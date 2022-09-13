class MinHeap_recursive:
    def __init__(self,capacity):
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0
    
    def getLeftChildIndex(self,index):
        return 2 * index + 1

    def getRightChildIndex(self,index):
        return 2 * index + 2

    def getParentIndex(self,index):
        return (index - 1) // 2

    def hasLeftChild(self,index):
        return self.getLeftChildIndex(index) < self.size

    def hasRightChild(self,index):
        return self.getRightChildIndex(index) < self.size

    def hasParent(self,index):
        return self.getParentIndex(index) >= 0
    
    def leftChild(self,index):
        return self.storage[self.getLeftChildIndex(index)]
    
    def rightChild(self,index):
        return self.storage[self.getRightChildIndex(index)]
    
    def parent(self,index):
        return self.storage[self.getParentIndex(index)]
    
    def isFull(self):
        return self.size == self.capacity 

    def swap(self,index1,index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp
    
    def removeMin(self):
        if(self.size == 0):
            raise("Empty Heap")
        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.heapifyDown(0)
        return data
    
    def heapifyDown(self,index):
        smallest = index
        if(self.hasLeftChild(index) and self.storage[smallest] > self.leftChild(index)):
            smallest = self.getLeftChildIndex(index)
        if(self.hasRightChild(index) and self.storage[smallest] > self.rightChild(index)):
            smallest = self.getRightChildIndex(index)
        if(smallest != index):
            self.swap(index,smallest)
            self.heapifyDown(smallest)
    
    def insert(self,data):
        if(self.isFull()):
            raise Exception("Heap is Full")
        self.storage[self.size] = data 
        self.size += 1
        self.heapifyUp(self.size - 1)

    def heapifyUp(self,index):
        if(self.hasParent(index) and self.parent(index) > self.storage[index]): 
            self.swap(index,self.getParentIndex(index))
            self.heapifyUp(self.getParentIndex(index))



class MinHeap_iterative:
    def __init__(self,capacity):
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0
    
    def getLeftChildIndex(self,index):
        return 2 * index + 1

    def getRightChildIndex(self,index):
        return 2 * index + 2

    def getParentIndex(self,index):
        return (index - 1) // 2

    def hasLeftChild(self,index):
        return self.getLeftChildIndex(index) < self.size

    def hasRightChild(self,index):
        return self.getRightChildIndex(index) < self.size

    def hasParent(self,index):
        return self.getParentIndex(index) >= 0
    
    def leftChild(self,index):
        return self.storage[self.getLeftChildIndex(index)]
    
    def rightChild(self,index):
        return self.storage[self.getRightChildIndex(index)]
    
    def parent(self,index):
        return self.storage[self.getParentIndex(index)]
    
    def isFull(self):
        return self.size == self.capacity 

    def swap(self,index1,index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp
    
    def removeMin(self):
        if(self.size == 0):
            raise Exception("Empty Heap")
        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.heapifyDown()
        return data
    
    def heapifyDown(self):
        index = 0
        while(self.hasLeftChild(index)):
            smallerChildIndex = self.getLeftChildIndex(index)
            if(self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index)):
                smallerChildIndex = self.getRightChildIndex(index)
            if(self.storage[index] < self.storage[smallerChildIndex]):
                break
            else:
                self.swap(index,smallerChildIndex)
            index = smallerChildIndex
    
    def insert(self,data):
        if(self.isFull()):
            raise Exception("Heap is Full")
        self.storage[self.size] = data 
        self.size += 1
        self.heapifyUp()

    def heapifyUp(self):
        index = self.size - 1
        while(self.hasParent(index) and 
              self.parent(index) > self.storage[index]):
            self.swap(self.getParentIndex(index),index)
            index = self.getParentIndex(index)


import heapq
import itertools
from typing import Iterator, List
"""
Time: O(nlogk)
"""
#bootcamp for k longest strings
"""
Logic:
    How to decide which type of heap to use. When using minheap, we will need to kickout smallest string in order to make way for elements after 
    size k. Smallest string sits at the top. Where as for maxheap we will need to kick out largest string sitting at the top. Since we need to preserve largest string. We will have to use minheap
"""
def top_k(k : int, stream: Iterator[str]) -> List[str]:
    # Entries are compared by their lengths
    # Heap elements can be tuples. This is useful for assigning comparison values (such as task priorities) 
    # alongside the main record being tracked
    min_heap = [(len(s), s) for s in itertools.islice(stream, k)]
    #use below or above portion, remember to pass list as iterator first
    # min_heap = []
    # for i in range(k):
    #     s = next(stream)
    #     min_heap.append((len(s), s))
    heapq.heapify(min_heap)

    for next_string in stream:
        # Push next_string and pop the shortest string in min_heap.
        heapq.heappushpop(min_heap, (len(next_string), next_string))
        #The combined action runs more efficiently than heappush() followed by a separate call to heappop()
        # https://docs.python.org/3/library/heapq.html
    return [p[1] for p in heapq.nsmallest(k, min_heap)]
    # return [p[1] for p in min_heap]

top_k(7, iter(['jayant', 'solanki', 'dsaf', 'cvsd', 'have', 'a', 'good', 'life', 'in', 'future', 'because', 'the', 'is', 'working', 'hard']))