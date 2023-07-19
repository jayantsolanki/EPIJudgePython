# from stack_with_max import Stack
from test_framework import generic_test
from test_framework.test_failure import TestFailure
#use combination of Question 8.1 and 8.8
class Stack:#imported from Stack with Max program
    def __init__(self):
         
        # main stack
        self.mainStack = []
        # stack to keep track of
        # max element
        self.trackMaxIndex = []
        self.mainStackLen = 0

    def empty(self):
        return len(self.mainStack) == 0

    def push(self, x):
        if self.empty():#check if empty
            self.mainStack.append(x)
            self.trackMaxIndex.append(self.mainStackLen)#store the index of the array max element
            self.mainStackLen = 1
        else:
            self.mainStack.append(x)
            if(self.mainStack[self.trackMaxIndex[-1]] < x):#insert only if found new bigger element
                self.trackMaxIndex.append(self.mainStackLen)
            self.mainStackLen += 1
            
 
    def max(self):
        return self.mainStack[self.trackMaxIndex[-1]]
 
    def pop(self):
        if self.empty():#check if empty
            return
        if self.mainStackLen == self.trackMaxIndex[-1] + 1:
            self.trackMaxIndex.pop()
        self.mainStackLen -= 1
        return(self.mainStack.pop())
        
#time: O(1) amortized for all push, pop and max
class QueueWithMax:
    def __init__(self) -> None:
        self._enqueue, self._dequeue = Stack(), Stack()

    def enqueue(self, x: int) -> None:

        self._enqueue.push(x)

    def dequeue(self) -> int:

        if self._dequeue.empty():
            while not self._enqueue.empty():
                self._dequeue.push(self._enqueue.pop())
        return self._dequeue.pop()

    def max(self) -> int:

        if not self._enqueue.empty():
            return self._enqueue.max() if self._dequeue.empty() else max(
                self._enqueue.max(), self._dequeue.max())
        return self._dequeue.max()


def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('8-09-queue_with_max.py',
                                       'queue_with_max.tsv', queue_tester))
