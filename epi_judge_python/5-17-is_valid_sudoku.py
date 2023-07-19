import collections
import math
from typing import List

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts. Specifically check if no rows or 
# columns contains duplicates
# 0 value in the entry means its blank
# we need to check 9 rows, 9 columns, and 9 sub squares
"""
We need to check nine rows, nine colmns and 9 subgrids (those squares consisting of 9 cells), 
to ensure no duplicates occurs
Time: O(n^2), space complexity: O(n)
Derivation of time: O(n^2) (rows) + O(n^2) (columns) + O(n^2/(n^0.5)^2 X (n^0.5)^2) (for subgrids) = O(n)^2
"""
def is_valid_sudoku_v1(partial_assignment: List[List[int]]) -> bool:

    # Return True if subarray
    # partial_assignment[start_row:end_row][start_col:end_col] contains any
    # duplicates in {1, 2, ..., len(partial_assignment)}; otherwise return
    # False.
    def has_duplicate(block):
        #block = list(filter(lambda x: x != 0, block))#this one filters out cell which has zero value, just check only 
        #filled ones
        block = [i for i in block if i!=0] #alternate of above line
        return len(block) != len(set(block))#matches length of a normal block with overall set where duplicates in block are removed

    n = len(partial_assignment)
    # Check row and column constraints.
    if any(
            has_duplicate([partial_assignment[i][j] for j in range(n)])
            or has_duplicate([partial_assignment[j][i] for j in range(n)])
            for i in range(n)):
        return False

    # Check region constraints.
    region_size = int(math.sqrt(n))
    return all(not has_duplicate([
        partial_assignment[a][b]
        for a in range(region_size * I, region_size * (I + 1))
        for b in range(region_size * J, region_size * (J + 1))
    ]) for I in range(region_size) for J in range(region_size))

#another version
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:

    # Return True if subarray
    # partial_assignment[start_row:end_row][start_col:end_col] contains any
    # duplicates in {1, 2, ..., len(partial_assignment)}; otherwise return
    # False.
    def has_duplicate(block):
        #block = list(filter(lambda x: x != 0, block))#this one filters out cell which has zero value, just check only 
        #filled ones
        block = [i for i in block if i!=0] #alternate of above line
        return len(block) != len(set(block))#matches length of a normal block with overall set where duplicates in block are removed

    n = len(partial_assignment)
    # Check row and column constraints.
    for i in range(n):
        if has_duplicate([partial_assignment[i][j] for j in range(n)]):#row
            return False
        if has_duplicate([partial_assignment[j][i] for j in range(n)]):#column
            return False

    # Check region constraints.
    #this also has to run 81 times, hence four for loops used, for grid size 3
    region_size = int(math.sqrt(n))
    for I in range(region_size): #decides row-wise subgrid blocks to process
        for J in range(region_size): #decides columns wise subgrid blocks to process
            if has_duplicate([
                partial_assignment[a][b]
                for a in range(region_size * I, region_size * (I + 1))#going through each sub grid 0 - 2, 3-5, 6- 8, top is 0 - 2
                for b in range(region_size * J, region_size * (J + 1))#visit each cell in that subgrid
            ]):
                return False
    #alternate
    # for I in range(region_size): #decides row-wise subgrid blocks to process
    #     for J in range(region_size): #decides columns wise subgrid blocks to process
    #         temp = []
    #         for i in range(region_size * I, region_size * I + region_size):
    #             for j in range(region_size * J, region_size * J + region_size):
    #                 temp.append(partial_assignment[i][j])
    #         if has_duplicate(temp):
    #             return False
    return True


# Pythonic solution that exploits the power of list comprehension.
def is_valid_sudoku_pythonic(partial_assignment):
    region_size = int(math.sqrt(len(partial_assignment)))
    return max(collections.Counter(
        k for i, row in enumerate(partial_assignment)
        for j, c in enumerate(row) if c != 0
        for k in ((i, str(c)), (str(c), j),
                  (i // region_size, j // region_size, str(c)))).values(),
               default=0) <= 1



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('5-17-is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
