import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure

"""
Leetcode: 133 https://leetcode.com/problems/clone-graph/
Design an algo that takes a reference to a vertex u, and creates a copy (deep copy) of the graph on the vertices reachable
from u. Return the copy of u
Logic:
    Use BFS, add each new vertex to queue, and in the BFS edge search, add those edges.
    Maintain a hashmap to keep progress on added vertices, and access them for adding edges to them
Time and Space: O(V) for both hash map and BFS queue
"""

class GraphVertex:
    def __init__(self, label: int) -> None:
        self.label = label
        self.edges: List['GraphVertex'] = []

#my take
def clone_graph(graph: GraphVertex) -> GraphVertex:
    node_queue = collections.deque()
    node_queue.append(graph)
    vertex_track = {
        graph.label: GraphVertex(graph.label)
    }#vertex_track also acts as a seen variable used in norma ldfs and bfs
    while node_queue:
        current_node = node_queue.popleft()
        new_vertex = vertex_track[current_node.label]#get the new vertex by its label from the hashmap
        for edge in current_node.edges:
            if edge.label not in vertex_track:#only create that node if not created before
                vertex_track[edge.label] = GraphVertex(edge.label) #create new node
                node_queue.append(edge)#at this edge in to queue for later processing
            new_vertex.edges.append(vertex_track[edge.label])#add this cloned vertex to new_vertex

    return vertex_track[graph.label]

#DFS - iterative
def clone_graph_iter(graph: GraphVertex) -> GraphVertex:
    if graph is None:
        return graph
    node_stack = []
    node_stack.append(graph)
    vertex_track = {
        graph.label: GraphVertex(graph.label)
    }#vertex_track also acts as a seen variable used in norma ldfs and bfs
    while node_stack:
        current_node = node_stack.pop()
        new_vertex = vertex_track[current_node.label]#get the new vertex by its val from the hashmap
        for edge in current_node.edges:
            if edge.label not in vertex_track:
                vertex_track[edge.label] = GraphVertex(edge.label) #create new node
                node_stack.append(edge)#at this edge in to queue for later processing
            new_vertex.edges.append(vertex_track[edge.label])#add this cloned vertex to new_vertex

    return vertex_track[graph.label]

#DFS recursive
def clone_graph_rec1(graph: GraphVertex) -> GraphVertex:
    if graph is None:
        return graph
    vertex_track = {
        graph.label: GraphVertex(graph.label)
    }#vertex_track also acts as a seen variable used in norma ldfs and bfs
    def dfs(current_node):
        new_vertex = vertex_track[current_node.label]#get the new vertex by its val from the hashmap
        for edge in current_node.edges:
            if edge.label not in vertex_track:
                vertex_track[edge.label] = GraphVertex(edge.label) #create new node
                dfs(edge)#at this edge in to stack for later processing
            new_vertex.edges.append(vertex_track[edge.label])#add this cloned vertex to new_vertex
    dfs(graph)
    return vertex_track[graph.label]
#DFS recursive
def clone_graph_rec2(graph: GraphVertex) -> GraphVertex:
    if graph is None:
        return graph
    vertex_track = {}
    def dfs(current_node):
        if current_node.label in vertex_track:
            return #vertex_track[current_node.label]
        
        vertex_track[current_node.label] = GraphVertex(current_node.label) #create new node
        
        new_vertex = vertex_track[current_node.label]#get the new vertex by its val from the hashmap
        for edge in current_node.edges:
            dfs(edge)#add this edge into dfs stack for later processing
            new_vertex.edges.append(vertex_track[edge.label])#add this cloned vertex to new_vertex
    dfs(graph)
    return vertex_track[graph.label]


#original
def clone_graph_ori(graph: GraphVertex) -> GraphVertex:

    if graph is None:
        return None

    q = collections.deque([graph])
    vertex_map = {graph: GraphVertex(graph.label)}
    while q:
        v = q.popleft()
        for e in v.edges:
            # Try to copy vertex e.
            if e not in vertex_map:
                vertex_map[e] = GraphVertex(e.label)
                q.append(e)
            # Copy edge.
            vertex_map[v].edges.append(vertex_map[e])
    return vertex_map[graph]




def copy_labels(edges):
    return [e.label for e in edges]


def check_graph(node, graph):
    if node is None:
        raise TestFailure('Graph was not copied')

    vertex_set = set()
    q = collections.deque()
    q.append(node)
    vertex_set.add(node)
    while q:
        vertex = q.popleft()
        if vertex.label >= len(graph):
            raise TestFailure('Invalid vertex label')
        label1 = copy_labels(vertex.edges)
        label2 = copy_labels(graph[vertex.label].edges)
        if sorted(label1) != sorted(label2):
            raise TestFailure('Edges mismatch')
        for e in vertex.edges:
            if e not in vertex_set:
                vertex_set.add(e)
                q.append(e)


def clone_graph_test(k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex(i) for i in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    result = clone_graph(graph[0])
    check_graph(result, graph)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('18-05-graph_clone.py', 'graph_clone.tsv',
                                       clone_graph_test))
