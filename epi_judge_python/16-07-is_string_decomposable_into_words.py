import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

"""
Leetcode: 139. Word Break
https://leetcode.com/problems/word-break/
This problem is similar to https://leetcode.com/problems/partition-equal-subset-sum/, type of knapsack

Building search index for domains
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated 
sequence of one or more dictionary words. Note that the same word in the dictionary may be reused multiple times in the 
segmentation.
Example
    Input: s = "leetcode", wordDict = ["leet","code"]
    Output: true
    Explanation: Return true because "leetcode" can be segmented as "leet code"

"""

def decompose_into_dictionary_words_ori(domain: str,
                                    dictionary: Set[str]) -> List[str]:

    # When the algorithm finishes, last_length[i] != -1 indicates domain[:i +
    # 1] has a valid decomposition, and the length of the last string in the
    # decomposition is last_length[i].
    last_length = [-1] * len(domain)
    for i in range(len(domain)):
        # If domain[:i + 1] is a dictionary word, set last_length[i] to the
        # length of that word.
        if domain[:i + 1] in dictionary:
            last_length[i] = i + 1
            continue

        # If domain[:i + 1] is not a dictionary word, we look for j < i such
        # that domain[: j + 1] has a valid decomposition and domain[j + 1:i + 1]
        # is a dictionary word. If so, record the length of that word in
        # last_length[i].
        for j in range(i):
            if last_length[j] != -1 and domain[j + 1:i + 1] in dictionary:
                last_length[i] = i - j
                break

    decompositions = []
    if last_length[-1] != -1:
        # domain can be assembled by dictionary words.
        idx = len(domain) - 1
        while idx >= 0:
            decompositions.append(domain[idx + 1 - last_length[idx]:idx + 1])
            idx -= last_length[idx]
        decompositions = decompositions[::-1]
    print(domain, last_length, decompositions)
    return decompositions

#my way, topdown
# Time complexity in all: O(N.K.L), L because of splicing/substring, L is average length of spliced substring
#Space: O(N)
def decompose_into_dictionary_words_mem(domain: str,
                                    dictionary: Set[str]) -> List[str]:
    location_index = [-1] * len(domain)
    @functools.cache
    def dp(i):
        if i < 0:
            return True
        else:
            for word in dictionary:
                #just like knapsack, where we need to make sure that j is >= current weight (len(word))
                if (i >= len(word) - 1 and dp(i - len(word))):#need to make sure that i is not less than given word size
                    if (domain[i - len(word) + 1: i + 1] == word):
                        location_index[i] = len(word) #this will store the len of string found, optional
                        return True
            return False 

    result = dp(len(domain) - 1)
    # reconstruct the dictionary words used from string
    words = []
    if result:
        index = len(domain)  - 1
        while index >= 0:
            if location_index[index] != -1:
                words.append(domain[index - location_index[index] + 1: index + 1])
                index -= location_index[index]
    # print(words[::-1])
    return words[::-1]

def decompose_into_dictionary_words(s: str, wordDict: List[str]) -> bool:
    m = len(s)
    location_index = [-1] * len(s)
    cache = [False] * (m + 1)
    cache[-1] = True#for padding, 0 length word can be created with 0 string in the dictionary, 
    for i in range(m):
        for word in wordDict:
            #just like knapsack, where we need to make sure that j is >= current weight (len(word))
            if (i >= len(word) - 1 and cache[i - len(word)]):#need to make sure that i is not less than given word size
                if (s[i - len(word) + 1: i + 1] == word):
                    location_index[i] = len(word)
                    cache[i] =  True
                    break#important
    # reconstruct the dictionary words used from string
    words = []
    if cache[m - 1]:
        index = len(s)  - 1
        while index >= 0:
            if location_index[index] != -1:
                words.append(s[index - location_index[index] + 1: index + 1])
                index -= location_index[index]
    return words[::-1]

#variant 2:
"""
May be we can use leetcode 647. Palindromic Substrings and then check for each palindrome if they can we decompose into given dictionary
https://leetcode.com/problems/palindromic-substrings/
"""


@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            '16-07-is_string_decomposable_into_words.py',
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
