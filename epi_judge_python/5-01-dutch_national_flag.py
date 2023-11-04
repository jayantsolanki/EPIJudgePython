import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)

#this is similar to odd-even problem we previously encountered
def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    # TODO - you fill in here.
    pivot = A[pivot_index]
    #keep the follwing invariants during partioning
    # bottom group: A[:smaller]
    # middle group: A[smaller:equal]
    # unclassified group: A[equal:larger]
    # top group: A[larger:]
    smaller, equal, larger = 0, 0, len(A)# reason we use len(A) instead of len(A) -1, 
    #because equal needs to go through all element
    # in case, for example 3, [2,1,0,5,4,3] 
    #keep iterating as long as there is an unclassified element
    #each iteration decreases the unclassifieds by one
    while equal < larger:
        # A[equal] is incoming unclassified element
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else: # A[equal] > pivot
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]
    return A


# variant 1
"""
Assuming that keys take one of the three values, reorder the array so that all three different values are grouped together.
[1,2,3,2,3,1] =  [1,1,3,3,2,2] or [1,1,2,2,3,3]
use O(n) time complexity and O(1) space
"""

def dutch_flag_partition_variant1(A):
    left, equal, right = 0, 0, len(A)
    left_element, right_element = A[left], None
    # we initialise the right element later because we dont know if there will be 
    # any element greater than middle
    while equal < right:
        # A[equal] is incoming unclassified element
        if A[equal] == left_element:
            A[left], A[equal] = A[equal], A[left]
            left, equal = left + 1, equal + 1
        # elif right_element is None or A[equal] == A[right]:
        elif right_element is None or A[equal] == right_element:
            right = right - 1
            A[right], A[equal] = A[equal], A[right]
            right_element = A[right]# this is tracking what in right
        else: 
            equal += 1
    return A

#testing
dutch_flag_partition_variant1([1,2,3,2,3,1])
dutch_flag_partition_variant1([1,2,3,1, 2, 3, 3, 2, 1, 1, 2,3,1])
dutch_flag_partition_variant1([1,1,1,1,1,2,2,2,2, 1])


#Variant 2
"""
Keys appear together
Assuming that keys take one of the 4 values ...[1,2,3,2,3,1,4, 3} =  [1,1,3,3,4,4, 2,2]
or [1,4,1,4,2,2,3,3], partition them use O(n) time complexity and O(1) space
https://gist.github.com/lopespm/81a336871ce6074f63f3cad349c3a95d
The rationale behind it is to squeeze the fourth value (middle right value) 
in between the middle-left and middle-right sub-arrays. It defines the 
values as the algorithm progresses.
"""

def dutch_flag_partition_variant2(A):
    left = A[0]
    mid_left = None
    right = None

    left_i = 0 #for tracking left element
    mid_left_i = 0
    mid_right_i = len(A)
    right_i = len(A)#counter for tracking rightmost element

    while mid_left_i < right_i and mid_left_i < mid_right_i:# first fill left, then right, 
        #then equal(third), then the fourth value
        if (A[mid_left_i] == left):#first value
            A[mid_left_i], A[left_i] = A[left_i], A[mid_left_i]
            mid_left_i += 1
            left_i += 1
        elif (right is None or A[mid_left_i] == right): #second value, mid_left_i is the 
            #counter similar to equal in previous code
            right_i -= 1
            mid_right_i = right_i#this is important, you need to squeeze 4th element between mid_right_i and right_i, 
            #hence mid_right_i will be always reseted to right_i whenever there is item ==right found
            #so mid_right_i also should move along with right_i
            A[mid_left_i], A[right_i] = A[right_i], A[mid_left_i]
            right = A[right_i]
        else:  # if it is a mid value that is neither left or right value, could be third or 4th key
            if (mid_left is None or A[mid_left_i] == mid_left):#same for third element again
                mid_left = A[mid_left_i]
                mid_left_i += 1 #similar to equal ++
            else:#4th element, the squeeze
                mid_right_i -= 1
                A[mid_left_i], A[mid_right_i] = A[mid_right_i], A[mid_left_i]
        # print(A)
        # print(left_i, mid_left_i, mid_right_i, right_i)
    return A

print(dutch_flag_partition_variant2([1,1,3,3,4,3,2,2, 4]))
print(dutch_flag_partition_variant2([1,2,3,4,2,3,1,3]))
print(dutch_flag_partition_variant2([1,2,3,4,4]))
print(dutch_flag_partition_variant2([0,1,2,5,5,2,2,0]))
print(dutch_flag_partition_variant2([0,1,1,2,5,1,5,2,2,0]))
print(dutch_flag_partition_variant2([1,0,3,0,5,5]))
print(dutch_flag_partition_variant2([1,0,3,0,0,0]))
print(dutch_flag_partition_variant2([0,0,3,0,0,0]))



# Variant 3
"""
Given array A of n objects with boolean valued keys, reorder them, such that false value appears first.
Same time complexity as above
Similar to odd-even problem
"""

def dutch_flag_partition_variant3(A):
    left, equal, right = 0, 0, len(A)
    # left_element = A[left]
    # right_element = None
    while equal < right:
        if A[equal]:#true goes to right side
            right -= 1
            A[right], A[equal] =  A[equal], A[right]
        else:
            A[left], A[equal] = A[equal], A[left]
            left, equal = left + 1, equal + 1           
    return A

#testing
dutch_flag_partition_variant3([True, True, True, False, False, False, True])
dutch_flag_partition_variant3([True, True, True, True])
dutch_flag_partition_variant3([True])
dutch_flag_partition_variant3([False])

# Variant 4

"""
Given an array A of n objects with Bool value keys, reorder, such that False appear first 
and relative ordering of objects with key true should not change
Same time and space complexity as above
https://stackoverflow.com/questions/29723998/boolean-array-reordering-in-o1-space-and-on-time
boolean array[n]; // The array
int lastTrue = n;
for (int i = n-1; i >= 0; --i) {
  if (array[i]) {
    swap(array[--lastTrue], array[i]);
  }
}
After every iteration all elements after lastTrue are true. 
No two true elements are swapped because if there was a true element between i and lastTrue 
it would have been encountered already and moved behind lastTrue
This programming is pushing False towards left, Ts order with respect to one another doesnt change
only required criteria: the relative ordering among true values to be preserved
"""
#start from right side and just move true to right side.
def dutch_flag_partition_variant4(A):
    lastTrue = len(A)#tracker for storing True moved by i
    i = len(A) - 1
    while i>=0:#have to start from the end, because I only need to push the False value towards left
        #you cannot move from index 0, since that will move true from right side to left, we want to push (not move) false from right side to left, hence decreasing order
        #just like bubble sort
        if A[i]:
            lastTrue -= 1
            A[lastTrue], A[i] =  A[i], A[lastTrue]#i is the tracker which moves towards left and sends back any True found
        i -= 1          
    return A

#another way, moving any true towards left
def dutch_flag_partition_variant4(A):
    # lastFalse = None
    lastTrue = 0
    i = 0
    while i<len(A):
        if A[i]: #look for True
            A[lastTrue], A[i] = A[i], A[lastTrue]
            lastTrue +=1
        i = i+1
  
    return A

dutch_flag_partition_variant4([True, True, True, False, False, False, True])
dutch_flag_partition_variant4([False, True, True, False, False, True, False, False, False, True])
dutch_flag_partition_variant4([True, True, True, False, True])
dutch_flag_partition_variant4([True, True, True, True])
dutch_flag_partition_variant4([False, False, False, False])
dutch_flag_partition_variant4([False, False, True, False, False])

@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('5-01-dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
