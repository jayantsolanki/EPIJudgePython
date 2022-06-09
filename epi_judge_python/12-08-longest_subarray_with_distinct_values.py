from typing import Dict, List

from test_framework import generic_test

"""
Logic:
    Use hash table to track latest index of any character, and use that to change the starting index of subarray
    whenever that character has been encountered again
Time: O(n)
"""
def longest_subarray_with_distinct_entries_original(A: List[int]) -> int:

    # Records the most recent occurrences of each entry.
    most_recent_occurrence: Dict[int, int] = {}
    longest_dup_free_subarray_start_idx = result = 0
    for i, a in enumerate(A):
        # Defer updating dup_idx until we see a duplicate.
        if a in most_recent_occurrence:
            dup_idx = most_recent_occurrence[a]
            # A[i] appeared before. Did it appear in the longest current
            # subarray? this line is important, make sure that if start index is greater than dup_idx, then ignore it
            if dup_idx >= longest_dup_free_subarray_start_idx:
                result = max(result, i - longest_dup_free_subarray_start_idx)
                longest_dup_free_subarray_start_idx = dup_idx + 1
        most_recent_occurrence[a] = i
    return max(result, len(A) - longest_dup_free_subarray_start_idx)

#practice

def longest_subarray_with_distinct_entries(A: List[int]) -> int:
    longest_subarray_yet_start_index = 0
    result = 0

    entries_pos = {}

    for index, entry in enumerate(A):
        if entry in entries_pos:
            dup_idx = entries_pos[entry] #get previously recorded index and check
            #if the previous is greater than equal to longest_subarray_yet_start_index
            if dup_idx >= longest_subarray_yet_start_index:
                result = max(result, index - longest_subarray_yet_start_index)
                longest_subarray_yet_start_index = dup_idx + 1 #this becomes the new start index, plus one, since index already contains that
        entries_pos[entry] = index #store most recent one
    return max(result, len(A) - longest_subarray_yet_start_index)

# longest_subarray_with_distinct_entries(['f', 's', 'f', 'e', 't', 'w', 'e', 'n', 'w', 'e'])

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            '12-08-longest_subarray_with_distinct_values.py',
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
