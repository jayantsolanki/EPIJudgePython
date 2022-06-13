import functools
from typing import List

from test_framework import generic_test

"""
Wite a program which takes an array of positive integers, and retyurns the smalles number which can be 
the sum of a subset of elements of the array
Logic:
    Trick is to play with smaller arrays and check the max sum, lower bound (minimum change that can be constructed) and then go for larger
    arrays
    Remember you are tasked with finding smallest number that the sum can produce, this makes thing easy
    Sort the array first
    Let V be the total sum encounterd, and u be the next number to be checkedl
        if u <= V+ 1, add it to V and proceed for next number
        else V+ 1 is the answer
Time: O(nlogn)
"""
def smallest_nonconstructible_value(A: List[int]) -> int:

    max_constructible_value = 0
    for a in sorted(A):
        if a > max_constructible_value + 1:
            break
        max_constructible_value += a
    return max_constructible_value + 1


def smallest_nonconstructible_value_pythonic(A: List[int]) -> int:
    return functools.reduce(
        lambda max_val, a: max_val +
        (0 if a > max_val + 1 else a), sorted(A), 0) + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('13-05-smallest_nonconstructible_value.py',
                                       'smallest_nonconstructible_value.tsv',
                                       smallest_nonconstructible_value))
