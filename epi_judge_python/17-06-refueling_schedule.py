import collections
import functools
from re import I
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

"""
Leetcode: 134. Gas Station
https://leetcode.com/problems/gas-station/
Given an instance of the gasup Problem. how would you efficiently compute an ample city? You can assume that an ample city does exist. The input is given in the form of two arrays, for gallons, gas at each city, and other for distance to next city.
Logic:
    Look at the graph in the book. We plot the consumption of gas when we start from first point. Note that the graph will remain same relatively irrespective from where we start.  That is drop in the consumption will remain same for each city visit.
    Our goal is to find the point (x, y), which can be used as the translation for this graph, such that minimum dip (fall), which 
    is below zero, could be moved up and left side. so that dip never goes below zero. That dip will be the start point (ample city)
"""

MPG = 20



# gallons[i] is the amount of gas in city i, and distances[i] is the
# distance city i to the next city.
def find_ample_city_ori(gallons: List[int], distances: List[int]) -> int:

    remaining_gallons = 0
    CityAndRemainingGas = collections.namedtuple('CityAndRemainingGas',
                                                 ('city', 'remaining_gallons'))
    city_remaining_gallons_pair = CityAndRemainingGas(0, 0)
    num_cities = len(gallons)
    for i in range(1, num_cities):
        remaining_gallons += gallons[i - 1] - distances[i - 1] // MPG
        if remaining_gallons < city_remaining_gallons_pair.remaining_gallons:
            city_remaining_gallons_pair = CityAndRemainingGas(
                i, remaining_gallons)
    return city_remaining_gallons_pair.city


# gallons[i] is the amount of gas in city i, and distances[i] is the
# distance city i to the next city.
#my take based on the analogy from book
# way, mimics grph in the book
def find_ample_city_simple(gallons: List[int], distances: List[int]) -> int:

    min_gas = float('Inf')
    min_point = -1
    m = len(gallons)
    current_gas = gallons[0]
    for i in range(m): 
        #to reach pos i, we need to go through 
        #gas left after reaching pos i + 1
        gas_left = current_gas - distances[(i) % m] // MPG
        # current_tank_level = refuel - consumed to reach that pos + previous_tank_level
        #refill at pos i + 1
        current_gas = gallons[(i + 1) % m] + gas_left
        if min_gas >= gas_left:
            min_gas = gas_left
            min_point = (i + 1) % m
        # print(current_gas, gallons[(i + 1) % m], distances[(i) % m])
    return min_point

#more better     
def find_ample_city(gallons: List[int], distances: List[int]) -> int:
    min_gas_left = float('Inf')
    min_point = -1 #point at which the min_gas_left was minimum
    m = len(gallons)
    gas_left = 0
    # current_gas = gallons[0]
    for i in range(1, m + 1): 
        #to reach pos i, we need to go through 
        #gas left after reaching pos i
        gas_left += gallons[i - 1] - distances[i - 1] // MPG
        #refill at pos i + 1
        if min_gas_left >= gas_left:
            min_gas_left = gas_left
            min_point = (i) % m
    return min_point
        
find_ample_city([50, 20, 5, 30, 25, 10, 10], [900, 600, 200, 400, 600, 200, 100])

#variant 1
# Solve the same problem when you cannot assume that there exists an ample city
"""
Logic:
    To make sure if there is no ample city, we just calcualte total gas available and total distance to cover.
    If the gas used for total distacne is > total gas avaialble, then no ample point, else we use above algo
"""
def find_ample_city(gallons: List[int], distances: List[int]) -> int:
    #check for feasibility
    if sum(gallons) < sum(distances) // MPG:
        return -1
    min_gas_left = float('Inf')
    min_point = -1 #point at which the min_gas_left was minimum
    m = len(gallons)
    gas_left = 0
    # current_gas = gallons[0]
    for i in range(1, m + 1): 
        #to reach pos i, we need to go through 
        #gas left after reaching pos i
        gas_left += gallons[i - 1] - distances[i - 1] // MPG
        #refill at pos i + 1
        if min_gas_left > gas_left:
            min_gas_left = gas_left
            min_point = (i) % m
    return min_point


@enable_executor_hook
def find_ample_city_wrapper(executor, gallons, distances):
    result = executor.run(
        functools.partial(find_ample_city, gallons, distances))
    num_cities = len(gallons)
    tank = 0
    for i in range(num_cities):
        city = (result + i) % num_cities
        tank += gallons[city] * MPG - distances[city]
        if tank < 0:
            raise TestFailure('Out of gas on city {}'.format(i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('17-06-refueling_schedule.py',
                                       'refueling_schedule.tsv',
                                       find_ample_city_wrapper))
