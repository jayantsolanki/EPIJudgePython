import itertools
from typing import Iterator

from test_framework import generic_test
from test_framework.test_failure import TestFailure

"""
Suppose you were given a file containing roughly 1 billion IP address, each of 32 bit size. How would you programatically
find an ip address that is not in the file? Assume you have unlimited storage but few MB of RAM. You only need to find 
any one IP.
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
        Since some lower half are missing, array indices representing those lower half will have count of zero
        Ta-da, those zero counts are your missing IPs
    Summary:
    Use two counters:
    1st counter(counter) is of size = the upper 0 - 2^16 - 1, each index represents the first half of IP numbers ( xxx-xxx-???-???)
    2nd counter (candidates) is of size lower 0 - 2^16 - 1, each index represents the first half of IP numbers ( ???-???-xxx-xxx)
    Iterate through the stream right shifting the bits of each ip by 16, this will help to get their counter in 1st array
    Since, some IPs are missing so not all index in the 1st counter will be == 2^16 value, just get any one index (candidate_bucket)
    Use that index as the mask, and iterate again through the stream, push the bits right by 16 and compare those with the mask
        if equal then use the lower 16bits as the indices to get the count in second counter.
    Since some IPs are missing so some of the indices in the second counter will remain 0, combine the 16bit of candidate bucket and 16bit of
    any one indices of 2nd counter and get the IP.
Time: O(n), Space: O(1)
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
    # candidate_bucket = next(i for i, c in enumerate(counter)#bascially get the index of those have less ip count, 
    # index is actually
    #                         if c < bucket_capacity)#first 16bit in integer
    # below or top both are fine
    #this is a variable not and array
    #basically get the index of those have less ip count, index is actually
    candidate_bucket = [i for i, c in enumerate(counter)
                            if c < bucket_capacity][0]#Only finding one missing IP address shall be fine, Important
    # Finds all IP addresses in the stream whose first 16 bits are equal to
    # candidate_bucket.
    
    #this array hold the lower 16bit portion of the IP, and not all will be marked
    # not all will be filled, some will remain zero and those are missing ones
    candidates = [0] * bucket_capacity
    #now go thorugh the stream, find those IP address whose first half is present in candidate_bucket, 
    # extract their second half and 
    #use those as index to count them in the candidates array, those found will be marked one, line 54
    for x in stream_copy:
        upper_part_x = x >> 16
        if candidate_bucket == upper_part_x:
            # Records the presence of 16 LSB of x.
            # lower_part_x = ((1 << 16) - 1) & x #gets the lower 16bits or use 2^16 - 1 mod
            lower_part_x = (2**16 - 1) & x
            # lower_part_x = (0xFFFF) & x #gets the lower 16bits, or use 65535 or 2^16 - 1
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
