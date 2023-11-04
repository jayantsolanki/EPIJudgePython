from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure

"""
Queue insertion and deletion follows first-in, first-out semantics; stack insertion and deletion is last-in, first-out.
How would you implement a queue given a library implementing stacks?
"""
# essentialy use two stacks, one for enqueue and other for dequeue
#once dequeue stack is empty, transfer content of first stack to dequeue to stack
# this approach takes O(m) time for m operations, each element is push and popped not more then two times
class Queue:
    def __init__(self) -> None:
        self._enq: List[int] = []
        self._deq: List[int] = []

    def enqueue(self, x: int) -> None:

        self._enq.append(x)

    def dequeue(self) -> int:

        if not self._deq:#in case empty
            # Transfers the elements in _enq to _deq.
            while self._enq:#you are inserting by popping first, becasue you need to reverse
                self._deq.append(self._enq.pop())
        return self._deq.pop()


def queue_tester(ops):
    try:
        q = Queue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = Queue()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('8-08-queue_from_stacks.py',
                                       'queue_from_stacks.tsv', queue_tester))
