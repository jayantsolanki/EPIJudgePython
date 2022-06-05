import collections
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook



"""
Write a program  which takes an array of strings and a set of strings, and return the indices of the starting and ending 
index of a shortest subarray of the given array that 'cover' all the elements in the set, irrespective of the order
Logic:
    Use a sliding window, but with flexible start and end.
    Move end first, and stop as soon as all elements covered, then start to reduce the size of that window by moving the
    start. If moving the start causes some element is the set not covered, then start moving the end, until all elements covered
    Repeat start and end adjustment until you reach the end of array. Then return the smallest window found.
Time: O(n)
"""
#this only look into unique member of the set, no repetition
Subarray = collections.namedtuple('Subarray', ('start', 'end'))
def find_smallest_subarray_covering_set_v2(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:

    keywords_to_cover = collections.Counter(keywords)
    result = Subarray(start=-1, end=-1)
    remaining_to_cover = len(keywords)
    left = 0
    for right, p in enumerate(paragraph):
        if p in keywords:#keyword is a set, lookup is O(1)
            keywords_to_cover[p] -= 1
            if keywords_to_cover[p] >= 0: ##this is very important, because same word can be encountered many times
                # so lower the cover count when it goes to zero,  if it is negative then no need
                remaining_to_cover -= 1 #if p is covered, then reduce the size

        # Keeps advancing left until keywords_to_cover does not contain all
        # keywords.
        #once all the elements are covered, start to reduce the size
        while remaining_to_cover == 0:
            if result == Subarray(#check if the size of subarray is less, if less than save the new indices
                    start=-1,
                    end=-1) or right - left < result.end - result.start:
                result = Subarray(start=left, end=right)
            pl = paragraph[left]
            if pl in keywords:# Keeps advancing left until keywords_to_cover does not contain all elements in the set
                keywords_to_cover[pl] += 1
                if keywords_to_cover[pl] > 0:#so increase the cover only when it goes above zero
                    remaining_to_cover += 1  #since keywords_to_cover[pl] became > 0
            left += 1
    return result

#alternate, only difference in how we track the element in the set, see keywords_to_cover
def find_smallest_subarray_covering_set_simple(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:

    # keywords_to_cover = collections.Counter(keywords)
    keywords_to_cover = {x: 0 for x in keywords} # here we update that element has covered when its count becomes 1
    result = Subarray(start=-1, end=-1)
    remaining_to_cover = len(keywords)
    left = 0
    for right, p in enumerate(paragraph):
        if p in keywords:#keyword is a set, lookup is O(1)
            # keywords_to_cover[p] -= 1
            keywords_to_cover[p] += 1#that specific element in the set can occur many times in the subarray
            if keywords_to_cover[p] == 1: ##only update remaining_to_cover when it reaches 1, stop doing when  > 1
                # so lower the cover count when it goes to zero,  if it is negative then no need
                remaining_to_cover -= 1 #if p is covered, then reduce the size

        # Keeps advancing left until keywords_to_cover does not contain all
        # keywords.
        #once all the elements are covered, start to reduce the size
        while remaining_to_cover == 0:
            if result == Subarray(#check if the size of subarray is less, if less than save the new indices
                    start=-1,
                    end=-1) or right - left < result.end - result.start:
                result = Subarray(start=left, end=right)
            pl = paragraph[left]
            if pl in keywords:# Keeps advancing left until keywords_to_cover does not contain all elements in the set
                keywords_to_cover[pl] -= 1
                if keywords_to_cover[pl] == 0:#so increase the cover only when it goes above zero
                    remaining_to_cover += 1
            left += 1
    return result

#this one tackles duplicates in the keywords, see leetcode https://leetcode.com/problems/minimum-window-substring/submissions/
def find_smallest_subarray_covering_set(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:

        # keywords_to_cover = collections.Counter(keywords)
        if len(paragraph) < len(keywords):
            return ""
        keywords_to_cover = {x: 0 for x in keywords} # here we update that element has covered when its count becomes 1
        KeyCountNeeded = collections.Counter(keywords) #desired count per character needed
        remaining_to_cover = len(keywords)
        keywords = set(keywords)
        result = Subarray(start=-1, end=-1)
        left = 0
        for right, p in enumerate(paragraph):
            if p in keywords:#keyword is a set, lookup is O(1)
                keywords_to_cover[p] += 1#that specific element in the set can occur many times in the subarray
                if keywords_to_cover[p] <= KeyCountNeeded[p]: #keep updating untill desired count reached
                    remaining_to_cover -= 1 #if p is covered, then reduce the size

            # Keeps advancing left until keywords_to_cover does not contain all
            # keywords.
            #once all the elements are covered, start to reduce the size
            while remaining_to_cover == 0:
                if result == Subarray(#check if the size of subarray is less, if less than save the new indices
                        start=-1,
                        end=-1) or right - left < result.end - result.start:
                    result = Subarray(start=left, end=right)
                pl = paragraph[left]
                if pl in keywords:# Keeps advancing left until keywords_to_cover does not contain all elements in the set
                    keywords_to_cover[pl] -= 1
                    if keywords_to_cover[pl] < KeyCountNeeded[pl]:#so increase the cover only when it goes below deisred count
                        remaining_to_cover += 1
                left += 1
        return result



@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure('Index out of range')

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure('Not all keywords are in the range')

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            '12-06-smallest_subarray_covering_set.py',
            'smallest_subarray_covering_set.tsv',
            find_smallest_subarray_covering_set_wrapper))
