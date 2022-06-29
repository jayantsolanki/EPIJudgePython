from typing import List
import copy
from test_framework import generic_test

"""
There can be many solutions, jfind all
Backtracking intro: https://cs.lmu.edu/~ray/notes/backtracking/
Leetcode 51 https://leetcode.com/problems/n-queens/solution/
Leetcode 52 Second type: https://leetcode.com/problems/n-queens-ii/
Write a program which returns all distnct non-attacking placements of n queens on a n x n chessboard, n is input
Logic:
    Ist important observation: Each queen will occupy one full row. There can't be placement greater factorial(n).
    Trick is to move from one row to another if the move is valid, else back track.
    Since we never place two queens on same row, a much faster solution is to enumerate placements that use distinct rows. Such
    placements will never lead to conflict in rows, but may lead to conflict in columns or diagonals
    This is a perfect problem for backtracking - place the queens one by one, and when all possibilities are 
    exhausted, backtrack by removing a queen and placing it elsewhere
    Goal is to find ways to make sure the move is valid
    #for validity, for each new placement, check it with previous placements, invalid if
        1 - check for diagonality by making sure that x1 - x2 == y1 - y2
        2 = check if c - col == 0, that is belonging to same column
    You move from one row to another, iterate in the col values to find valid position, then move to next row, else back track
    and find better col value. Keep permutating
"""

def n_queens_ori(n: int) -> List[List[int]]:
    def solve_n_queens(row):
        if row == n:
            # All queens are legally placed.
            result.append(col_placement[:]) #this also valid
            #result.append(col_placement.copy())#its a copy, because col_placement will keep on changing
            return
        for col in range(n):
            # Test if a newly placed queen will conflict any earlier queens
            # placed before.
            if all(
                    abs(c - col) not in (0, row - i) #is same column then c -col == 0, which is in that tuple
                    #if diagonal then abs(c - col) == (i - row), since diagonal has slope of 1, i1 - i2 = j1 - j2
                    for i, c in enumerate(col_placement[:row])):
                col_placement[row] = col
                solve_n_queens(row + 1)

    result: List[List[int]] = []
    col_placement = [0] * n
    solve_n_queens(0) #for n = 4, rows = 0, 1, 2, 3
    return result

# [["".join(['Q' if x == c else '.' for x in range(4)]) for c in solution] for solution in a]
#a bit simple of validity check
def n_queens(n: int) -> List[List[int]]:
    def validity(col, row):
        for i, c in enumerate(col_placement[:row]):
            #check diagonal
            if (abs(i - row) == abs(col - c)):#tan 45 is 1
                return False
            if c == col:#same column
                return False
        return True
    def solve_n_queens(row):
        if row == n:
            # All queens are legally placed.
            result.append(col_placement[:]) #this also valid
            #result.append(col_placement.copy())#its a copy, because col_placement will keep on changing
            return
        for col in range(n):
            # Test if a newly placed queen will conflict any earlier queens
            # placed before.
            # print(row, col, validity(col, row))
            if validity(col, row):
                col_placement[row] = col
                solve_n_queens(row + 1)

    result: List[List[int]] = []
    col_placement = [0] * n
    solve_n_queens(0) #for n = 4, rows = 0, 1, 2, 3
    return result

n_queens(4)

#variant 1
"""
Compute the number of nonattacking placements of n queens on n xn cheesboard

"""
def totalNQueens(n: int) -> int:
    def validity(col, row):
        for i, c in enumerate(col_placement[:row]):
            #check diagonal
            if (abs(i - row) == abs(col - c)):#tan 45 is 1
                return False
            if c == col:#same column
                return False
        return True
    def solve_n_queens(row):
        if row == n:
            # All queens are legally placed.
            result[0] += 1 #this also valid
            #result.append(col_placement.copy())#its a copy, because col_placement will keep on changing
            return
        for col in range(n):
            # Test if a newly placed queen will conflict any earlier queens
            # placed before.
            # print(row, col, validity(col, row))
            if validity(col, row):
                col_placement[row] = col
                solve_n_queens(row + 1)

    result =  [0]
    col_placement = [0] * n
    solve_n_queens(0) #for n = 4, rows = 0, 1, 2, 3
    return result[0] 

#variant 2
"""
Kinda a brute force with recursion
https://www.geeksforgeeks.org/minimum-queens-required-to-cover-all-the-squares-of-a-chess-board/
Compute the smallest number of queens that can be placed to attack each uncovered square
Logic:
    Step 1: Starting from any corner square of the board, find an ‘uncovered’ square (Uncovered square is a square which isn’t attacked by any of the queens already placed). If none found, goto Step 4.
    Step 2: Place a Queen on this square and increment variable ‘count’ by 1.
    Step 3: Repeat step 1.
    Step 4: Now, you’ve got a layout where every square is covered. Therefore, the value of ‘count’ can be the answer. However, you might be able to do better, as there might exist a better layout with lesser number of queens. So, store this ‘count’ as the best value till now and proceed to find a better solution.
    Step 5: Remove the last queen placed and place it in the next ‘uncovered’ cell.
    Step 6: Proceed recursively and try out all the possible layouts. Finally, the one with the least number of queens is the answer.

    Basically trick is to identify if there are any valid spaces left every time you place one queen in the matrix.
    If no space left, then store that answer
    Important part is checking the space
"""
def totalNQueens_attack(n: int) -> int:
    def check_any_placement_left():
        for i in range(n):
            for j in range(n):
                if validity(i, j):#there are some places still left
                    return False
        return True
    def validity(row, col):
        #check for queen across column 'column
        for i in range(n):
            if board[i][col]:
                return False
        #check for queen across row 'row'
        for j in range(n):
            if board[row][j]:
                return False
        # check across diagonal
        for i in range(n):
            #moving right top
            if row - i >= 0 and i + col < n and board[row - i][i+col]:
                return False
            #moving left bottom
            elif row + i < n and col - i >= 0 and board[row + i][col - i]:
                return False
            #moving left top
            elif row - i >=0 and col - i >= 0 and board[row - i][col - i]:
                return False
            #moving bottom right
            elif row + i < n and col + i < n and board[row + i][col + i]:
                return False
        return True
    def solve_n_queens(queen_count=0):
        if queen_count >= smallest_count[0]:
            return #no need to go further
        #check all the places are attacked
        if check_any_placement_left():
            result.append(copy.deepcopy(board))
            smallest_count[0] = queen_count
            return
        for row in range(n):
            for col in range(n):
                if validity(row, col):
                    board[row][col] = True
                    solve_n_queens(queen_count + 1)
                    board[row][col] = False
                    
    smallest_count = [float('Inf')]
    result = []
    board = [[False for i in range(n)] for j in range(n)]
    solve_n_queens()
    # return (result, smallest_count[0])
    return (smallest_count[0])

# totalNQueens_attack(11)#answer is 5, not 7 for n == 11
totalNQueens_attack(5)#answer is 3, not 4 for n == 5
# totalNQueens_attack(4)#answer is 3, not 4 for n == 4

def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('15-03-n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))

def combine(n, k):   
    sol=[]
    def backtrack(remain,comb,nex):
        # solution found
        if remain==0:
            sol.append(comb.copy())
        else:
            # iterate through all possible candidates
            for i in range(nex,n+1):
                # add candidate
                comb.append(i)
                #backtrack
                backtrack(remain-1,comb,i+1)
                # remove candidate
                comb.pop()
        
    backtrack(k,[],1)
    return sol

combine(5, 2)