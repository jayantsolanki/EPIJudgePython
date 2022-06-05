from typing import List

from test_framework import generic_test

# search for an item in a 2-d sorted array. 
"""
A 2d array of m x n is sorted if it has non decreasing row and non decreasing columns
A normal binary search for each row and overall will take O(mlogn)
Technique also called Search Space Reduction
Logic:
    A good rule for design is to look for extreme cases
    1 - Compare search element x with A[0][n - 1] top-right corner
        a - if x > A[0][n-1] then x is greater than every elements in Row 0
        b - if x < A[0][n-1] then x is smaller than every elements in column n -1, hence move one place in that column
    2 - Compare search element x with A[m -1][0] bottom-left corner
        a - if x > A[m -1][0] then x is greater than every elements in Column 0
        b - if x < A[m -1][0] then x is smaller than every elements in Row m - 1, , hence move one place in that row
    You may use either 1 or 2 for your logic
Time: O(m + n), each iteration removes a row or column, so at max we inspedct m+n-1 elements
"""
def matrix_search(A: List[List[int]], x: int) -> bool:

    row, col = 0, len(A[0]) - 1  # Start from the top-right corner. Using Logic point 1
    # Keeps searching while there are unclassified rows and columns.
    while row < len(A) and col >= 0: #overall row index is increasing toward m and column index is decreasing towards 0
        if A[row][col] == x:
            return True
        elif A[row][col] < x:
            row += 1  # Eliminate this row. moves to next element in that column col
        else:  # A[row][col] > x.
            col -= 1  # Eliminate this column.
    return False

#variant1
# https://leetcode.com/problems/search-a-2d-matrix/solution/


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('11-06-search_row_col_sorted_matrix.py',
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
