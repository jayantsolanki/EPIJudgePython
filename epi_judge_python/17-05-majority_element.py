from typing import Iterator
import collections
from test_framework import generic_test


"""
Leetcode: 169. Majority Element
https://leetcode.com/problems/majority-element/
Check https://leetcode.com/problems/majority-element-ii/
Write a program that makes a single pass over the sequence and identifies the majority element.
Remember majority means count  > n/2. Hence only the algo will work
Logic:
    You can solve it in O(n) space and time using hashmap to track the count.
    For improved space:

    Boyer-Moore Voting Algorithm
    To figure out a 
    O(1) space requirement, we would need to get this simple intuition first. For an array of length n:

        There can be at most one majority element which is more than ⌊n/2⌋ times.
        There can be at most two majority elements which are more than ⌊n/3⌋ times.
        There can be at most three majority elements which are more than ⌊n/4⌋ times.
    Since majority here means count > n/2, hence we just maintain the count of element being encountered
    We initialize count of first element to 1, if the next element is same, we increament the count, else decrement
    If after decrement the count is zero, we reintialize the count to 1 again for the current item and carry on.
    The last remaining element will be the majority. Because rest of the other elements wont be able to cancel out the
    count of the majority element.
    Time O(n), Space O(1)
"""
#original
def majority_search_ori(stream: Iterator[str]) -> str:

    candidate_count = 0
    for it in stream:
        if candidate_count == 0:
            candidate, candidate_count = it, candidate_count + 1
        elif candidate == it:
            candidate_count += 1
        else:
            candidate_count -= 1
    return candidate


#using hashmap

def majority_search_hash(stream: Iterator[str]) -> str:
    counter_map = collections.defaultdict(int)#int important
    maxCount, maxValue = 0, None
    for item in iter(stream):
        counter_map[item] += 1
        if counter_map[item] > maxCount:
            maxCount = counter_map[item]
            maxValue = item
    return maxValue

#my take on improved space

def majority_search(stream: Iterator[str]) -> str:
    current_count = 0
    current_val = None
    
    for item in stream:
        if current_val is None:
            current_count += 1
            current_val = item
        else:
            if current_count == 0:
                current_val = item
                current_count += 1
            elif current_val == item:
                current_count += 1
            else:
                current_count -= 1
            
    return current_val



def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('17-05-majority_element.py',
                                       'majority_element.tsv',
                                       majority_search_wrapper))
