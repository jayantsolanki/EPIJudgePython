from typing import List

from test_framework import generic_test

"""
Schedule to minimize waiting time
Given service times for a set of queries, compute a schedule for processing the queries that 
minimizes the total waiting time.
Logic:
    Sort the service times by ascending order and process the shorter queries first. So that they are gone quickly and 
    then we focus on longer queries and let them take their due time
Time: O(nlogn)
"""
#original

def minimum_total_waiting_time_ori(service_times: List[int]) -> int:

    # Sort the service times in increasing order.
    service_times.sort()
    total_waiting_time = 0
    for i, service_time in enumerate(service_times):
        num_remaining_queries = len(service_times) - (i + 1)
        total_waiting_time += service_time * num_remaining_queries
    return total_waiting_time


def minimum_total_waiting_time_pythonic(service_times):
    return sum(
        remaining_queries * time
        for remaining_queries, time in enumerate(sorted(service_times)[::-1]))

#my way
#first one is always zero, so i start from 1 and start adding those to previous values
#second variable takes the total
def minimum_total_waiting_time(service_times: List[int]) -> int:
    service_times.sort()
    wait_time_cumulative = [0]
    total_wait = 0
    for i in range(1, len(service_times)):
        wait_time_cumulative.append(wait_time_cumulative[-1] + service_times[i-1]) #ith will run after  i -1, i - 2 .. 0 items are done
        total_wait = total_wait + wait_time_cumulative[-1]
    return total_wait



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('17-02-minimum_waiting_time.py',
                                       'minimum_waiting_time.tsv',
                                       minimum_total_waiting_time))
