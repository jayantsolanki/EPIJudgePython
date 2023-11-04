import collections
import copy
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


"""
Leetcode 505. The Maze II
https://leetcode.com/problems/the-maze-ii/
Given 2-D array maze with obstacles, black are obstacles and white are open cells. With designated entrance and exit,
find the path between them, if one exists.
Logic:
    You may use DFS or BFS, but DFS is easier to implement. Use an array to get store the cordinates path, and keep popping them
    in case the function returns false during backtrack.
"""

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

#this code is modifying the maze
def search_maze_ori(maze: List[List[int]], s: Coordinate,
                e: Coordinate) -> List[Coordinate]:

    # Perform DFS to find a feasible path.
    def search_maze_helper(cur):
        # Checks cur is within maze and is a white pixel.
        if not (0 <= cur.x < len(maze) and 0 <= cur.y < len(maze[cur.x])
                and maze[cur.x][cur.y] == WHITE):
            return False
        path.append(cur)
        maze[cur.x][cur.y] = BLACK
        if cur == e:
            return True

        if any(
                map(
                    search_maze_helper,
                    map(Coordinate, (cur.x - 1, cur.x + 1, cur.x, cur.x),
                        (cur.y, cur.y, cur.y - 1, cur.y + 1)))):
            return True
        # Cannot find a path, remove the entry added in path.append(cur).
        del path[-1]
        return False

    path: List[Coordinate] = []
    search_maze_helper(s)
    return path

#my implementation - dfs
def search_maze_v1(maze: List[List[int]], s: Coordinate,
                e: Coordinate) -> List[Coordinate]:
    path = []
    motions = [Coordinate(0, -1), Coordinate(0, 1), Coordinate(1, 0), Coordinate(-1, 0)]
    # here modify the maze cell to add black color for visited cells, so that no cycle is formed accidently
    #no need to track visited set because of modifying maze
    #you may wanna use tuple set, if you dont want to modify the maze
    # visit
    def dfs(node):
        if maze[node.x][node.y] == BLACK:#visited already or a obstacle
            return False        
        else:
            maze[node.x][node.y] = BLACK#mark it as visited
            path.append(node)
            if node == e: #path found
                return True
            for motion in motions:
                if 0 <= node.x + motion.x < len(maze) and 0 <= node.y + motion.y < len(maze[0]):#valid motions only
                    if dfs(Coordinate(node.x + motion.x, node.y + motion.y)):
                        return True
            path.pop()
            return False
    dfs(s)
    return path

#second version, without modifying original maze , some interviews dont like modifying the original data, like amazon
#my implementation
def search_maze_dfs(maze: List[List[int]], s: Coordinate,
                e: Coordinate) -> List[Coordinate]:
    path = []
    visited = set()#store the tuple
    motions = [Coordinate(0, -1), Coordinate(0, 1), Coordinate(1, 0), Coordinate(-1, 0)]
    def dfs(node):
        if maze[node.x][node.y] == BLACK or (node.x, node.y) in visited:#visited already or a obstacle
            return False  
        # elif (node.x, node.y) in visited:
        #     return False      
        else:
            # maze[node.x][node.y] = BLACK#mark it as visited
            visited.add((node.x, node.y))#marking cell as visited
            path.append(node)
            if node == e: #path found
                return True
            for motion in motions:
                if 0 <= node.x + motion.x < len(maze) and 0 <= node.y + motion.y < len(maze[0]):#valid motions only
                    if dfs(Coordinate(node.x + motion.x, node.y + motion.y)):
                        return True
            path.pop()
            return False
    dfs(s)
    return path

#bfs, this gives the shortest path
def search_maze(maze: List[List[int]], s: Coordinate,
                e: Coordinate) -> List[Coordinate]:
    path = []
    visited = set()
    motions = [Coordinate(0, -1), Coordinate(0, 1), Coordinate(1, 0), Coordinate(-1, 0)]
    node_queue = collections.deque([([s], s)])#storing both path and the starting node
    while node_queue:
        current_path, current_node = node_queue.popleft()
        if (current_node.x, current_node.y) in visited or maze[current_node.x][current_node.y] == BLACK:
            continue
        visited.add((current_node.x, current_node.y))
        if current_node == e:
            path = current_path
            break
        for motion in motions:
            if 0 <= current_node.x + motion.x < len(maze) and 0 <= current_node.y + motion.y < len(maze[0]):#valid motions only
                node_queue.append([current_path + [Coordinate(current_node.x + motion.x, current_node.y + motion.y)], (Coordinate(current_node.x + motion.x, current_node.y + motion.y))])
    return path

# Variant 1:
# https://leetcode.com/problems/flood-fill/ 
# Leetcode 695, https://leetcode.com/problems/max-area-of-island/

def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure('Path doesn\'t lay between start and end points')

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure('Path contains invalid segments')

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('18-01-search_maze.py', 'search_maze.tsv',
                                       search_maze_wrapper))
