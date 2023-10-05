import collections
from string import ascii_lowercase
from typing import Set

from test_framework import generic_test


"""


Transform one string to another
S is source and t is target vertex. You need to traverse from s to t in shortest fashion hence bfs recommended

Given a dictionary D and two string s, and t, write a program to determine if s produces t.
Assume all characters are lowercase alphabets. If s does prodcue t, output the length of a shortest production sequence
otherwise return -1.
Logic:
    Treat string in D as vertices in undirected graph, with an edge between u and v if and only if the u and v differ
    in one character, also both vertices should be of same length.
    Once edges are created, you just need to search for t vertex, starting from s vertex. Use BFS to do the shortest
    path search.
"""
#very slow, and dictionary being copied
def transform_string_slow(D: Set[str], s: str, t: str) -> int:
    def lexical_compare(w1, w2):
        count = 0
        if w1 != w2 and len(w1) == len(w2):
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    count += 1
        return count == 1
    #now bfs
    node_queue = collections.deque()
    node_queue.append((s, 0))
    D.remove(s)
    while node_queue:
        current_node, distance = node_queue.popleft()
        if current_node == t:
            return distance
        for word in D.copy():
            if lexical_compare(current_node, word): #check if these can be edges
                node_queue.append((word, distance + 1))
                D.remove(word)
    return -1
#another try, need to imporove the neighbour checks
"""
https://pythonexamples.org/python-string-replace-character-at-specific-position/
Python: Replace Character at Specific Index in String
To replace a character with a given character at a specified index, you can use python string slicing as shown below:

string = string[:position] + character + string[position+1:]
Time:
    For BFS, time is O(d + d^2) == O(d^2), number of edges in worst case will be d^2 for d vertices. If average size
    of each vertex is n, then upper bound will be O(nd)
Space: O(d)
"""
def transform_string(D: Set[str], s: str, t: str) -> int:
    node_queue = collections.deque()
    node_queue.append((s, 0))
    D.remove(s) ## Marks s as visited by erasing it in D.
    while node_queue:
        current_node, distance = node_queue.popleft()
        if current_node == t:
            return distance
        #now find neighbours y varying the characters in current node, at ith position
        for i in range(len(current_node)):
            for ch in ascii_lowercase: #iterates through characters in a - z
                word = current_node[:i] + ch + current_node[i + 1:]#
                if word in D:
                    node_queue.append((word, distance + 1))
                    D.remove(word) #mark as visited
    return -1
    
transform_string(set(['bat', 'cot', 'dog', 'dag', 'dot', 'cat']), 'cat', 'dog')

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('18-07-string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))
