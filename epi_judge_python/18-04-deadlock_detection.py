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
        0: 'Not Visited',#white
        1: 'Visiting',#gray
        2: 'Visited'#black
    }
    def __init__(self) -> None:
        self.color = 0
        self.edges: List['GraphVertex'] = []


def is_deadlocked_dfs(graph: List[GraphVertex]) -> bool:
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
        if node.color != 2: #important# we avoid cross edges too, doesnt matter actually
            if dfs(node):
                return True
    return False
#another form, 03OCT2023
def is_deadlocked(graph: List[GraphVertex]) -> bool:
    def dfs(node):
        if node.color == 1:#gray
            return True #cycle found
        if node.color == 2:
            return False #already visited, forward/cross edge
        else: #mark it being visited
            node.color = 1
            #get neighbours
            for neighbour in node.edges:
                if dfs(neighbour):
                    return True
            node.color = 2 #finally all its nodes visited
        return False
    #check for all the nodes
    for node in graph:
        if dfs(node):
            return True
    return False


#variant 1: Leetcode 261 https://leetcode.com/problems/graph-valid-tree/solution/
class Solution:

    # Approach 3: Advanced Graph Theory + Union Find
    #using disjoint set, make sure you get only one root node then return true
    #also there must be no double edge, to check for double edge, find the roots for each edge,
    #if there are same root, than its a double edge
    #time O(NxαN), α(N) is the Inverse Ackermann Function.,  inverse function, f−1, grows very slowly.
    def validTree_unionFind(self, n: int, edges: List[List[int]]) -> bool:
        nodes = [i for i in range(n)]
        rank = [1 for i in range(n)]
        self.count = n
        self.double_edge = False
        print(nodes)
        #disjoint set implementation
        def find(x):
            if x == nodes[x]:
                return x
            else:
                nodes[x] = find(nodes[x])
                return nodes[x]
        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            if rootx != rooty:
                if rank[rootx] > rank[rooty]:
                    nodes[rooty] = rootx
                elif rank[rootx] < rank[rooty]:
                    nodes[rootx] = rooty
                else:
                    nodes[rooty] = rootx
                    rank[rootx] += 1
                self.count -= 1
            else:#if there is already a common root then return False
                # print('double edge')
                # self.double_edge =  True
                return False
            return True

        
        for i, j in edges:
                if not union(i, j):
                    return False
        print(nodes, rank, self.count)
        # return sum([1 for i in range(n) if i == cities[i]])
        return  self.count == 1
    
    """
    # For the graph to be a valid tree, it must have exactly n - 1 edges.
    # Any less, and it can't possibly be fully connected. Any more, and it has to contain cycles.
    Note: Recall that the most complicated part of Approach 1 was in checking whether or not the graph 
    contained cycles. This was because in an undirected graph, we needed to be careful of trivial cycles. 
    Checking whether or not a graph is fully connected is straightforward—we simply checked if all nodes were
    reachable from a search starting at a single node.

    """
    def validTree_dfs_iter(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1: return False

        # Create an adjacency list.
        adj_list = [[] for _ in range(n)]
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)

        # We still need a seen set to prevent our code from infinite
        # looping if there *is* cycles (and on the trivial cycles!)
        seen = {0}
        stack = [0]

        while stack:
            node = stack.pop()
            for neighbour in adj_list[node]:
                if neighbour in seen:
                    continue
                seen.add(neighbour)
                stack.append(neighbour)

        return len(seen) == n
    def validTree_dfs_rec(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1: return False

        # Create an adjacency list.
        adj_list = [[] for _ in range(n)]
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)

        # We still need a seen set to prevent our code from infinite
        # looping if there *is* cycles (and on the trivial cycles!)
        seen = set()

        def dfs(node):
            if node in seen: return
            seen.add(node)
            for neighbour in adj_list[node]:
                dfs(neighbour)

        dfs(0)
        return len(seen) == n
    
    #practice
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodes = [i for i in range(n)]
        rank = [1] * n
        self.count = n
        def find(x):
            if nodes[x] ==  x:
                return x
            else:
                nodes[x] = find(nodes[x])
                return nodes[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    nodes[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    nodes[rootX] = rootY
                else:
                    nodes[rootY] = rootX
                    rank[rootX] += 1
                self.count -= 1
            else:#already has a common root, double edge found
                return False
            return True
    
        for i, j in edges:
            if not union(i, j):
                return False
        return self.count == 1
            
                
                    
        


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
