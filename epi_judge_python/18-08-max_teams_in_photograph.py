import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

"""
Topological Sort, assuming no cycle in these questions
Team Photo Day - 2
How would you generalize this problem for multiple team rows:
    Design an algo that takes as input two teams and the heights of the players in the teams and checks if it is possible
    to place players to take the photo subject to the placement contraint.
Return the length of longest(max) such sequence of Teams formed.
Logic:
    You have been given  a Graph with vertices depicting each team. You are also provided with list of DAG edges
    for each vertices  X, Y, such that Team X can be placed before Team Y in the rows.
    We simply run the topological sort on this.
    In first attempt we use DFS
    In the second attempt we use Kahn's Algo for Topoligical Sort
Time: O(V + E)
"""

class GraphVertex:
    def __init__(self) -> None:
        self.edges: List[GraphVertex] = []
        # Set max_distance = 0 to indicate unvisitied vertex.
        self.max_distance = 0

#logic: we keep on following the path and return the max depth, if a cycle is found, we return node.max_distance
def find_largest_number_teams(graph: List[GraphVertex]) -> int:
    def dfs(node):
        if node.max_distance != 0:#cycle found, return the value of the node which got encountered after cycle formation
            # print(node.max_distance, "I ran")
            return node.max_distance
            # return -1 #this works on cycle
        else:
            node.max_distance = 1#important, default value
            for neighbour in node.edges:
                node.max_distance = max(node.max_distance , dfs(neighbour) + 1)
            return node.max_distance
    return max(dfs(node) for node in graph if node.max_distance == 0) 

#this code fails at cycle
def find_largest_number_teams_ori(graph: List[GraphVertex]) -> int:
    def dfs(curr):
        curr.max_distance = max(
            ((vertex.max_distance if vertex.max_distance != 0 else dfs(vertex))
             + 1 for vertex in curr.edges),
            default=1)
        return curr.max_distance
    return max(dfs(g) for g in graph if g.max_distance == 0)


# k = 6
# # edges = [[0, 2], [1, 2]]
# edges = [[0, 1], [1, 2], [1, 3], [3, 4], [4, 5], [5, 0]]
# graph = [GraphVertex() for _ in range(k)]

# for (fr, to) in edges:
#     if fr < 0 or fr >= k or to < 0 or to >= k:
#         raise RuntimeError('Invalid vertex index')
#     graph[fr].edges.append(graph[to])
# # find_largest_number_teams_ori(graph)
# find_largest_number_teams(graph)


@enable_executor_hook
def find_largest_number_teams_wrapper(executor, k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex() for _ in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(find_largest_number_teams, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('18-08-max_teams_in_photograph.py',
                                       'max_teams_in_photograph.tsv',
                                       find_largest_number_teams_wrapper))
