import heapq
from typing import Iterator, List


from test_framework import generic_test

"""
Leetcode: 295 https://leetcode.com/problems/find-median-from-data-stream/
Design a program to compute running median of a sequence
Logic:
    Median elements = X[(n+1)/2], if n is odd, else, (x[n/2] + x[n/2 + 1])/2, X is already sorted. 
    Median is all about position. If we could maintain direct access to median elements at all times, 
    then finding the median would take a constant amount of time.
    If we could find a reasonably fast way of adding numbers to our containers, 
    additional penalties incurred could be lessened.
    Most importantly, we only need a consistent way to access the median elements. 
    Keeping the entire input sorted is not a requirement
    We could maintain two heaps in the following way:
    1 - A max-heap to store the smaller half of the input numbers, this heap will store largest value of this half at root
    2 - A min-heap to store the larger half of the input numbers, this heap will store smaller value of this half at root
    If the following conditions are met:

    1 - Both the heaps are balanced (or nearly balanced)
    2 - The max-heap contains all the smaller numbers while the min-heap contains all the larger numbers
    then we can say that:

    All the numbers in the max-heap are smaller or equal to the top element of the max-heap (let's call it x)
    All the numbers in the min-heap are larger or equal to the top element of the min-heap (let's call it y)
    Then x and/or y are smaller than (or equal to) almost half of the elements and larger than 
    (or equal to) the other half. That is the definition of median elements.
    Time: log(n)
"""
 
def online_median_v2(sequence: Iterator[int]) -> List[float]:

    # min_heap stores the larger half seen so far.
    min_heap: List[int] = []
    # max_heap stores the smaller half seen so far.
    # values in max_heap are negative
    max_heap: List[int] = []
    result = []#stores running median
    # https://leetcode.com/problems/find-median-from-data-stream/solution/
    for x in sequence: # implementation on leetcode is opposite of this but is correct
        # Since max heap stores the lesser half of the sequence so
        #max heap is supposed to get the smaller numbers from min_heap. 
        # It cannot get directly from the array sequence
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, x)) #max_heap keep getting the smaller numbers
        # Ensure min_heap and max_heap have equal number of elements if an even
        # number of elements is read; otherwise, min_heap must have one more
        # element than max_heap.
        # we store the extra one value in min_heap when both heaps are unbalanced, 
        # balanced as in  0 == 0 also
        if len(max_heap) > len(min_heap):#checks if even or odd number of values read 
            # this line makes sure that min_heap length is never zero
            # cause in line 45, min_heap let go off its element via pushpop. 
            # Without line 52, min_heap will always remain of length 0 due to pushpop
            heapq.heappush(min_heap, -heapq.heappop(max_heap)) #  min_heap keep getting the larger numbers

        result.append(0.5 * (min_heap[0] + (-max_heap[0])) if len(min_heap) ==
                      len(max_heap) else min_heap[0])
        print("================")
        print(x)
        print("minheap", min_heap)
        print("maxheap",  max_heap)
        print(result[-1])
    return result
# online_median_v2(iter([1, 0, 3, 5, 2, 0, 1]))
online_median_v2(iter([5, 4, 3, 2, 1]))

# alternate, much simpler
# here make sure that min_heap keep getting the larger numbers and max_heap keep getting the smaller numbers
# hence use pushpop on maxheap and minheap respectively on line 82 and 85

def online_median_simple(sequence: Iterator[int]) -> List[float]:

    # min_heap stores the larger half seen so far.
    min_heap: List[int] = []
    # max_heap stores the smaller half seen so far.
    # values in max_heap are negative
    max_heap: List[int] = []
    result = []#stores running median
    count  = 1
    for x in sequence:
        if count % 2 == 0:#even
            #max, only minimum numbers from min_heap can be stored into max_heap,
            #  this makes sure maxheap contains smaller 
            # first half
            heapq.heappush(max_heap, -heapq.heappushpop(min_heap, x))
        else:#odd, #only max numbers from max_heap can be stored into min_heap, 
            #this makes sure minheap contains larger second half
            #when odd ( aka unbalanced), min heap needs to have largest element from maxheap
            heapq.heappush(min_heap, -heapq.heappushpop(max_heap, -x))
        count += 1

        result.append(0.5 * (min_heap[0] + (-max_heap[0])) if len(min_heap) ==
                      len(max_heap) else min_heap[0])
    return result

#idea here is same, both heap should have largest of the first half and smallest 
# of the second half. And line 104 has to be executed lest max_heap will always remain 
# of length zero. so same thing as above, but funneling though max-heap first, instead 
# of min_heap
def online_median(sequence: Iterator[int]) -> List[float]:

    # min_heap stores the larger half seen so far.
    min_heap: List[int] = []
    # max_heap stores the smaller half seen so far.
    # values in max_heap are negative
    max_heap: List[int] = []
    result = []#stores running median
    for x in sequence: 
        heapq.heappush(min_heap, -heapq.heappushpop(max_heap, -x))
        if len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap)) 

        result.append(0.5 * (min_heap[0] + (-max_heap[0])) if len(min_heap) ==
                      len(max_heap) else -max_heap[0])
        #max heap here, since max_heap contains the extra element
    return result

def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('10-05-online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
