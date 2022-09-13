import functools
import math
from typing import Iterator, List, Tuple
import heapq

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

"""
Remember there is O(n) solution using Quickselect
write a program to find k nearest stars in terms of distance to earth (0, 0, 0)
    Logic:
        Well first add the initial k stars from the input in to heap, this time a max heap
        Use the negative value to push to max value to the top root.
        Now once the heap is generated, start processing next star and only add those which are lesser than current max
        , if adding, then make sure to kick out the max star.
        Simply add each star to the maxheap, and discard the max from the max-heap once it contains the k + 1 stars
    Time: O(nlogk), space O(k)
"""
class Star:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __lt__(self, rhs: 'Star') -> bool:
        return self.distance < rhs.distance

    def __repr__(self):
        return str(self.distance)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, rhs):
        return math.isclose(self.distance, rhs.distance)#interesting


def find_closest_k_stars_v1(stars: Iterator[Star], k: int) -> List[Star]:

    # max_heap to store the closest k stars seen so far.
    max_heap: List[Tuple[float, Star]] = []
    for star in stars:
        # Add each star to the max-heap. If the max-heap size exceeds k, remove
        # the maximum element from the max-heap.
        # As python has only min-heap, insert tuple (negative of distance, star)
        # to sort in reversed distance order.
        heapq.heappush(max_heap, (-star.distance, star)) # see the negative sign
        if len(max_heap) == k + 1:#kinda counter intuitive, but remember, if the insert star is max, it will be at root then
            #hence, below line will eventually kick it, so any further max start automatically gets kicked out
            # deletion always occurs at the root, and the mx is only stored at the top
            heapq.heappop(max_heap)
        #so once the k max-heap goes thorugh all the star, it will only contains k max(negative) stars.

    # Iteratively extract from the max-heap, which yields the stars sorted
    # according from furthest to closest.# actually it is opposite, closest to further
    return [s[1] for s in heapq.nlargest(k, max_heap)]
    # return [s[1] for s in max_heap] #this also works

#this also works
def find_closest_k_stars(stars: Iterator[Star], k: int) -> List[Star]:

    # max_heap to store the closest k stars seen so far.
    max_heap: List[Tuple[float, Star]] = []
    for star in stars:
        # Add each star to the max-heap. If the max-heap size exceeds k, remove
        # the maximum element from the max-heap.
        # As python has only min-heap, insert tuple (negative of distance, star)
        # to sort in reversed distance order.
        if len(max_heap) == k:
             heapq.heappushpop(max_heap, (-star.distance, star))
        else:
            heapq.heappush(max_heap, (-star.distance, star)) # see the negative sign
        # if len(max_heap) == k + 1:#kinda counter intuitive, but remember, if the insert star is max, it will be at root then
        #     #hence, below line will eventually kick it, so any further max start automatically gets kicked out
        #     # deletion always occurs at the root, and the mx is only stored at the top
        #     heapq.heappop(max_heap)
        #so once the k max-heap goes thorugh all the star, it will only contains k max(negative) stars.

    # Iteratively extract from the max-heap, which yields the stars sorted
    # according from furthest to closest.# actually it is opposite, closest to further
    return [s[1] for s in heapq.nlargest(k, max_heap)]
    # return [s[1] for s in max_heap] #this also works


#variant 1
"""
Design an O(nlogk) time algo that reads a sequence of n elements and for each element, starting from the kth element, 
prints the kth largest element read up to that point. The length of sequence is not known in advance. You algo 
cannot use more than  O(k) additional storage. 
What are the worst-case inputs for your algo.
    Logic: kth largest element upto that point means print the smallest element encountered so far.
    Since after reading the first k elements, min heap will keep the smallest at the top aka the kth largest element
    After that start printing the root, then insert the next, pop the root. Pop the root because we want to remove that
    smallest element read so far
    Check with [1,2,3,4,5,6,7,8,9], k = 3, it should print 1, 2, 3, 4, 5, 6 once all the inputs are read
    Worst case input will be inputs already sorted in descending order, that will force the reorganization of 
    heap on every insert
"""
def kth_largest_element(elements:  Iterator[int], k: int):
    min_heap = []
    for element in elements:
        heapq.heappush(min_heap, element)
        if len(min_heap) == k + 1:#i think it should k not k + 1
            print(heapq.heappop(min_heap))
    
kth_largest_element(iter([1,2,3,4,5,6,7,8,9]), 3)


def comp(expected_output, output):
    if len(output) != len(expected_output):
        return False
    return all(
        math.isclose(s.distance, d)
        for s, d in zip(sorted(output), expected_output))


@enable_executor_hook
def find_closest_k_stars_wrapper(executor, stars, k):
    stars = [Star(*a) for a in stars]
    return executor.run(functools.partial(find_closest_k_stars, iter(stars),
                                          k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('10-04-k_closest_stars.py',
                                       'k_closest_stars.tsv',
                                       find_closest_k_stars_wrapper, comp))
