import typing
from typing import List
import heapq

import bintrees

from test_framework import generic_test

"""
Leetcode: 632, https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
Find the closest entries in the three sorted arrays

Observation: you cant use array value as key, since some array may have same values, hence use tuple (array_val, val_index) as key
We can also use heaop here, by finding the max on the fly

Design an algorithm that takes three sorted arrays of integers and return the length of a shorted interval that includes at least one entry from each array. A single value may be present in more that on array, but there are no duplicates within single array.
Ex: [5,10,15], [3,6,9,12,15], [8,16,24] , result = [15, 16], length = 16-15 = 1
Logic:
    The trick is to keep looking for the next smallest values in all the arrays and make combinations out of them. Smallest values will
    give you the smallest interval length.
    We fill up the the interval array with smallest picks from given arrays, finding the difference, then replacing the smallest among the element with the second smallest from same array it belonged from, reason we replace the samllest is because we want to reduce the interval distance. Repeat process until all arrays are exhausted.
    Here we need to keep track of min and max to find the interval length, using bintrees or sortedcontainers will work
Time: O(nlogk), where n is the total elements in k arrays. If k is small than O(n) overall
"""
def find_closest_elements_in_sorted_arrays_original(sorted_arrays: List[List[int]]
                                           ) -> int:
    #Reminds me of merging k sorted arrays
    # Stores array iterators in each entry.
    iters = bintrees.RBTree()
    for idx, sorted_array in enumerate(sorted_arrays):
        it = iter(sorted_array)#converting them to iterators, useful
        first_min = next(it, None)
        if first_min is not None:
            iters.insert((first_min, idx), it) #here using (first_min, idx) has tuple as key, second item 'it' is the iterator as value
            #cant use first_min alone as the key, since two array may have same values, hence we use idx too.
            # if  

    min_distance_so_far = float('inf')
    while True:
        min_value, min_idx = iters.min_key() #fetches min key
        max_value = iters.max_key()[0]
        min_distance_so_far = min(max_value - min_value, min_distance_so_far)
        it = iters.pop_min()[1]#[1] returns the iterator of min which was ejected, pop_min return key, value pair
        next_min = next(it, None)
        # Return if some array has no remaining elements.
        if next_min is None:
            return typing.cast(int, min_distance_so_far)
        iters.insert((next_min, min_idx), it)

# below code proves that you can simply just create key without tuple to address duplicates. 
# code returns incorrect answer for non tuple keys
def find_closest_elements_in_sorted_arrays_simple(sorted_arrays: List[List[int]]
                                           ) -> int:
    #Reminds me of merging k sorted arrays
    # Stores array iterators in each entry.
    sorted_arrays_iter = [iter(it) for it in sorted_arrays]
    iters = bintrees.RBTree()
    for idx, sorted_array in enumerate(sorted_arrays_iter):
        # it = iter(sorted_array)#converting them to iterators, useful
        first_min = next(sorted_array, None)
        if first_min is not None:
            #here using (first_min, idx) has tuple as key, second item 'idx' is the value
            iters.insert((first_min, idx), idx) 
            #cant use first_min alone as the key, since two array may have same values, hence we use idx too. 

    min_distance_so_far = float('inf')
    while True:
        min_value, _ = iters.min_key() #fetches min value key
        max_value = iters.max_key()[0]
        min_distance_so_far = min(max_value - min_value, min_distance_so_far)
        idx = iters.pop_min()[1]#[1] returns the index of min item which was ejected
        next_min = next(sorted_arrays_iter[idx], None)
        # Return if some array has no remaining elements.
        if next_min is None:
            return typing.cast(int, min_distance_so_far)
        iters.insert((next_min, idx), idx)

# find_closest_elements_in_sorted_arrays_simple([[5,10,15], [3,6,9,12,15], [8,16,24]])

#using sortedcontainer
from sortedcontainers import SortedList
def find_closest_elements_in_sorted_arrays_sorted_containers(sorted_arrays: List[List[int]]):
    bst = SortedList([])
    min_interval_diff = float('Inf')
    nums_iter = [iter(num) for num in sorted_arrays]
    for idx, val in enumerate(nums_iter):
        elem = next(val, None)
        if elem is not None:
            bst.add((elem, idx))
    
    while True:
        min_elem, idx = bst[0]
        max_elem, _ = bst[-1]
        interval_diff = max_elem - min_elem
        if interval_diff < min_interval_diff:
            min_interval_diff = interval_diff
        next_elem = next(nums_iter[idx], None)
        bst.pop(0)
        if next_elem is None:
            break
        bst.add((next_elem, idx))
    return min_interval_diff

#faster
#using heap and iter and finding max on the fly
# Time: O(nlogk)

def find_closest_elements_in_sorted_arrays_heap1(sorted_arrays: List[List[int]]):
    min_heap = []
    heapq.heapify(min_heap)
    min_interval_diff = float('Inf')
    max_elem = float('-Inf')#dont use zero, it will fail for negative numbers only arrays
    nums_iter = [iter(num) for num in sorted_arrays]
    for idx, val in enumerate(nums_iter):
        elem = next(val, None)
        if elem is not None:
            heapq.heappush(min_heap, (elem, idx))
            max_elem = max(max_elem, elem)
            
    while True:
        min_elem, idx = heapq.heappop(min_heap)
        interval_diff = max_elem - min_elem
        if interval_diff < min_interval_diff:
            min_interval_diff = interval_diff
        next_elem = next(nums_iter[idx], None)
        if next_elem is None:
            break
        heapq.heappush(min_heap, (next_elem, idx))
        max_elem = max(next_elem, max_elem)
    return min_interval_diff

#using heap and index only
# Time: O(nlogk)
def find_closest_elements_in_sorted_arrays(sorted_arrays: List[List[int]]):
    min_heap = []
    heapq.heapify(min_heap)
    min_interval_diff = float('Inf')
    max_elem = float('-Inf')#dont use zero, it will fail for negative numbers only arrays
    for arr_idx, val in enumerate(sorted_arrays):
        elem = val[0]
        if elem is not None:
            heapq.heappush(min_heap, (elem, arr_idx, 0))
            max_elem = max(max_elem, elem)
            
    while True:
        min_elem, arr_idx, pos = heapq.heappop(min_heap)
        interval_diff = max_elem - min_elem
        if interval_diff < min_interval_diff:
            min_interval_diff = interval_diff
        if pos == len(sorted_arrays[arr_idx]) - 1:
            break
        next_elem = sorted_arrays[arr_idx][pos + 1]
        heapq.heappush(min_heap, (next_elem, arr_idx, pos + 1))
        max_elem = max(next_elem, max_elem)
    return min_interval_diff

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('14-06-minimum_distance_3_sorted_arrays.py',
                                       'minimum_distance_3_sorted_arrays.tsv',
                                       find_closest_elements_in_sorted_arrays))
