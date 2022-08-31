import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

"""
Leetcode: 785. Is Graph Bipartite?
https://leetcode.com/problems/is-graph-bipartite/

We can check if a graph is Bipartite or not by coloring the graph using two colors. If a given graph is 2-colorable, then it is Bipartite, otherwise not.
https://www.geeksforgeeks.org/bipartite-graph/
A bipartite graph is possible if the graph coloring is possible using two colors such that vertices in a set are colored with the same color. Note that it is possible to color a cycle graph with even cycle using two colors. For example, see the following graph. 
It is not possible to color a cycle graph with odd cycle using two colors. 
Following is a simple algorithm to find out whether a given graph is Bipartite or not using Breadth First Search (BFS). 
1. Assign RED color to the source vertex (putting into set U). 
2. Color all the neighbors with BLUE color (putting into set V). 
3. Color all neighbor’s neighbor with RED color (putting into set U). 
4. This way, assign color to all vertices such that it satisfies all the constraints of m way coloring problem where m = 2. 
5. While assigning colors, if we find a neighbor which is colored with same color as current vertex, then the graph cannot be colored with 2 vertices (or graph is not Bipartite) 
"""

class GraphVertex:
    def __init__(self) -> None:
        self.d = -1
        self.edges: List[GraphVertex] = []


"""
Logic:
    Start adding distance to the vertices encounter with reference to first vertex. And add those vertices to queue.
    If a cross edge is found between two vertices, which are k distance from first vertex, then it is a odd cycle, and graph 
    cannot be colored into two colors.
    That is solved through cycle detection between source and neighbor. If a source node shares the same level order as a 
    neighbor, it means a cycle exists and that cross-edge is within the same group.
Time: O(V + E)
Space: O(V)
"""
def is_any_placement_feasible(graph: List[GraphVertex]) -> bool:

    def bfs(node):
        node_queue = collections.deque()
        node.d = 0 #setting start distance to zero
        node_queue.append(node)
        while node_queue:
            current_node = node_queue.popleft()
            #getting neighbours
            for neighbour in current_node.edges:
                if neighbour.d == -1: #not colored
                    neighbour.d = current_node.d + 1
                    node_queue.append(neighbour)
                elif neighbour.d == current_node.d:#if a cross edge found and its distance is same as current node
                    return False # cycle found with same k distances hence cannot be colored
        return True
    return all( bfs(node) for node in graph if node.d == -1)#now check for both connected and disconnected graphs
    # return all( bfs(graph[i]) for i in range(len(graph)) if graph[i].d == -1)#now check for both connected and disconnected graphs


@enable_executor_hook
def is_any_placement_feasible_wrapper(executor, k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex() for _ in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_any_placement_feasible, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('18-06-is_circuit_wirable.py',
                                       'is_circuit_wirable.tsv',
                                       is_any_placement_feasible_wrapper))
