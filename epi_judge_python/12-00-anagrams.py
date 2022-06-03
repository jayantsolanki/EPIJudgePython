import collections
from typing import DefaultDict, List

from test_framework import generic_test, test_utils
import functools

#string_hash
def string_hash(s: str, modulus: int) -> int:
    mult = 997
    return functools.reduce(lambda v, c: (v * mult + ord(c)) % modulus, s, 0)

string_hash("jayant", 10)

"""
Write a program to group words into their anagrams
https://leetcode.com/problems/group-anagrams/
Logic:
    Anagram words have same letters after sorting, hence
    Sort each word you encounter, treat the sorted words as keys, add their original word to a hash table in the list form
    List form for each key is the grouping of those words
    Return the result in the form of a list of a list

Time: sorting each key is mlogm, where m is the largest number of characters in a string, sorting all keys is O(nmlogm)
    Insertion into the hashmap for each sorted key takes O(m), so for all words, insertion will be O(nm). 
    Hence total Time: O(nmlogm)

"""
def find_anagrams_v2(dictionary: List[str]) -> List[List[str]]:

    sorted_string_to_anagrams: DefaultDict[
        str, List[str]] = collections.defaultdict(list)
    for s in dictionary:
        # Sorts the string, uses it as a key, and then appends the original
        # string as another value into hash table.
        # https://towardsdatascience.com/python-pro-tip-start-using-python-defaultdict-and-counter-in-place-of-dictionary-d1922513f747
        https://realpython.com/python-defaultdict/
        sorted_string_to_anagrams[''.join(sorted(s))].append(s)

    return [
        group for group in sorted_string_to_anagrams.values()
        if len(group) >= 2
    ]
#easy one
def find_anagrams_simple(dictionary: List[str]) -> List[List[str]]:

    sorted_string_to_anagrams = {}
    # sorted_string_to_anagrams: DefaultDict[
    #     str, List[str]] = collections.defaultdict(list)
    for s in dictionary:
        # Sorts the string, uses it as a key, and then appends the original
        # string as another value into hash table.
        temp = ''.join(sorted(s))
        if temp not in sorted_string_to_anagrams:
            sorted_string_to_anagrams[temp] = [s]
        else:
            sorted_string_to_anagrams[temp].append(s)

    return [
        group for group in sorted_string_to_anagrams.values()
        if len(group) >= 2
    ]

#Variant 1, find anagrams in O(nm)
"""
Create key independent of sorted values, i think use the custom hash function created in previous algo\
    Logic:
        With prime mapping 2 strings are guaranteed to have different factors.
        https://stackoverflow.com/questions/18781106/generate-same-unique-hash-code-for-all-anagrams
        Pick a set of prime numbers (26 ofr alphabets, and one for space), as small as you like, the same size as your character set, and build a fast mapping function from your chars to that. Then for a given word, map each character into the matching prime, and multiply. finally, hash using the result.
"""

def find_anagrams_v1(dictionary: List[str]) -> List[List[str]]:

    sorted_string_to_anagrams = {}
    def string_hash_v2(s: str) -> int:
        primes_chrs_map = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131]
        key = 1
        for char in s:
            if char != ' ':
                key = key * primes_chrs_map[ord(char)- ord('a')]
            else:
                key = key * primes_chrs_map[-1]#assigning last prime for whitespace
        return key

    for s in dictionary:
        # Sorts the string, uses it as a key, and then appends the original
        # string as another value into hash table.
        temp = string_hash_v2(s)
        if temp not in sorted_string_to_anagrams:
            sorted_string_to_anagrams[temp] = [s]
        else:
            sorted_string_to_anagrams[temp].append(s)

    return [
        group for group in sorted_string_to_anagrams.values()
        if len(group) >= 2
    ]


#from leetcode
# https://leetcode.com/problems/group-anagrams/solution/
#Variant 1 alternate, find anagrams in O(nm)
# Two strings are anagrams if and only if their character counts (respective number of occurrences of each character) are 
# the same
# so create count array of each word, then count each alphabet in it, convert whole array into tuple and use it as a key
def find_anagrams(dictionary):
    # ans = collections.defaultdict(list)
    ans = {}
    for s in dictionary:
        count = [0] * 27#recreate count array everytime, thats a signature for each word
        for c in s:
            if c == " ":
                count[-1] += 1
            else:
                count[ord(c) - ord('a')] += 1
        temp = tuple(count)
        if temp not in ans:
            ans[tuple(count)] = [s]
        else:
            ans[tuple(count)].append(s)#list is mutable, hence we need to convert it into a tuple to use it as key
    return [words for words in ans.values() if len(words) >= 2]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            '12-00-anagrams.py',
            'anagrams.tsv',
            find_anagrams,
            comparator=test_utils.unordered_compare))
