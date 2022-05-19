from dataclasses import dataclass
from turtle import left
from typing import List
from functools import reduce
from collections import deque

# from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


class BinaryTreeNode:
    def __init__(self, data = None, left = None, right = None) -> None:
        self.data = data
        self.left = left
        self.right = right

#basically get children nodes at every iteration using left and right pointers, push them to
# a list (kinda queue), now process that list and get the data (this is specific level), once done, process the queue to
#get children again (left, right), keep repeating until children are no more
def binary_tree_depth_order_original(tree: BinaryTreeNode) -> List[List[int]]:

    result: List[List[int]] = []
    if not tree:
        return result

    curr_depth_nodes = [tree]
    while curr_depth_nodes:
        result.append([curr.data for curr in curr_depth_nodes])#get the value of current nodes
        curr_depth_nodes = [#this line gets the children of current node
            child for curr in curr_depth_nodes
            for child in (curr.left, curr.right) if child
        ]
    return result

#simple version
def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:

    result = []
    if not tree:
        return result

    curr_depth_nodes = [tree] #get root
    while curr_depth_nodes:
        result.append([curr.data for curr in curr_depth_nodes])#get the value of nodes at current level
        #enclosing above in an separate list, since each separate list defines the level (depth)
        #now fetch the nodes at next level
        children = []
        for curr in curr_depth_nodes:
            children = children + [child for child in (curr.left, curr.right) if child]
        curr_depth_nodes = children
    return result

#variant 1
#alternate left-right or right-left order
def binary_tree_depth_order_alt(tree: BinaryTreeNode) -> List[List[int]]:

    result = []
    if not tree:
        return result

    curr_depth_nodes = [tree] #get root
    switch = 1
    while curr_depth_nodes:
        result.append([curr.data for curr in curr_depth_nodes])#get the value of nodes at current level
        #enclosing above in an sepearate list, since each separate list defines the level (depth)
        #now fetch the nodes at next level
        children = []
        if switch:
            for curr in curr_depth_nodes:
                children = children + [child for child in (curr.left, curr.right) if child]
        else:
            for curr in curr_depth_nodes:
                children = children + [child for child in (curr.right, curr.left) if child]          
        curr_depth_nodes = children
        switch ^= 1
    return result

#variant 2
#write a program which takes as input a binary tree and returns the keys in a bottom up, left-to-right order
#just reverse the first program result array or use deque
#using deque
def binary_tree_depth_order_bottomup(tree: BinaryTreeNode) -> List[List[int]]:

    result = deque()
    if not tree:
        return result

    curr_depth_nodes = [tree]
    while curr_depth_nodes:
        result.append([curr.data for curr in curr_depth_nodes])#get the value of current nodes
        result.appendleft([curr.data for curr in curr_depth_nodes])#get the value of current nodes
        curr_depth_nodes = [#this line gets the children of current node
            child for curr in curr_depth_nodes
            for child in (curr.left, curr.right) if child
        ]
    return result #or use list(result)
#variant3
# write a program to calcuate of nodes at each depth
def binary_tree_depth_order_avg(tree: BinaryTreeNode) -> List[List[int]]:

    result: List[List[int]] = []
    if not tree:
        return result

    curr_depth_nodes = [tree]
    while curr_depth_nodes:
        temp = [curr.data for curr in curr_depth_nodes]
        result.append(reduce(lambda x, y: x + y, temp)/float(len(temp)))
        curr_depth_nodes = [#this line gets the children of current node
            child for curr in curr_depth_nodes
            for child in (curr.left, curr.right) if child
        ]
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('8-06-tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
