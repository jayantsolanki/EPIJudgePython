import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure

#Design a list that includes a max operation n addition to push and pop
# Max should return the max number stored in the stack
# O(1) for checking max after each push. But a bit longer for checking max after pop
# we do this; for each entry into the stack, we cache the maximum stored at or below that entry
# when we pop we evict that corresponding cached value
# sapce complexity: O(n), since we are maintaining a another stack
class StackWithMax:#original\

    ElementWithCachedMax = collections.namedtuple('ElementWithCachedMax',
                                                  ('element', 'max'))

    def __init__(self) -> None:
        # self._element_with_cached_max: List[StackWithMax.ElementWithCachedMax] = []
        self._element_with_cached_max = [] # this is also fine

    def empty(self) -> bool:

        return len(self._element_with_cached_max) == 0

    def max(self) -> int:

        return self._element_with_cached_max[-1].max

    def pop(self) -> int:

        return self._element_with_cached_max.pop().element

    def push(self, x: int) -> None:

        self._element_with_cached_max.append(
            self.ElementWithCachedMax(
                x, x if self.empty() else max(x, self.max())))
"""
Create an auxiliary stack, say ‘trackStack’ to keep the track of maximum element
Push the first element to both mainStack and the trackStack. 
 
Now from the second element, push the element to the main stack. Compare the element with the top element of the track stack, if the current element is greater than the top of trackStack then push the current element to trackStack otherwise push the top element of trackStack again into it. 
 
If we pop an element from the main stack, then pop an element from the trackStack as well. 
 
Now to compute the maximum of the main stack at any point, we can simply print the top element of Track stack. 
"""
class Stack_simple:#simple
    def __init__(self):
         
        # main stack
        self.mainStack = []
     
        # stack to keep track of
        # max element
        self.trackStack = []

    def empty(self):
        return len(self.mainStack) == 0

    def push(self, x):
        if self.empty():#check if empty
            self.mainStack.append(x)
            self.trackStack.append(x)
        else:
            self.mainStack.append(x)
            self.trackStack.append(max(x, self.trackStack[-1]))
 
    def max(self):
        return self.trackStack[-1]
 
    def pop(self):
        if self.empty():#check if empty
            return
        self.trackStack.pop()
        return(self.mainStack.pop())

# j = Stack()
# j.push(1)
# j.push(3)
# j.push(2)
# j.push(5)
# j.push(4)
# print(j.max())
# print(j.pop())
# print(j.pop())
# print(j.max())

# variant 1

"""
Can you improve on additional storeage space, if there are many duplicates
example [1,5,0,1,2,2,1,5,2,6,3,3,0,3] #only max we are caring for are 1,5,6
Logic: keep tracking the index of max element in the auxilliary array instead of storing actual element
If index of max element is not equal to index of element to be popped, then dont remove the index from aux array
"""
class Stack:#simple
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
        if self.mainStackLen == self.trackMaxIndex[-1] + 1:#update the tracker for max index, if length same as tracker's last index
            self.trackMaxIndex.pop()
        self.mainStackLen -= 1
        return(self.mainStack.pop())
j = Stack()
j.push(1)
j.push(3)
j.push(2)
j.push(5)
j.push(4)
print(j.max())
print(j.pop())
print(j.pop())
print(j.max())

def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('8-01-stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
