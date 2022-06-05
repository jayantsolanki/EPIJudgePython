import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
# Easy heuristic:

# if you discard mid for the next iteration (i.e. l = mid+1 or r = mid-1) then use while (l <= r).
# if you keep mid for the next iteration (i.e. l = mid or r = mid) then use while (l < r)
# https://leetcode.com/problems/single-element-in-a-sorted-array/solution/1155561

# Another

# if you are returning from inside the loop, use left <= right
# if you are reducing the search space, use left < right and finally return a[left]
# https://leetcode.com/problems/single-element-in-a-sorted-array/solution/670414

"""
Design an algo which returns the index i where i == A[i], provided that A is a sorted array of distinct numbers
If there are multiple same A[i] == i, just return one
Logic:
    Use binary search
    Lok for boundaries A[i] > i and A[i] < i. Only search withinn this boundaries
    Alternatively, calculate a secondary array whose elements are A[i] - i and and check for zeroes.
    difference will be always increasing or at worst may remain same, since array is sorted.
Time: O(logn)
"""
# https://leetcode.com/problems/fixed-point/solution/
def search_entry_equal_to_its_index_v2(A: List[int]) -> int:

    left, right = 0, len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        difference = A[mid] - mid
        # A[mid] == mid if and only if difference == 0.
        if difference == 0:
            return mid
        elif difference > 0:#go towards lesser,, its like finding minima
            right = mid - 1
        else:  # difference < 0.
            left = mid + 1
    return -1

def search_entry_equal_to_its_index(A: List[int]) -> int:
    left, mid, right = 0, 0, len(A) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if (A[mid] - mid) == 0:
            return mid
        elif (A[mid] - mid) > 0:#A[i] > i
            right = mid - 1
        else:
            left = mid + 1
    return -1 

# variant 1
"""
Attempt above problem provided that array is sorted and may contain duplicates
"""
"""
https://www.geeksforgeeks.org/find-fixed-point-array-duplicates-allowed/
https://stackoverflow.com/questions/42599946/finding-ai-i-in-a-sorted-array-with-duplicates
The general pattern is that we compare mid Index and midValue for equality first. Then, if they are not equal, we recursively search the left and right sides as follows: 
#we just search in both side, and short circuit the right search if element found in left
Time Complexity : O(logn),  this problem has no sublinear-time algorithm, worst case O(n)
"""
def search_entry_equal_to_its_index_duplicates(A: List[int]) -> int:
    left, right = 0, len(A) - 1
    def binarySearch(A, left, right):
        if (right < left):
            return -1
        mid = left + (right - left) // 2
   
        if (mid == A[mid]):
            return mid

        # Search left
        #leftindex = min(mid - 1, A[mid])#if moving towards left, either the element left to A[mid] will remain same or decrease, 
        #hence pick min
        #this also work
        left = binarySearch(A, left, mid - 1) # A[mid] - mid < 0 or A[mid] < mid
    
        if (left >= 0):#shortcircuit
            return left
    
        # Search right
        #rightindex = max(mid + 1, A[mid])
        right = binarySearch(A, mid + 1, right) # A[mid] - mid > 0 or A[mid] > mid
    
        return right
    return binarySearch(A, left, right)
search_entry_equal_to_its_index_duplicates([-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13])
search_entry_equal_to_its_index_duplicates([-2, 0, 1, 4, 4, 6, 7, 9])
search_entry_equal_to_its_index_duplicates([-2, 0, 4, 4, 6, 7, 7, 7, 9])
#                                          [-2, -1, 2, 1, 2, 2, 1, 0, 1]

@enable_executor_hook
def search_entry_equal_to_its_index_wrapper(executor, A):
    result = executor.run(functools.partial(search_entry_equal_to_its_index,
                                            A))
    if result != -1:
        if A[result] != result:
            raise TestFailure('Entry does not equal to its index')
    else:
        if any(i == a for i, a in enumerate(A)):
            raise TestFailure('There are entries which equal to its index')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            '11-02-search_entry_equal_to_index.py',
            'search_entry_equal_to_index.tsv',
            search_entry_equal_to_its_index_wrapper))
