from typing import List

from test_framework import generic_test
import collections


"""
Leetcode: 733. Flood Fill
https://leetcode.com/problems/flood-fill/

Implement a routine that takes an mxn Boolean array A together with an entry (x, y), and 
flips the color of the region associated with (x, y). 
Logic, similar to flood fill, check the neighbours value which are not equal to original value of the coordinate at x, y
start flipping them, and then match successive neighbours of those flipped cells
Time : O(mn) for DFS and BFS
Space: O(m + n) for BFS atmost, since there are atmost m + n vertices at the same distance from a given entry, same for DFS
"""
#DFS
def flip_color_dfs(sx: int, sy: int, image: List[List[bool]]) -> None:
    motions = [(0, 1), (0, - 1), (1, 0), (-1, 0)]
    m, n  = len(image), len(image[0])
    visited = set()
    def dfs(x, y):
        if (x, y) in visited:
            return
        else:
            image[x][y] = not image[x][y] #change the color
            visited.add((x, y))
            for motion in motions:
                if 0 <= x + motion[0] < m and 0 <= y + motion[1] < n and image[x + motion[0]][y + motion[1]] != image[x][y]:
                    dfs(x + motion[0], y + motion[1])
    dfs(sx, sy)
    return(image)

#dfs iterative
def flip_color(sx: int, sy: int, image: List[List[bool]]) -> None:
    motions = [(0, 1), (0, - 1), (1, 0), (-1, 0)]
    m, n  = len(image), len(image[0])
    visited = set()
    node_stack = [(sx, sy)]

    while node_stack:
        x, y = node_stack.pop()
        if (x, y) in visited:
            continue
        else:
            image[x][y] = not image[x][y] #change the color
            visited.add((x, y))
            for motion in motions:
                if 0 <= x + motion[0] < m and 0 <= y + motion[1] < n and image[x + motion[0]][y + motion[1]] != image[x][y]:
                    node_stack.append((x + motion[0], y + motion[1]))

    return(image)

#bfs
def flip_color_bfs(sx: int, sy: int, image: List[List[bool]]) -> None:
    motions = [(0, 1), (0, - 1), (1, 0), (-1, 0)]
    m, n  = len(image), len(image[0])
    visited = set()

    node_queue = collections.deque()
    node_queue.append((sx, sy))
    while node_queue:
        x, y = node_queue.popleft()
        if (x, y) in visited:
            continue
        else:
            image[x][y] = not image[x][y] #change the color
            visited.add((x, y))
            for motion in motions:
                if 0 <= x + motion[0] < m and 0 <= y + motion[1] < n and image[x + motion[0]][y + motion[1]] != image[x][y]:
                    node_queue.append((x + motion[0], y + motion[1]))

    return(image)


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('18-02-matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
