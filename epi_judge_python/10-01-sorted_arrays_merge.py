import heapq
from typing import List, Tuple

from test_framework import generic_test

"""
    Leetcode: 23, https://leetcode.com/problems/merge-k-sorted-lists/
    logic:
    create a min heap of size of numbers of arrays
    iteratively pick first elements from each array and put into heap
    Once done, start the process of picking smallest number from heap, and replace the number lost in heap with the 
    next element of the array whose element was picked up. You can do this by using a index tracker, hence the use of 
    tuple
    Go on until heap runs out
    Time: O(nlogk), where k is the size of array count, or depth(size) of heap used
    Space: Space: O(k), size of heap used
"""
def merge_sorted_arrays_v2(sorted_arrays: List[List[int]]) -> List[int]:

    min_heap: List[Tuple[int, int]] = []
    # Builds a list of iterators for each array in sorted_arrays.
    sorted_arrays_iters = [iter(x) for x in sorted_arrays]

    # Puts first element from each iterator in min_heap.
    #awesome way to get first element from each array
    for i, it in enumerate(sorted_arrays_iters):
        first_element = next(it, None)#if out of value return None
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))

    result = []
    while min_heap:
        smallest_entry, smallest_array_i = heapq.heappop(min_heap)
        smallest_array_iter = sorted_arrays_iters[smallest_array_i]
        result.append(smallest_entry)
        next_element = next(smallest_array_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_array_i))
    return result


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    sorted_arrays_iter = [iter(i) for i in sorted_arrays]
    # creating min_heap to store the first elements from each array
    min_heap = []
    result = []

    for i, array in enumerate(sorted_arrays_iter):#getting first element from each iterator
        element = next(array, None)
        if element is not None:
            heapq.heappush(min_heap, (element, i))
    #now starting the insertion, until the heap runs out 
    while min_heap:
        smallest_element, smallest_element_index = heapq.heappop(min_heap)
        result.append(smallest_element)
        #now insert new element for repleced element, from the same iterator it was earlier taken
        next_element = next(sorted_arrays_iter[smallest_element_index], None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_element_index))
    return result

# Pythonic solution, uses the heapq.merge() method which takes multiple inputs.
def merge_sorted_arrays_pythonic(sorted_arrays):
    return list(heapq.merge(*sorted_arrays))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('10-01-sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
