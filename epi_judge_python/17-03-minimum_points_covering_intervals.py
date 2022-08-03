import collections
import functools
import operator
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


"""
Leetcode: 452. Minimum Number of Arrows to Burst Balloons
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

The interval covering problem
You are given a set of closed intervals. Design an efficeint algorithm for finding a minimum sized set of 
numbers that covers all the intervals.
Another description:
Consider a foreman responsible for a number fo tasks on the factory floor. Each task starts at a fixed time 
and ends at fixed time. The foremanwants to visit the floor to check on the tasks. Your job is to help 
him minimize the number of visits. That is find the visit times which can conincide with max running tasks.
Logic:
    Sort all interval on right endpoints. Select the first interval's right endpoint, iterate through 
    intervals, looking for those intervals which have overlapping with selected right endpoint. Look for the first interval 
    which has no overalpping, and select its right endpoint and move on until you are done with all tasks. 
    These right end points selected will be the visit times.
    Example: [[1, 2], [2, 3], [3, 4], [2, 3], [3, 4], [4, 5]], Sorted: [[1, 2], [2, 3], [2, 3], [3, 4], [3, 4], [4, 5]]
"""

Interval = collections.namedtuple('Interval', ('left', 'right'))

def find_minimum_visits_ori(intervals: List[Interval]) -> int:

    # Sort intervals based on the right endpoints.
    intervals.sort(key=operator.attrgetter('right'))
    last_visit_time, num_visits = float('-inf'), 0
    for interval in intervals:
        if interval.left > last_visit_time:
            # The current right endpoint, last_visit_time, will not cover any
            # more intervals.
            last_visit_time = interval.right
            num_visits += 1
    return num_visits


#my way
def find_minimum_visits(intervals: List[Interval]) -> int:
    if len(intervals) == 0:
        return 0
    visit_time = 0
    intervals.sort(key = lambda a: a.right)#sort by endpoints
    total = 1 #at least one
    visit_time = intervals[0].right
    for i in range(1, len(intervals)):
        if intervals[i].left <= visit_time <= intervals[i].right:
            continue
        visit_time = intervals[i].right
        total += 1
    return total

#variant 1
""" 
You are responsible for the security of a castle. The castle has circular permimeter. A total of n robots patrol the perimeter.
Each robot is responsible for a closed connected subset of the perimter (arc). Arcs may overlap. What is the minimum number
of cameras required to monitor those robots.
Logic:
    same as above, just make sure that start and end of each arcs are provided
"""
def find_minimum_cameras(intervals: List[Interval]) -> int:
    if len(intervals) == 0:
        return 0
    visit_time = 0
    intervals.sort(key = lambda a: a.right)
    total = 1 #at least one
    visit_time = intervals[0].right
    for i in range(1, len(intervals)):
        if intervals[i].left <= visit_time <= intervals[i].right:
            continue
        visit_time = intervals[i].right
        total += 1
    return total

#variant 2
"""
There are number of points in the plane that you want to observe. You are located at the point(0, 0).
You can rotate about this point. What should the direction you face to maximize the number of visible point (field of view)?
Logic:
    Calculate the radians from x,y cooridnates. Sort it, and watch in the max radian - min radian
"""
@enable_executor_hook
def find_minimum_visits_wrapper(executor, A):
    A = [Interval(*a) for a in A]
    return executor.run(functools.partial(find_minimum_visits, A))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            '17-03-minimum_points_covering_intervals.py',
            'minimum_points_covering_intervals.tsv',
            find_minimum_visits_wrapper))
