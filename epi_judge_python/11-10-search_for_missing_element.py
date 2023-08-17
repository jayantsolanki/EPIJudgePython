import collections
import functools
from typing import List
import operator

from test_framework import generic_test
from test_framework.test_failure import PropertyName

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
                                             ('duplicate', 'missing'))

"""
You are given an array of n integers between 0 , n-1 inclusive. Exactly one element appears twice, implying exactly one number between 0 to n-1 is missing from the array.
How would you compute the missing and duplicate numbers
Logic:
    If array is just missing a number then XOR can be used to find it.Similary if array is just having a duplicate, XOR can be
    used to find it.
    If we take the XOR; reduce(operator.xor, list(range(0, n))) ^ reduce(operator.xor, array) = m ^ t
    t is duplicate and m is missing
    Since m != t, there must be some bit in m ^ t which is set to 1. 
    Above fact allow us to focus on the subset of 0, n-1 integers where we can guarantee exactly one of m or t is present.
    See book for notes
Time: O(n), space O(1)
"""
def find_duplicate_missing(A: List[int]) -> DuplicateAndMissing:

    # Compute the XOR of all numbers from 0 to |A| - 1 and all entries in A.
    #miss_xor_dup = functools.reduce(lambda v, i: v ^ i[0] ^ i[1], enumerate(A),0)
    #below is also correct
    miss_xor_dup = functools.reduce(operator.xor, A) ^ functools.reduce(operator.xor, list(range(0, len(A))))
    # We need to find a bit that's set to 1 in miss_xor_dup. Such a bit must
    # exist if there is a single missing number and a single duplicated number
    # in A.
    #
    # The bit-fiddling assignment below sets all of bits in differ_bit
    # to 0 except for the least significant bit in miss_xor_dup that's 1.
    differ_bit, miss_or_dup = miss_xor_dup & (~(miss_xor_dup - 1)), 0 # to get 1st set bit from right, x & ~(x -1)
    # for i, a in enumerate(A):
    #     # Focus on entries and numbers in which the differ_bit-th bit is 1.
    #     if i & differ_bit:
    #         miss_or_dup ^= i
    #     if a & differ_bit:
    #         miss_or_dup ^= a
    #above for loop can be written as
    #get those numbers in array A whose ith bit is same as ith bit in differ_bit == 1
    for a in A:
        # Focus on entries in which the differ_bit-th bit is 1.
        if a & differ_bit:
            miss_or_dup ^= a
    #now do for all numbers, idealy range
    #get those numbers in 0 - (n-1) values whose ith bit is same as ith bit in differ_bit == 1
    for i in range(len(A)):
        if i & differ_bit:
            miss_or_dup ^= i

    # miss_or_dup is either the missing value or the duplicated entry.
    # If miss_or_dup is in A, miss_or_dup is the duplicate;
    # otherwise, miss_or_dup is the missing value.
    return (DuplicateAndMissing(miss_or_dup, miss_or_dup
                                ^ miss_xor_dup) if miss_or_dup in A else
            DuplicateAndMissing(miss_or_dup ^ miss_xor_dup, miss_or_dup))


def res_printer(prop, value):
    def fmt(x):
        return 'duplicate: {}, missing: {}'.format(x[0], x[1]) if x else None

    return fmt(value) if prop in (PropertyName.EXPECTED,
                                  PropertyName.RESULT) else value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('11-10-search_for_missing_element.py',
                                       'find_missing_and_duplicate.tsv',
                                       find_duplicate_missing,
                                       res_printer=res_printer))
