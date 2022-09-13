from typing import List
import heapq

from test_framework import generic_test, test_utils

"""
Find k largest elements in a Max-heap without modifying the existing heap
HInt: Use array representation of i, 2i + 1 and 2i + 2, to find parent, and its respective children
Second hint: parent is always equal to greater than its two children, so start constructing the result array from parent at index 0
Third hint: use a temporary maxheap to procure the stored elements from given heap and also to get max element encountered till now
Time: O(klogk), space O(k)
"""
def k_largest_in_binary_heap_v2(A: List[int], k: int) -> List[int]:

    if k <= 0:
        return []

    # Stores the (-value, index)-pair in candidate_max_heap. This heap is
    # ordered by value field. Uses the negative of value to get the effect of
    # a max heap.
    candidate_max_heap = []# heap is needed because children of the children in one subtree may or may not be larger than
    #an the children of the children in other subtree. Hence we keep pushing those children found into the max heap 
    # and popping the max out of them
    # The largest element in A is at index 0.
    candidate_max_heap.append((-A[0], 0))
    result = []
    for _ in range(k):
        candidate_idx = candidate_max_heap[0][1]
        result.append(-heapq.heappop(candidate_max_heap)[0])
    #now get the children and put them to temp heap
        left_child_idx = 2 * candidate_idx + 1
        if left_child_idx < len(A): #important, make sure the left_child exists
            heapq.heappush(candidate_max_heap,
                           (-A[left_child_idx], left_child_idx))
        right_child_idx = 2 * candidate_idx + 2
        if right_child_idx < len(A):
            heapq.heappush(candidate_max_heap,
                           (-A[right_child_idx], right_child_idx))
    return result


#practice:
def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    if not A:
        return []
    if k <= 0:
        return []
    result = []
    max_heap = [(-A[0], 0)] #negative because it is maxheap

    for _ in range(k):
        largest_element, element_index = heapq.heappop(max_heap)
        left_index = 2 * element_index + 1
        right_index = 2 * element_index + 2

        if left_index < len(A):
            heapq.heappush(max_heap, (-A[left_index], left_index))
        if right_index < len(A):
            heapq.heappush(max_heap, (-A[right_index], right_index))

        result.append(-largest_element)
    return result








if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            '10-06-k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
