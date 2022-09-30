import copy
import functools
import itertools
import math
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

"""
Leetcode: 37. Sudoku Solver
https://leetcode.com/problems/sudoku-solver/
Implement a Sudoku solver.
Logic: #similar to n-queen
    Traverse the 2-D array entries one at a time, if empty, we try each value, then we check the validity of that specific cell
    across row, column and subgrid, if right we recurse further else backtrack
Time: https://github.com/amitkumar50/Code-examples/blob/master/DS_Questions/Questions/vectors_arrays/2d-grid/Sudoku_Solver/4x4Board/README.md#co
Time complexity is constant here since the board size is fixed and there is no N-parameter to measure. Though let's discuss the number of operations needed : (9!)^9
 . Let's consider one row, i.e. not more than 99 cells to fill. There are not more than 9 possibilities for the first number to put, not more than 9 x 8 for the second one, not more than 9x 8 x 7 for the third one etc. In total that results in not more than 9! possibilities for a just one row, that means not more than (9!)^9 operations in total
In other way each row can be filled in 9!, there are 9 rows, hence (9!)^9
Space Complexity: O(m*n)
Space Complexity Expl: The space was the recursion stack, which for an empty grid can stack up to (9 * 9) or (m * n).

"""
def solve_sudoku_ori(partial_assignment: List[List[int]]) -> bool:
    def solve_partial_sudoku(i, j):
        if i == len(partial_assignment):
            i = 0  # Starts a row.
            j += 1
            if j == len(partial_assignment[i]):
                return True  # Entire matrix has been filled without conflict.

        # Skips nonempty entries.
        if partial_assignment[i][j] != empty_entry:
            return solve_partial_sudoku(i + 1, j)

        def valid_to_add(i, j, val):
            # Check row constraints.
            if any(val == partial_assignment[k][j]
                   for k in range(len(partial_assignment))):
                return False

            # Check column constraints.
            if val in partial_assignment[i]:
                return False

            # Check region constraints., get the region they belong to
            region_size = int(math.sqrt(len(partial_assignment)))
            I = i // region_size
            J = j // region_size
            return not any(
                val == partial_assignment[region_size * I +
                                          a][region_size * J + b]
                for a, b in itertools.product(range(region_size), repeat=2))

        for val in range(1, len(partial_assignment) + 1):
            # It's substantially quicker to check if entry val with any of the
            # constraints if we add it at (i,j) adding it, rather than adding it and
            # then checking all constraints. The reason is that we know we are
            # starting with a valid configuration, and the only entry which can
            # cause a problem is entry val at (i,j).
            if valid_to_add(i, j, val):
                partial_assignment[i][j] = val
                if solve_partial_sudoku(i + 1, j):
                    return True
        partial_assignment[i][j] = empty_entry  # Undo assignment.
        return False

    empty_entry = 0
    return solve_partial_sudoku(0, 0)

#changed the subgrid validation technique, moved out the validation method outside of backtrack method
def solve_sudoku(partial_assignment: List[List[int]]) -> bool:
    def valid_to_add(i, j, val):
        # Check column constraints.
        if any(val == partial_assignment[k][j]
                for k in range(len(partial_assignment))):
            return False

        # Check row constraints.
        if val in partial_assignment[i]:
            return False

        # Check region constraints.
        #a bit simpler
        region_size = int(math.sqrt(len(partial_assignment)))
        I = i // region_size
        J = j // region_size
        for a in range(region_size * I, region_size * (I + 1)):
            for b in range(region_size * J, region_size * (J + 1)):
                if partial_assignment[a][b] == val:
                    return False
        return True
    #backtrack method
    def solve_partial_sudoku(i, j): # we are filling the sudoku columnwise (vertically)
        if i == len(partial_assignment):#if reached the end of rows, switch to next column, go back to top row
            i = 0  # Starts a row.
            j += 1
            if j == len(partial_assignment[i]): #if reached end of column, end
                # print(partial_assignment)
                return True  # Entire matrix has been filled without conflict.

        # Skips nonempty entries.
        if partial_assignment[i][j] != empty_entry:
            return solve_partial_sudoku(i + 1, j)


        #start putting values from 1 - 9 in cell i, j
        for val in range(1, len(partial_assignment) + 1):# if it 9x9 grid, we will check for values from 1- 9
            # It's substantially quicker to check if entry val with any of the
            # constraints if we add it at (i,j) adding it, rather than adding it and
            # then checking all constraints. The reason is that we know we are
            # starting with a valid configuration, and the only entry which can
            # cause a problem is entry val at (i,j).
            if valid_to_add(i, j, val):#check for validity before assigning #pruning too, similar to n-queen
                partial_assignment[i][j] = val
                if solve_partial_sudoku(i + 1, j): # we are filling the sudoku columnwise (vertically)
                    # print(partial_assignment)
                    return True
        #if here, that means, above numbers failed, go back to previous row and try again
        partial_assignment[i][j] = empty_entry  # Undo assignment.
        return False

    empty_entry = 0
    return solve_partial_sudoku(0, 0)


solve_sudoku([[5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0], [0, 9, 8, 0, 0, 0, 0, 6, 0], [8, 0, 0, 0, 6, 0, 0, 0, 3], [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6], [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5], [0, 0, 0, 0, 8, 0, 0, 7, 9]])


def assert_unique_seq(seq):
    seen = set()
    for x in seq:
        if x == 0:
            raise TestFailure('Cell left uninitialized')
        if x < 0 or x > len(seq):
            raise TestFailure('Cell value out of range')
        if x in seen:
            raise TestFailure('Duplicate value in section')
        seen.add(x)


def gather_square_block(data, block_size, n):
    block_x = (n % block_size) * block_size
    block_y = (n // block_size) * block_size

    return [
        data[block_x + i][block_y + j] for j in range(block_size)
        for i in range(block_size)
    ]


@enable_executor_hook
def solve_sudoku_wrapper(executor, partial_assignment):
    solved = copy.deepcopy(partial_assignment)

    executor.run(functools.partial(solve_sudoku, solved))

    if len(partial_assignment) != len(solved):
        raise TestFailure('Initial cell assignment has been changed')

    for (br, sr) in zip(partial_assignment, solved):
        if len(br) != len(sr):
            raise TestFailure('Initial cell assignment has been changed')
        for (bcell, scell) in zip(br, sr):
            if bcell != 0 and bcell != scell:
                raise TestFailure('Initial cell assignment has been changed')

    block_size = int(math.sqrt(len(solved)))
    for i, solved_row in enumerate(solved):
        assert_unique_seq(solved_row)
        assert_unique_seq([row[i] for row in solved])
        assert_unique_seq(gather_square_block(solved, block_size, i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('15-10-sudoku_solve.py', 'sudoku_solve.tsv',
                                       solve_sudoku_wrapper))
