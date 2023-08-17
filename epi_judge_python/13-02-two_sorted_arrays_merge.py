from typing import List

from test_framework import generic_test

"""
Write a program which takes as inputs two sorted arrays of integers, and updates the first array to the 
combined entries of the two arrays in sorted order. Assume the first array has enough empty entries 
at its end to hold the result.
Logic:
    Start from the end, index at m + n  - 1. 
time: O(m + n)
"""
def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:

    a, b, write_idx = m - 1, n - 1, m + n - 1
    while a >= 0 and b >= 0:
        if A[a] > B[b]:
            A[write_idx] = A[a]
            a -= 1
        else:
            A[write_idx] = B[b]
            b -= 1
        write_idx -= 1
    while b >= 0:#we have assumed that array has to be stored in A
        A[write_idx] = B[b]
        write_idx, b = write_idx - 1, b - 1
    #this also same
    # if b >= 0:
    #     A[:write_idx+1] = B[:b+1]


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('13-02-two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
