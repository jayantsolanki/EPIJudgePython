import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
import operator

# Event is a tuple (start_time, end_time)

"""
Write a program that takes a series of events, and determines the maximum number of events that take place concurrently
Logic:
    Sort the intervals in ascending ordering, giving preference to start point first.
    For each end point of the intervals, if that is a start point, increase the counter, if finish time
    decrease the counter. Max value of counter is the max overlapping intervals
    Check https://docs.python.org/3.8/howto/sorting.html to learn sorting on multiple keys
    You can use lambda function for multiple keys, or the faster method of itemgetter or attrgettr
    For lambda you need to enclose return values in tuple
Time: Sort takes O(nlogn), scanning takes O(n), overall O(nlogn)
"""
Event = collections.namedtuple('Event', ('start', 'finish'))

def find_max_simultaneous_events(A: List[Event]) -> int:

    # Endpoint is a tuple (start_time, 0) or (end_time, 1) so that if times, True is 1, False is 0
    # are equal, start_time comes first
    Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))
    # Builds an array of all endpoints.
    E = [
        p for event in A
        for p in (Endpoint(event.start, True), Endpoint(event.finish, False))
        # for p in (Endpoint(event[0], True), Endpoint(event[1], False))
    ]
    # Sorts the endpoint array according to the time, breaking ties by putting
    # start times before end times.
    # https://docs.python.org/3.8/howto/sorting.html
    # https://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes
    #python can sort using multiple keys, you need to priovdfe them using tuples
    # https://stackoverflow.com/questions/18595686/how-do-operator-itemgetter-and-sort-work
    E.sort(key=lambda e: (e.time, not e.is_start))
    # Track the number of simultaneous events, record the maximum number of
    # simultaneous events.
    max_num_simultaneous_events, num_simultaneous_events = 0, 0
    for e in E:
        if e.is_start:
            num_simultaneous_events += 1
            max_num_simultaneous_events = max(num_simultaneous_events,
                                              max_num_simultaneous_events)
        else:
            num_simultaneous_events -= 1
    return max_num_simultaneous_events
#alternate
def find_max_simultaneous_events_alt(A: List[Event]) -> int:

    # Endpoint is a tuple (start_time, 0) or (end_time, 1) so that if times, True is 1, False is 0
    # are equal, start_time comes first
    Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))
    # Builds an array of all endpoints.
    E = [
        p for event in A
        for p in (Endpoint(event.start, 0), Endpoint(event.finish, 1))
    ]
    # Sorts the endpoint array according to the time, breaking ties by putting
    # start times before end times.
    # https://docs.python.org/3.8/howto/sorting.html
    # https://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes
    #python can sort using multiple keys, you need to priovdfe them using tuples
    # https://stackoverflow.com/questions/18595686/how-do-operator-itemgetter-and-sort-work
    # E.sort(key=lambda e: (e.time, not e.is_start))
    E.sort(key = operator.attrgetter('time', 'is_start')) # thsi also works E.sort(key = operator.itemgetter(0, 1))
    # Track the number of simultaneous events, record the maximum number of
    # simultaneous events.
    max_num_simultaneous_events, num_simultaneous_events = 0, 0
    for e in E:
        if e.is_start == 0:
            num_simultaneous_events += 1
            max_num_simultaneous_events = max(num_simultaneous_events,
                                              max_num_simultaneous_events)
        else:
            num_simultaneous_events -= 1
    return max_num_simultaneous_events

#variant 1
"""
Users 1, 2, ...., n share an Internet connection. User i uses bi bandwidthj from time si to fi, inclusive. What is the
peak bandwith usage?
Logic:
    Peak bandwith usage is the max bandwith used during concurrent usage from multiple users
    We can store the start time, end time and bandwith used in a tuple, then sort them then do the concurrency check
"""

def find_max_simultaneous_bandwidth_usage(A) -> int:

    # Endpoint is a tuple (start_time, 0) or (end_time, 1) so that if times, True is 1, False is 0
    # are equal, start_time comes first
    Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start', 'bandwidth'))
    # Builds an array of all endpoints.
    E = [
        p for event in A
        for p in (Endpoint(event[0], 0, event[2]), Endpoint(event[1], 1, event[2])) #stores (start or finish, is_start, bandwidth)
    ]
    # Sorts the endpoint array according to the time, breaking ties by putting
    # start times before end times.

    E.sort(key = operator.attrgetter('time', 'is_start')) # this also works E.sort(key = operator.itemgetter(0, 1))
    # Track the number of simultaneous events, record the maximum number of
    # simultaneous events.
    print(E)
    max_num_simultaneous_bandwidths, num_simultaneous_bandwidths = 0, 0
    for e in E:
        if e.is_start == 0:
            num_simultaneous_bandwidths += e.bandwidth
            max_num_simultaneous_bandwidths = max(num_simultaneous_bandwidths,
                                              max_num_simultaneous_bandwidths)
        else:
            num_simultaneous_bandwidths -= e.bandwidth
    return max_num_simultaneous_bandwidths

find_max_simultaneous_bandwidth_usage([[1, 5, 1], [2, 7, 2], [4, 5, 1], [6, 10, 3], [8, 9, 3], [9, 17, 3], [11, 13, 1], [12, 15, 3], [14, 15, 2]])

#variant 1-2 #uswe two arrays, one for intervals, and other for bandwidth
def find_max_simultaneous_bandwidth_usage_2(A, B) -> int:

    # Endpoint is a tuple (start_time, 0) or (end_time, 1) so that if times, True is 1, False is 0
    # are equal, start_time comes first
    temp = list(zip(A, B)) # [([1, 5], 1), ([2, 7], 2), ([4, 5], 1), ([6, 10], 3), ([8, 9], 3), ([9, 17], 3), ([11, 13], 1), ([12, 15], 3), ([14, 15], 2)]
    combined = [(x[0], x[1], y) for x, y in temp]
    Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start', 'bandwidth'))
    # Builds an array of all endpoints.
    E = [
        p for event in combined
        for p in (Endpoint(event[0], 0, event[2]), Endpoint(event[1], 1, event[2])) #stores (start or finish, is_start, bandwidth)
    ]
    # Sorts the endpoint array according to the time, breaking ties by putting
    # start times before end times.

    E.sort(key = operator.attrgetter('time', 'is_start')) # this also works E.sort(key = operator.itemgetter(0, 1))
    # Track the number of simultaneous events, record the maximum number of
    # simultaneous events.
    print(E)
    max_num_simultaneous_bandwidths, num_simultaneous_bandwidths = 0, 0
    for e in E:
        if e.is_start == 0:
            num_simultaneous_bandwidths += e.bandwidth
            max_num_simultaneous_bandwidths = max(num_simultaneous_bandwidths,
                                              max_num_simultaneous_bandwidths)
        else:
            num_simultaneous_bandwidths -= e.bandwidth
    return max_num_simultaneous_bandwidths

find_max_simultaneous_bandwidth_usage_2([[1, 5], [2, 7], [4, 5], [6, 10], [8, 9], [9, 17], [11, 13], [12, 15], [14, 15]], [1, 2, 1, 3, 3, 3, 1, 3, 2])

@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('13-06-calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
