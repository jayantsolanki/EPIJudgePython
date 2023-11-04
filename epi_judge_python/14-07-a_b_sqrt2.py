import heapq
import math
from typing import List
from sortedcontainers import SortedList

import bintrees

from test_framework import generic_test

# These numbers have very interesting property, and people called it ugly numbers. It is also called quadratic integer rings.

"""
Very weird problem, only runs with bintree, no heaps or sortedcontainers, key gets duplicated
Design an algorithm for efficiently computing the k smallest numbers of the form a + b*sqroot(2) for nonnegative integers a and b.
Logic:
    Use bST to find min a + b* sqroot(2), then insert (a+1) + b*sqroot(2) and a + (b+1)*sqroot(root). 
    Keep on popping min and inserting two next numbers. until result has k numbers.
In each iteration we perform a deletion and two insertion. There are k insertions, so the time complexity is O(klogk)
Space is O(k).
"""

class Number:
    def __init__(self, a, b):
        self.a, self.b = a, b
        self.val = a + b * math.sqrt(2)

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val
    
    def __hash__(self):
        return id(self)


def generate_first_k_a_b_sqrt2_(k: int) -> List[float]:

    # Initial for 0 + 0 * sqrt(2).
    candidates = bintrees.RBTree([(Number(0, 0), None)])#in this key value, value doesnt matter, hence None
    result: List[float] = []
    while len(result) < k:
        next_smallest = candidates.pop_min()[0]
        result.append(next_smallest.val)
        # Adds the next two numbers derived from next_smallest.
        candidates[Number(next_smallest.a + 1, next_smallest.b)] = None
        candidates[Number(next_smallest.a, next_smallest.b + 1)] = None
    return result

#using sortedlist
def generate_first_k_a_b_sqrt2_sortedList(k: int) -> List[float]:

    # Initial for 0 + 0 * sqrt(2).
    candidates = SortedList([Number(0, 0)])
    result = []
    while len(result) < k:
        next_smallest = candidates.pop(0)#get the minimum
        if result and result[-1] == next_smallest.val:#if duplicate found then ignore
            continue
        result.append(next_smallest.val)
        # Adds the next two numbers derived from next_smallest.
        candidates.add(Number(next_smallest.a + 1, next_smallest.b))
        candidates.add(Number(next_smallest.a, next_smallest.b + 1))
    return result
#using heap
def generate_first_k_a_b_sqrt2(k: int) -> List[float]:
    # Initial for 0 + 0 * sqrt(2).
    candidates = [Number(0, 0)]
    heapq.heapify(candidates)
    result = []
    while len(result) < k:
        next_smallest = heapq.heappop(candidates)#get the minimum
        if result and result[-1] == next_smallest.val:
            continue
        result.append(next_smallest.val)
        # Adds the next two numbers derived from next_smallest.
        heapq.heappush(candidates, Number(next_smallest.a + 1, next_smallest.b))
        heapq.heappush(candidates, Number(next_smallest.a, next_smallest.b + 1))
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('14-07-a_b_sqrt2.py', 'a_b_sqrt2.tsv',
                                       generate_first_k_a_b_sqrt2))
