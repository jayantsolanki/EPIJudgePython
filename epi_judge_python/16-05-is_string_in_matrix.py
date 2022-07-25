import functools
from typing import List

from test_framework import generic_test

"""
Write a program that takes  as arugments a 2d array and a 1d array, and chgecks whether the 1d array occurs in the 2d array .
Logic:
    Use Recursion with memoization.
    Similar to n-queen problem, start with the first poin tin 2d which matches with the 1d array and carry one from there
Time and Space: O(mnl), l is size of pattern
"""
def is_pattern_contained_in_grid_ori(grid: List[List[int]],
                                 pattern: List[int]) -> bool:
    @functools.lru_cache(None)
    def is_pattern_suffix_contained_starting_at_xy(x, y, offset):
        if len(pattern) == offset:
            # Nothing left to complete.
            return True

        # Early return if (x, y) lies outside the grid or the character
        # does not match or we have already tried this combination.
        if (not (0 <= x < len(grid) and 0 <= y < len(grid[x]))
                or grid[x][y] != pattern[offset]):
            return False

        return any(
            is_pattern_suffix_contained_starting_at_xy(*next_xy, offset + 1)
            for next_xy in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)))

    return any(
        is_pattern_suffix_contained_starting_at_xy(i, j, offset=0)
        for i in range(len(grid)) for j in range(len(grid[i])))
#my take
def is_pattern_contained_in_grid(grid: List[List[int]],
                                 pattern: List[int]) -> bool:
    m, n = len(grid), len(grid[0])
    @functools.cache
    def dp(i, j, offset):
        if offset == len(pattern): #sequence processed, completed
            return True
        elif i == m or j == n:
            return False
        elif i < 0 or j < 0:
            return False
        elif grid[i][j] != pattern[offset]:
            return False
        else:
            return dp(i - 1, j, offset + 1) | dp(i, j - 1, offset + 1) | dp(i + 1, j, offset + 1) | dp(i, j + 1, offset + 1)
            #above or below
            # if dp(i - 1, j, offset + 1):
            #     return True
            # if dp(i, j - 1, offset + 1):
            #     return True
            # if dp(i + 1, j, offset + 1):
            #     return True
            # if dp(i, j + 1, offset + 1):
            #     return True
            # return False

    for i in range(m):
        for j in range(n):
            if dp(i, j, 0):#looking for starting point
                return True
    return False





if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('16-05-is_string_in_matrix.py',
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
