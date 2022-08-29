import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

"""
Leetcode: 261. Graph Valid Tree, this is a bit different because we have to take only one root here
https://leetcode.com/problems/graph-valid-tree/solution/
Leetcode: 207. Course Schedule
https://leetcode.com/problems/course-schedule/

Write a program that takes as input a directed graph and checks if the graph contains a cycle.
Logic:
    We have to mark three stages of node, unvisited, being visited and visited
    A node which was being visited and agian encountered in the stack loop, it means it is a cycle
Time: O(V + E), we iterate over all vertices and spend a constant amount of time per edge.
Space: O(V), this is max stack depth, if we go deeper that V calls, this means some vertex myuust repeat., 
hence early termination 
"""
class GraphVertex:
    color = {
        0: 'Not Visited',
        1: 'Visiting',
        2: 'Visited'
    }
    def __init__(self) -> None:
        self.color = 0
        self.edges: List['GraphVertex'] = []


def is_deadlocked(graph: List[GraphVertex]) -> bool:
    def dfs(node):
        if node.color == 1:
            return True #cycle found
        else: #mark it being visited
            node.color = 1
            #get neighbours
            for neighbour in node.edges:
                if neighbour.color != 2:#only visit non visited cells
                    if dfs(neighbour):
                        return True
            node.color = 2 #finally all its nodes visited
        return False
    #check for all the nodes
    for node in graph:
        if node.color != 2: #important# we avoid cross edges too
            if dfs(node):
                return True
    return False




@enable_executor_hook
def is_deadlocked_wrapper(executor, num_nodes, edges):
    if num_nodes <= 0:
        raise RuntimeError('Invalid num_nodes value')
    graph = [GraphVertex() for _ in range(num_nodes)]

    for (fr, to) in edges:
        if fr < 0 or fr >= num_nodes or to < 0 or to >= num_nodes:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_deadlocked, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('18-04-deadlock_detection.py',
                                       'deadlock_detection.tsv',
                                       is_deadlocked_wrapper))
