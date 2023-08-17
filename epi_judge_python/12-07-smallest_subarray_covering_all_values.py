import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure  # keep
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

"""
Write a program that takes two arrays of strings, and return the indices of the starting and ending index of a 
shortest subarray of the first array that 'sequentially covers' all the strings of the keywords array. 
Assume all strings are disctict in keyword array.
Logic:
One hashmap and two  arrays
    Create  hashmap (keyword_to_idx) for tracking the relative position of strings in keywords, i.e., their index numbers in keywords
    Create  an array (shortest_subarray_length) for storing the shortest subarray length created until that string in the keyword list
    Create another array which has its index mapped to position of those kywords, this array will store the altest index found for that keyword

    While enumerating through the paragraph array, keep updating the latest location of keyword encountered, and if
    they are in order, update the shortest_subarray_length for that keyword
    IT doesnt matter if after update the length increase, we concentrate on the overall length of subarray
    at the last if condition



    only the shortest_subarray_length[-1] is used for finding the overall shortest size of subarray
Time: O(n), space: O(m), m is the number strings in keywords
"""
#sounds like a dynamic program
def find_smallest_sequentially_covering_subset_original(paragraph: List[str],
                                               keywords: List[str]
                                               ) -> Subarray:

    # Maps each keyword to its index in the keywords array.
    keyword_to_idx = {k: i for i, k in enumerate(keywords)}# used for getting the index once the keyword found in the paragraph

    # Since keywords are uniquely identified by their indices in keywords
    # array, we can use those indices as keys to lookup in an array.
    #above line is important, using indices instead of keyword: Jayant

    latest_occurrence = [-1] * len(keywords) #for storing the latest index of that keyword in the paragraph
    # For each keyword (identified by its index in keywords array), the length
    # of the shortest subarray ending at the most recent occurrence of that
    # keyword that sequentially cover all keywords up to that keyword.
    shortest_subarray_length = [float('inf')] * len(keywords) #storing and updating the distance

    shortest_distance = float('inf')
    result = Subarray(-1, -1)
    for i, p in enumerate(paragraph):
        if p in keyword_to_idx:
            
            keyword_idx = keyword_to_idx[p] #get the index position of that keyword in the keywords
            #note that these keyword position will be updated throughout the iteration
            #on each update their latest_occurrence position will only move ahead, so
            #if a keyword of order ith is found and reupdated with new index, it wont have any impact on i+1th keyword up until i+1th keyword
            #is also found later. Then their shortest_subarray_length array will be updated
            if keyword_idx == 0:  # First keyword.
                shortest_subarray_length[keyword_idx] = 1
            elif shortest_subarray_length[keyword_idx - 1] != float('inf'):#check if previous has been filled then only update. This maintains the order
                distance_to_previous_keyword = (
                    i - latest_occurrence[keyword_idx - 1])
                shortest_subarray_length[keyword_idx] = (
                    distance_to_previous_keyword +
                    shortest_subarray_length[keyword_idx - 1])
            latest_occurrence[keyword_idx] = i
            
            # Last keyword, for improved subarray. for getting the shortest distance
            if (keyword_idx == len(keywords) - 1
                    and shortest_subarray_length[-1] < shortest_distance):
                shortest_distance = shortest_subarray_length[-1]
                result = Subarray(i - shortest_distance + 1, i)#we are not using latest location of first keywords
                #since that could have been updated with new one
            #print(f'keyword_idx = {keyword_idx} p = {p}, latest_occurrence[keyword_idx] = {latest_occurrence[keyword_idx]}, shortest_subarray_length = {shortest_subarray_length}, shortest_distance = {shortest_distance}')
            #print("==========")
    return result

# find_smallest_sequentially_covering_subset(['apple', 'banana','cat','apple', 'cat', 'banana', 'cat', 'apple', 'cat'],  ['banana', 'apple', 'cat'])

#practice run
def find_smallest_sequentially_covering_subset(paragraph: List[str],
                                               keywords: List[str]
                                               ) -> Subarray:
    Subarray = collections.namedtuple('Subarray', ('start', 'end'))
    result = Subarray(start = -1, end = -1)
    keywords_to_idx = {value: index for index, value in enumerate(keywords)}
    latest_location_keywords = [-1] * len(keywords)
    subarray_length_per_keyword = [float('Inf')] * len(keywords)
    shortest_subarray = float('Inf')
    for index, word in enumerate(paragraph):
        if word in keywords_to_idx:
            key_index = keywords_to_idx[word]
            latest_location_keywords[key_index] =  index
            if key_index == 0:
                subarray_length_per_keyword[key_index] = 1
            elif subarray_length_per_keyword[key_index - 1] != float('Inf'): #check to make sure that previous key was encountered
                distance_to_key = index - latest_location_keywords[key_index - 1]
                subarray_length_per_keyword[key_index] = distance_to_key + subarray_length_per_keyword[key_index - 1]
            
            if (key_index == len(keywords) - 1 and 
                subarray_length_per_keyword[-1] < shortest_subarray):
                shortest_subarray = subarray_length_per_keyword[-1]
                result = Subarray(start = index - shortest_subarray + 1, end = index)
    return result
    

@enable_executor_hook
def find_smallest_sequentially_covering_subset_wrapper(executor, paragraph,
                                                       keywords):
    result = executor.run(
        functools.partial(find_smallest_sequentially_covering_subset,
                          paragraph, keywords))

    kw_idx = 0
    para_idx = result.start
    if para_idx < 0:
        raise RuntimeError('Subarray start index is negative')

    while kw_idx < len(keywords):
        if para_idx >= len(paragraph):
            raise TestFailure('Not all keywords are in the generated subarray')
        if para_idx >= len(paragraph):
            raise TestFailure('Subarray end index exceeds array size')
        if paragraph[para_idx] == keywords[kw_idx]:
            kw_idx += 1
        para_idx += 1

    return result.end - result.start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            '12-07-smallest_subarray_covering_all_values.py',
            'smallest_subarray_covering_all_values.tsv',
            find_smallest_sequentially_covering_subset_wrapper))
