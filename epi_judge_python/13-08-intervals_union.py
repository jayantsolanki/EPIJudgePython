import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

"""
Leetcode 56: https://leetcode.com/problems/merge-intervals/
Design an algo that takes as input a set of intervals, and outputs their union expressed as a set of disjoint intervals.
Logic:
    First sort the array by left endpoints, in ascending order then start handling the cases:
    1 - the intervals most recently added to the result array does not intersect with the incoming interval (current interval), 
        nor does its right endpoint equals the left endpoint of incoming interval, then simply added the incoming interval to result
    2 - The most recent interval intersects with the incoming one, then in this case, update the right enpoint of recent interval with the
        value end point which is max (get the union) and update the recent one.
    3- recent interval and incoming are that the boundary (that is right endpoint of recent intervals equals left endpoint of incoming one) and either the right endpoint of recent one or the left enpoint of current is closed interval, then in this case we get the union and update the recent one.
"""
Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))


def union_of_intervals_v2(intervals: List[Interval]) -> List[Interval]:

    # Empty input.
    if not intervals:
        return []

    # Sort intervals according to left endpoints of intervals.
    intervals.sort(key=lambda i: (i.left.val, not i.left.is_closed))
    result = [intervals[0]]
    for i in intervals:
        if intervals and (i.left.val < result[-1].right.val or #checking for intervals is empty or not needed
                          (i.left.val == result[-1].right.val and
                           (i.left.is_closed or result[-1].right.is_closed))):
            if (i.right.val > result[-1].right.val or
                (i.right.val == result[-1].right.val and i.right.is_closed)):
                result[-1] = Interval(result[-1].left, i.right)
        else:
            result.append(i)
    return result

# a bit simple
def union_of_intervals(intervals: List[Interval]) -> List[Interval]:

    # Empty input.
    if not intervals:
        return []

    # Sort intervals according to left endpoints of intervals.
    intervals.sort(key=lambda i: (i.left.val, not i.left.is_closed))
    result = [intervals[0]]
    for i in intervals:
        if (i.left.val < result[-1].right.val):#intersecting, just modify the result[-1] element
            #now find the right most boundary, make sure to get the closed interal status if present
            #calculating union
            if i.right.val > result[-1].right.val:
                result[-1] = Interval(result[-1].left, i.right)
            elif ((i.right.val == result[-1].right.val and i.right.is_closed)):#if closed, then pick the closed one
                result[-1] = Interval(result[-1].left, i.right)
        elif (i.left.val == result[-1].right.val and #doesnt intersect but at the boundary
                (i.left.is_closed or result[-1].right.is_closed)):
            if i.right.val > result[-1].right.val:
                result[-1] = Interval(result[-1].left, i.right)
            elif ((i.right.val == result[-1].right.val and i.right.is_closed)):#if closed, then pick the closed one
                result[-1] = Interval(result[-1].left, i.right)
        else:
            result.append(i)
    return result

@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [(i.left.val, i.left.is_closed, i.right.val, i.right.is_closed)
            for i in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('13-08-intervals_union.py',
                                       'intervals_union.tsv',
                                       union_of_intervals_wrapper))
