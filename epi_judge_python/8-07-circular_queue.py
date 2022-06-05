from test_framework import generic_test
from test_framework.test_failure import TestFailure


#remember to reset head and tail if they breach the length of array
#enqueue happens using tail, dequeue happens using head
#time: dequeue is O(1), enqueue amortized time is O(1)
class Queue:

    SCALE_FACTOR = 2

    def __init__(self, capacity: int) -> None:

        self._entries = [0] * capacity
        self._head = self._tail = self._num_queue_elements = 0

    def enqueue(self, x: int) -> None:

        if self._num_queue_elements == len(self._entries):  # Needs to resize.
            # step 1. Makes the queue elements appear consecutively. Important action to do before resizing
            self._entries = (self._entries[self._head:] +
                             self._entries[:self._head])
            # Step2. Resets head and tail.
            self._head, self._tail = 0, self._num_queue_elements
            # self._entries += [0] * (len(self._entries) * Queue.SCALE_FACTOR -
            #                         len(self._entries))
            # self._entries = self._entries * 2 # this also fine
            self._entries += [0] * len(self._entries) # this too
        self._entries[self._tail] = x
        self._tail = (self._tail + 1) % len(self._entries)#interesting, makes sure if it breaches the boundary, it goes to start
        self._num_queue_elements += 1

    def dequeue(self) -> int:
        self._num_queue_elements -= 1
        result = self._entries[self._head]
        self._head = (self._head + 1) % len(self._entries)
        return result

    def size(self) -> int:

        return self._num_queue_elements

def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('8-07-circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
