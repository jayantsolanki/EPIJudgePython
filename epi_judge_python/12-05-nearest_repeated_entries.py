import typing
from typing import Dict, List

from test_framework import generic_test

"""
Write a program to find distance of closest pair of same word if they were repeated
Time: O(n), Space: O(d), d is unique words encountered in paragraph
Logic:
    We basically keep looking for min distance found so far when we encounter a already existing word key
    We only care of the two recently encountred positions of same key, hence we keep on updting the index
    of the key with latest index
"""
def find_nearest_repetition_v2(paragraph: List[str]) -> int:

    word_to_latest_index: Dict[str, int] = {}
    nearest_repeated_distance = float('inf')
    for i, word in enumerate(paragraph):
        if word in word_to_latest_index: #if key exist beforehand
            latest_equal_word = word_to_latest_index[word]
            nearest_repeated_distance = min(nearest_repeated_distance,
                                            i - latest_equal_word)
        word_to_latest_index[word] = i
    return typing.cast(int, nearest_repeated_distance
                       ) if nearest_repeated_distance != float('inf') else -1


#my take
def find_nearest_repetition(paragraph: List[str]) -> int:

    word_mapper = {}
    min_encountered = float("Inf")
    for index, value in enumerate(paragraph):
        if value not in word_mapper:
            word_mapper[value] = index
        else:
            min_encountered = min(index - word_mapper[value], min_encountered)
            word_mapper[value] = index #also update the old index with new
    return min_encountered if min_encountered != float("Inf") else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('12-05-nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
