from typing import List

from test_framework import generic_test

"""
Leetcode: 15. 3Sum
https://leetcode.com/problems/3sum/

Three Sum problem
Design an algo that takes as input an Array and a number, and determines if there are three entries in the
array (not necessarily distinct position) which add up to the specified number.
Logic:
    First we sort the array    .
    We use two_sum method as a helper function. Idea is to lower the coun to two needed element for two sum.
    We can do this by iterating over a loop and send t - A[i] to the two_sum function. Tada!!!
Time: O(n^2)
Space: O(1) 
"""

"""
Leetcode: 167. Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Leetcode: 1. Two Sum
https://leetcode.com/problems/two-sum/
Two sum:
Logic:
    We presume the array is sorted. 
    Maintain a subarray which is guaranteed to hold a solution if it exits. This subarray is initialized to the entire array, 
    and iteratively shrunk from one side or the other. Shrinking make sure sortedness of the array. If required sum is greater 
    than A[leftmost] + A[rightmost], then we increase the index of leftmost, since thats the only way we can increase the some.
    If required sum less than  A[leftmost] + A[rightmost] then we decease the index of rightmost index.
Time: O(n)
Space: O(1)
"""
def two_sum(A, t):
    i, j = 0, len(A) - 1

    while i <= j: #we can reuse the same element twice, hence  <=
        if A[i] + A[j] == t:
            return True
        elif A[i] + A[j] < t:
            i += 1
        else:
            j -= 1

# two_sum([-2, 1, 2, 4, 7, 11], 13)

def has_three_sum(A: List[int], t: int) -> bool:
    A.sort()
    for i in range(len(A)):
        if two_sum(A, t - A[i]):
            return True
    return False

# has_three_sum([11, 2, 5, 7, 3], 21)

#variant 1
"""
Solve the problem  when three elements must be distinct.
Example:  [5, 2, 3, 4, 3] and t = 9, aceeptable answ = [2, 3, 4] or [2, 4, 3]
"""
def two_sum_distinct(A, t, l):
    i, j = 0, len(A) - 1

    while i < j: 
        if A[i] + A[j] == t and i != l and j != l:
            return True
        elif A[i] + A[j] < t:
            i += 1
        else:
            j -= 1

# two_sum([-2, 1, 2, 4, 7, 11], 13)

def has_three_sum_distinct(A: List[int], t: int) -> bool:
    A.sort()
    for i in range(len(A)):
        if two_sum_distinct(A, t - A[i], i):
            return True
    return False
has_three_sum_distinct([11, 2, 5, 7, 3], 21)
has_three_sum_distinct([5, 2, 3, 4, 3], 9)

#variant 2
"""
"""

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('17-04-three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
