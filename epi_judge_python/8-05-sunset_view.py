from typing import Iterator, List
import collections

from numpy import Inf
from test_framework import generic_test

"""
Write a program that processess buildings from east-to-west order, and returns the set of buildings which view the sunset.
Each building is specified by a size
#basically, you maintain a stack of buildings that can view the sunset
If a incoming building is taller than building at the top of stack, we keep popping it untill we find a building taller then 
incoming build. Voila
"""
def examine_buildings_with_sunset_original(sequence: Iterator[int]) -> List[int]: #returns the indices 

    BuildingWithHeight = collections.namedtuple('BuildingWithHeight',
                                                ('id', 'height'))# need to keep track of both height and indices
    candidates: List[BuildingWithHeight] = []#creating a list of tuple pair
    for building_idx, building_height in enumerate(sequence):
        while candidates and building_height >= candidates[-1].height:
            candidates.pop()
        candidates.append(BuildingWithHeight(building_idx, building_height))
    return [c.id for c in reversed(candidates)]

print(examine_buildings_with_sunset_original([1,2,3,4,5,6]))
print(examine_buildings_with_sunset_original([6,5,4,3,2,1]))

def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]: #returns the indices 

    candidates = []#creating a list of tuple pair
    for building_idx, building_height in enumerate(sequence):
        while candidates and building_height >= candidates[-1][1]:# need to keep track of both height and indices
            candidates.pop()
        candidates.append((building_idx, building_height)) #0 has index, 1 has height
    return [c[0] for c in reversed(candidates)]#returning the index in reverse, i dont know whey reverse

# print(examine_buildings_with_sunset_v2([1,2,3,4,5,6]))
# print(examine_buildings_with_sunset_v2([6,5,4,3,2,1]))

#SIMPLE
#just check the running max
def examine_buildings_with_sunset_v2(sequence: Iterator[int]) -> List[int]: #returns the indices 
    candidates = []
    running_max = float("-Inf")
    for building_idx, building_height in reversed(list(enumerate(sequence))):#accesses original index but in reverse
        if building_height > running_max:
            candidates.append(building_idx)
            running_max = building_height
    # return [c for c in reversed(candidates)]
    return [c for c in candidates]

print(examine_buildings_with_sunset_v2([1,2,3,4,5,6]))
print(examine_buildings_with_sunset_v2([6,5,4,3,2,1]))
print(examine_buildings_with_sunset_v2([6, 3, 4]))


#variant 2, buildings west-east order
#logic just keep trackof running sum, and dont reverse the list
def examine_buildings_with_sunset_v3(sequence: Iterator[int]) -> List[int]: #returns the indices 
    candidates = []
    running_max = float("-Inf")
    for building_idx, building_height in enumerate(sequence):#accesses original index but in reverse
        if building_height > running_max:
            candidates.append(building_idx)
            running_max = building_height
    # return [c for c in reversed(candidates)]
    return [c for c in candidates]

print(examine_buildings_with_sunset_v3([6, 3, 4]))
print(examine_buildings_with_sunset_v3([7, 4, 8, 2, 9]))


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('8-05-sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
