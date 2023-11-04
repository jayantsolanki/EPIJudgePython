from typing import List

from test_framework import generic_test
import bisect

"""
Write a program which takes as hput two sorted arrays, and returns a new array containing elements 
that are present in both of the input arrays. The input arrays may have duplicate entries, 
but the returned array should be free of duplicates.
For example, the input is <2,3,3,5,5,6,7,7,8,12> and (5,5,6,8 ,8,9,70,10), your output should be (5, 6, 8).
https://leetcode.com/problems/intersection-of-three-sorted-arrays/solution/
1213. Intersection of Three Sorted Arrays

https://leetcode.com/problems/intersection-of-two-arrays-ii/
350. Intersection of Two Arrays II
"""

#this one has  Time complexity O(mn)
def intersect_two_sorted_arrays_one(A: List[int], B: List[int]) -> List[int]:

    return [a for i, a in enumerate(A) if (i == 0 or a != A[i - 1]) and a in B]

#practice above
def intersect_two_sorted_arrays_one_prac(A: List[int], B: List[int]) -> List[int]:
    result = []

    for index, val in enumerate(A):
        #shortcircuiting with OR so that no need to check for duplicate
        if (index == 0 or A[index - 1] != A[index]) and val in B: 
            #at index ==- 0
            result.append(val)
    return result

#version 2:
"""
This one iterates in one array that is shorter and does the binary search in other array to find the common elements
Time: O(nlogm), m is longer
"""
def intersect_two_sorted_arrays_two(A: List[int], B: List[int]) -> List[int]:
    result = []
    def present(k, arr):
        index = bisect.bisect_left(arr, k)
        return index < len(arr) and arr[index] == k
    if len(A) < len(B):
        for i, val in enumerate(A):
            if (i == 0 or A[i-1] != A[i] )and present(val, B):
                result.append(val)
    else:
        for i, val in enumerate(B):
            if (i == 0 or B[i-1] != B[i] )and present(val, A):
                result.append(val)
    return result

#version 3
"""
This strives for nearly a linear runtime, provided that both arrays' length are similar
Logic:
    Move together in both arrays
    If element present in both, check if not duplicate, then add it
    if one array has next element lesser in value to other array, move to next element in the former array, 
    do vice versa

Time: O(m + n)
"""

def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    result, i, j = [], 0, 0

    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            #check for duplicate
            if i == 0 or A[i] != A[i - 1]:
            # if i == 0 or len(result) == 0 or A[i] != result[-1]:
                result.append(A[i])
            i += 1 #imp
            j += 1 #imp
        elif A[i] < B[j]:
            i += 1
        else: #A[i] > B[j]
            j += 1
    return result
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('13-01-intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
