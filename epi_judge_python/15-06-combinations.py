from typing import List

from test_framework import generic_test, test_utils


def combinations(n: int, k: int) -> List[List[int]]:
    # TODO - you fill in here.
    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            '15-06-combinations.py',
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
