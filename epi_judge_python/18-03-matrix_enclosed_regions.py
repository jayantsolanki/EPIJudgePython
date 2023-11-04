import collections
from typing import List

from test_framework import generic_test

"""
Leetcode 130. Surrounded Regions
https://leetcode.com/problems/surrounded-regions/
Let A be a 2-D array whose entries are either W or B. Write a program that takes A, and replaces all Ws 
that cannot reach the boundary with a B.
We do the inverse of what is asked. We focus on identifying those Ws which can reach the boundries. We mark 
those W with some else value 'T' using BFS. THen later on once the while loop is done, we replace those T with W, 
and rest of the values are renamed 'B'
Time : O(mn) 
Space: 1
"""
#My take
def fill_surrounded_regions_simple(board: List[List[str]]) -> None:
    m, n = len(board), len(board[0])
    node_queue = collections.deque()
    #getting all the boundaries nodes into the queue
    #adding first and last row nodes
    for j in range(n):
        node_queue.append((0, j))
        node_queue.append((m + ~0, j)) #last row
    #adding first and last column nodes
    for i in range(1, m - 1):#excluding row 0 and last row elements
        node_queue.append((i, 0))
        node_queue.append((i, n + ~0)) #last column, if board[i][-1] == 'W':
    motions = [(0, 1), (0, - 1), (1, 0), (-1, 0)]
    #now start the BFS, we Find those W which starts from boundaries and we need to preserve them
    # we mark them with other value 'T', rest of the values wil be converted into B after end of while loop

    while node_queue:
        x, y = node_queue.popleft()
        if board[x][y] != 'W' : #only allow element with W
            continue
        board[x][y] = "T"
        for motion in motions:
            if 0 <= x + motion[0] < m and 0 <= y + motion[1] < n and board[x + motion[0]][y + motion[1]] == 'W':
                node_queue.append((x + motion[0], y + motion[1]))
    #now replace every remaining W 
    
    board[:] = [ ['W' if board[i][j] == 'T' else 'B' for j in range(n)] for i in range(m)]
    return board
#another take 02OCT2023, you can filter the cell in the initial for loop itself
def fill_surrounded_regions(board: List[List[str]]) -> None:
    m, n = len(board), len(board[0])
    node_queue = collections.deque()
    #getting all the boundaries nodes into the queue
    #adding first and last row nodes
    for j in range(n):
        if board[0][j] == 'W':
            node_queue.append((0, j))
        if board[-1][j] == 'W':
            node_queue.append((m + ~0, j)) #last row
    #adding first and last column nodes
    for i in range(1, m - 1):#excluding row 0 and last row elements
        if board[i][0] == 'W':
            node_queue.append((i, 0))
        if board[i][n + ~0] == 'W':#if board[i][-1] == 'W':
            node_queue.append((i, n + ~0)) #last column
    motions = [(0, 1), (0, - 1), (1, 0), (-1, 0)]
    #now start the BFS, we Find those W which starts from boundaries and we need to preserve them
    # we mark them with other value 'T', rest of the values wil be converted into B after end of while loop

    while node_queue:
        x, y = node_queue.popleft()
        if board[x][y] == 'T' : #only allow elements with W
            continue
        board[x][y] = "T"
        for motion in motions:
            if 0 <= x + motion[0] < m and 0 <= y + motion[1] < n and board[x + motion[0]][y + motion[1]] == 'W':
                node_queue.append((x + motion[0], y + motion[1]))
    #now replace every remaining W 
    
    board[:] = [ ['W' if board[i][j] == 'T' else 'B' for j in range(n)] for i in range(m)]
    return board


# fill_surrounded_regions([['B', 'B', 'B', 'B'], ['W', 'B', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'B', 'B', 'B']])

def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('18-03-matrix_enclosed_regions.py',
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
