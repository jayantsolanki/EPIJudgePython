import itertools
from typing import Iterator

from test_framework import generic_test
from test_framework.test_failure import TestFailure

"""
Based on ferquency counter
A files contains roughly 1 billion IP addresses. Design an algo to programatically find IP numbers which are not present 
in the file. Only finding one missing IP address shall be fine
Total IP numbers represented = 2^32

Since IP address is made up of 32 bits, use first half of bits (2^16 bits) to find the count of each series
Store first 16 bits in the form of 0 - 2^16 - 1 size array. 
Logic:
    Divide the IP series representation into first 16 bits half and second 16 bits half
    Use the first half to get the total combination of IP series found. 
        For this create an array called counter array, of size 0 - 2^16 - 1, each index represents the first half of IP numbers ( xxx-xxx-???-???)
        Each index at ideal will count to 2^16, since lower 16 bit half can have 2^16 combinations
        So some indices representing IP series will have lower count, so identify them
        Once those IP Series have identified, your task is now to count the lower half of those 16 bits.
        Create and array called candidates, to represent those lower half, array size = 2 ^ 16 -1.
        Since some lower half are missing, array indices repsenting those lower half will have count of zero
        Ta-da, those zero counts are your missing IPs
"""
def find_missing_element(stream: Iterator[int]) -> int:

    num_bucket = 1 << 16
    counter = [0] * num_bucket#creating integer array of size 2^16 -1 to store the count of each series (xxx-xxx-???-???)
    stream, stream_copy = itertools.tee(stream)#create two copies, one for counting another for searching the missing ones
    for x in stream:
        upper_part_x = x >> 16 #pull out their first 16 bits
        counter[upper_part_x] += 1#then count their occurrence

    # Look for a bucket that contains less than (1 << 16) elements.
    bucket_capacity = 1 << 16 # 1 <<16 because first 16bits can  hold at most 2^16 combinations of last 16 bits
    # candidate_bucket = next(i for i, c in enumerate(counter)#bascially get the index of those have less ip count, index is actually
    #                         if c < bucket_capacity)#first 16bit in integer
    # below or top both are fine
    #this is a variable not and array
    candidate_bucket = [i for i, c in enumerate(counter)#bascially get the index of those have less ip count, index is actually
                            if c < bucket_capacity][0]#Only finding one missing IP address shall be fine, Important
    # Finds all IP addresses in the stream whose first 16 bits are equal to
    # candidate_bucket.
    
    #this array hold the lower 16bit portion of the IP, and not all will be marked
    candidates = [0] * bucket_capacity# not all will be filled, some will remain zero and those are missing ones
    #now go thorugh the stream, find those IP address whose first half is present in candidate_bucket, extract their second half and 
    #use those as index to count them in the candidates array, those found will be marked one, line 54
    for x in stream_copy:
        upper_part_x = x >> 16
        if candidate_bucket == upper_part_x:
            # Records the presence of 16 LSB of x.
            # lower_part_x = ((1 << 16) - 1) & x #gets the lower 16bits
            lower_part_x = (0xFFFF) & x #gets the lower 16bits, or use 65535 or 2^16 - 1
            candidates[lower_part_x] = 1 #this are found one, so those with zero are missing ones

    # At least one of the LSB combinations is absent, find it.
    for i, v in enumerate(candidates):
        if v == 0:#count should be zero
            return (candidate_bucket << 16) | i#recreating the missing ip, firsthalf and second half

    raise ValueError('no missing element')


def find_missing_element_wrapper(stream):
    try:
        res = find_missing_element(iter(stream))
        if res in stream:
            raise TestFailure('{} appears in stream'.format(res))
    except ValueError:
        raise TestFailure('Unexpected no missing element exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('11-09-absent_value_array.py',
                                       'absent_value_array.tsv',
                                       find_missing_element_wrapper))
