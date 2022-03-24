import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName, TestFailure
from test_framework.test_utils import enable_executor_hook
'''
Array Alternation:
A[0]<=A[2]>=A[3]<=A[4]>=A[5]<=A[6]
'''
#iterating thorugh the array and swapping A[i] and A[i+1] when i is even and A[i] > A[i+1]
# or i is odd and A[i] < A[i+1]
def rearrange(A: List[int]) -> None:
    for i in range(len(A)):
        A[i:i+2] = sorted(A[i:i+2], reverse = bool(i%2))
    return 

"""
Another way, i like this more
The idea is to start from the second array element and increment the index by 2 for each loop’s iteration. 
If the last element is greater than the current element, swap the elements. Similarly, 
if the next element is greater than the current element, swap both elements. 
At the end of the loop, we will get the desired array that satisfies given constraints
Basically you are comparing a triplet, center element has to be greater than left or right side
a<=b>=c<=d>=e<=f
lets say d is not > c, but since c is already <b, swapping c with d wont break comparison with b
O(n)
"""
# Function to rearrange the list such that every second element
# of the list is greater than its left and right elements
def rearrangeArray(A):
    # start from the second element and increment index
    # by 2 for each iteration of the loop
    for i in range(1, len(A), 2):
 
        # if the previous element is greater than the current element,
        # swap the elements
        if A[i - 1] > A[i]:
            A[i-1], A[i] = A[i], A[i-1]
 
        # if the next element is greater than the current element,
        # swap the elements
        if i + 1 < len(A) and A[i + 1] > A[i]:
            A[i+1], A[i] = A[i], A[i+1]
    # print(A)

rearrangeArray([9, 6, 8, 3, 7])
rearrangeArray([5,6,4,7,1,5])

#sorting and then swapping each pair, O(nlogn)
def rearrange_v2(A: List[int]) -> None:
    A.sort()
    print(A) 
    i = 0
    while i<len(A)-1:
        A[i], A[i+1] = A[i+1], A[i]
        i = i+2
    print(A)
    return 

# rearrange([1, 5, 4, 7, 1, 5, 1])
# rearrange([7, 7, 3, 1, 9, 2, 5, 6, 3])
# rearrange_OLD([7, 7, 3, 1, 9, 2, 5, 6, 3])

@enable_executor_hook
def rearrange_wrapper(executor, A):
    def check_answer(A):
        for i in range(len(A)):
            if i % 2:
                if A[i] < A[i - 1]:
                    raise TestFailure().with_property(
                        PropertyName.RESULT, A).with_mismatch_info(
                            i, 'A[{}] <= A[{}]'.format(i - 1, i),
                            '{} > {}'.format(A[i - 1], A[i]))
                if i + 1 < len(A):
                    if A[i] < A[i + 1]:
                        raise TestFailure().with_property(
                            PropertyName.RESULT, A).with_mismatch_info(
                                i, 'A[{}] >= A[{}]'.format(i, i + 1),
                                '{} < {}'.format(A[i], A[i + 1]))
            else:
                if i > 0:
                    if A[i - 1] < A[i]:
                        raise TestFailure().with_property(
                            PropertyName.RESULT, A).with_mismatch_info(
                                i, 'A[{}] >= A[{}]'.format(i - 1, i),
                                '{} < {}'.format(A[i - 1], A[i]))
                if i + 1 < len(A):
                    if A[i + 1] < A[i]:
                        raise TestFailure().with_property(
                            PropertyName.RESULT, A).with_mismatch_info(
                                i, 'A[{}] <= A[{}]'.format(i, i + 1),
                                '{} > {}'.format(A[i], A[i + 1]))

    executor.run(functools.partial(rearrange, A))
    check_answer(A)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('5-08-alternating_array.py',
                                       'alternating_array.tsv',
                                       rearrange_wrapper))
