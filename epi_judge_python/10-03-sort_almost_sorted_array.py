import heapq
import itertools
from typing import Iterator, List

from test_framework import generic_test

"""
Write a program which takes as input a very long dequence of numbers and prints the numbers
in sorted array. Each number is at most k position away from it correctly sorted position. Also called k-sorted array
Example [3, -1, 2, 6, 4, 5, 8], is numbers is within 2 positions away from its correctly sorted [-1, 2, 3, 4, 5, 6, 8]
Analogy, Often data is almost sorted, for example, a server receivesn timestamped stock quiotes and earlier quotes 
may arrive slightly after later quotes because of server loads or network congestions.
Below probelm will efficiently sort those
Logic: To solve this problem in general setting, we need to store the k+1 numbers in a min-heap, that will enable to 
extract min number efficiently, and add new number efficiently. We add additional numbers to minheap and extract 
minimum from the min heap. When  we run out of new number we simple starts to just extract
Time: O(nlogk), space O(k)
"""
def sort_approximately_sorted_array_v2(sequence: Iterator[int],
                                    k: int) -> List[int]:

    min_heap: List[int] = []
    # Adds the first k elements into min_heap. Stop if there are fewer than k
    # elements.
    for x in itertools.islice(sequence, k):
        heapq.heappush(min_heap, x)

    result = []
    # For every new element, add it to min_heap and extract the smallest.
    for x in sequence:
        smallest = heapq.heappushpop(min_heap, x)#heappushpop is more efficient
        result.append(smallest)

    # sequence is exhausted, iteratively extracts the remaining elements.
    while min_heap:
        smallest = heapq.heappop(min_heap)
        result.append(smallest)

    return result

#practice run
def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:

    min_heap = []
    result = []
    #adding first k items
    for item in itertools.islice(sequence, k):
        heapq.heappush(min_heap, item)
    
    #now taking out the min elements and adding it to result and at the same time adding new element to heap
    for item in sequence:
        smallest = heapq.heappushpop(min_heap, item)
        result.append(smallest)
    #once run out of sequence then append the remaining elements from heap
    while min_heap:
        result.append(heapq.heappop(min_heap))
    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            '10-03-sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
