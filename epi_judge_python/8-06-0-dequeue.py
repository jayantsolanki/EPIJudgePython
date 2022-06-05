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
