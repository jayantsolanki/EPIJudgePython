import itertools
from typing import List

# from sorted_arrays_merge import merge_sorted_arrays
import importlib
ms= importlib.import_module("10-01-sorted_arrays_merge")
merge_sorted_arrays = ms.merge_sorted_arrays
from test_framework import generic_test



# design an eficient algo for sorting a k-increasing-decreasing array
"""
    logic:
    decompose the array into k sorted arrays (the decreasing ones will be reversed) and then
    use the algo from previous question to merge all those
    Time: O(nlogk)
"""
def sort_k_increasing_decreasing_array_v2(A: List[int]) -> List[int]:

    # Decomposes A into a set of sorted arrays.
    sorted_subarrays = []
    increasing, decreasing = range(2)
    subarray_type = increasing
    start_idx = 0
    for i in range(1, len(A) + 1):
        if (i == len(A) or  # A is ended. Adds the last subarray.
            (A[i - 1] < A[i] and subarray_type == decreasing) or
            (A[i - 1] >= A[i] and subarray_type == increasing)):
            sorted_subarrays.append(A[start_idx:i] if subarray_type ==
                                    increasing else A[i - 1:start_idx - 1:-1])
            start_idx = i
            subarray_type = (decreasing
                             if subarray_type == increasing else increasing)
    return merge_sorted_arrays(sorted_subarrays)

#for my simple mind
#important to take note that decreasing array needs to be reversed
def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:

    # Decomposes A into a set of sorted arrays.
    sorted_subarrays = []
    increasing, decreasing = range(2)
    subarray_type = increasing
    start_idx = 0

    for i in range(0, len(A) -1):
        if subarray_type == increasing and A[i] >= A[i + 1]:#find the boundary index where i starts to decrease
            sorted_subarrays.append(A[start_idx:i+1])
            start_idx = i + 1
            subarray_type = decreasing
        elif subarray_type == decreasing and A[i] < A[i + 1]: 
            sorted_subarrays.append(A[i:start_idx-1:-1])#store the reverse
            start_idx = i + 1
            subarray_type = increasing

    if subarray_type == increasing:
        sorted_subarrays.append(A[start_idx:]) # add the remainant
    else:      
        sorted_subarrays.append(A[len(A)-1:start_idx-1:-1]) # add the remainant
    return merge_sorted_arrays(sorted_subarrays)

# sort_k_increasing_decreasing_array([57, 131, 493, 294, 221, 339, 418, 452, 442, 190])
# sort_k_increasing_decreasing_array([57, 131, 493, 294])


# Pythonic solution, uses a stateful object to trace the monotonic subarrays.
def sort_k_increasing_decreasing_array_pythonic(A: List[int]) -> List[int]:
    class Monotonic:
        def __init__(self):
            self._last = float('-inf')

        def __call__(self, curr):
            result = curr < self._last
            self._last = curr
            return result

    return merge_sorted_arrays([
        list(group)[::-1 if is_decreasing else 1]
        for is_decreasing, group in itertools.groupby(A, Monotonic())
    ])

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('10-02-sort_increasing_decreasing_array.py',
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
