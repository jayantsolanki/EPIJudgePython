from cmath import inf
import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName
MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))

#time is O(n) and n - 1 comparison
#remember if a < b and b < c, that means a < c, this definitely saves extra comparison
# total 3 comparsion for each iteration, and total iteration is n/2
def find_min_max(A: List[int]) -> MinMax:
    def min_max(a, b):
        return MinMax(a, b) if a < b else MinMax(b, a)

    if len(A) <= 1:
        return MinMax(A[0], A[0])

    global_min_max = min_max(A[0], A[1])
    # Process two elements at a time.
    for i in range(2, len(A) - 1, 2):#this would leave out the last element if array length is odd
        local_min_max = min_max(A[i], A[i + 1]) #comparison 1
        global_min_max = MinMax(
            min(global_min_max.smallest, local_min_max.smallest), #comparison 2
            max(global_min_max.largest, local_min_max.largest)) #comparison 3
    # If there is odd number of elements in the array, we still need to
    # compare the last element with the existing answer.
    if len(A) % 2:
        global_min_max = MinMax(min(global_min_max.smallest, A[-1]),
                                max(global_min_max.largest, A[-1]))
    return global_min_max

#this takes 2n - 1 comparisons
# , two comparisons each iteraton and total iteration n
def find_min_max_(A: List[int]) -> MinMax:
    global_min_max = MinMax(float('Inf'), float('-Inf'))
    if len(A) <= 1:
        return MinMax(A[0], A[0])
    smallest, largest = float('Inf'), A[0]
    for i in range(1, len(A)):
        if largest < A[i]:
            if smallest > largest:
                smallest = largest
            largest = A[i]
            global_min_max = MinMax(smallest, largest)
        else:
            if smallest > A[i]:
                smallest = A[i]
            global_min_max = MinMax(smallest, largest)
    return global_min_max

def res_printer(prop, value):
    def fmt(x):
        return 'min: {}, max: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('11-07-search_for_min_max_in_array.py',
                                       'search_for_min_max_in_array.tsv',
                                       find_min_max,
                                       res_printer=res_printer))
