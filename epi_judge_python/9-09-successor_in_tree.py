import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook

"""
Write a program to compute inorder successor of node in a binary tree
Time: O(h)
Logic: Understand the concept of inorder traversing,  next node to a current node is always towards its right child tree.
For extreme cases, such as having no right subtree, then you will have to back track on following situation,
1 -  if current node is someone's left child (parent), then that parent is the successor
2 - if the current node is someone's right child then we already have visited the parent, hence, 
then to find next node we keep visiting parent's parent until we encounter a parent when we 
move up from a left child. that parent is the successor
"""
def find_successor_v2(node: BinaryTreeNode) -> Optional[BinaryTreeNode]:

    #this is the first thing you should check, a successor always belongs to right subtree's left most node if it exists
    if node.right:
        # Successor is the leftmost element in node's right subtree.
        node = node.right
        while node.left:#check until the left node has no left child
            node = node.left
        return node
    #not in right, current node in left part of a tree
    #exceptions
    # Find the closest ancestor whose left subtree contains node. Keep going up until
    #  you either encounter node.parent is None or 
    # node.parent.left = node (this is the answer)
    #this loop will break coz of 1 - either node reaches top, or 
    # 2 - node == node.parent.left
    while node.parent and node.parent.right is node:
        node = node.parent

    # A return value of None means node does not have successor, i.e., node is
    # the rightmost node in the tree.
    return node.parent

#for my simple mind
def find_successor(node: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    #think in terms of how an inorder works
    if node.right:#this is the first thing you should, a successor aslways belongs to right subtree
        # Successor is the leftmost element in node's right subtree.
        node = node.right
        while node.left:#check until the left node has no left child
            node = node.left
        return node
    #exceptions, in case no right child was there
    #keep going up until you reach the parent from the left branch child,
    #  that parent is the answer. at worse it will be None
    if node.parent:
        #if parent's left child is node than parent is the successor
        #else keep moving up until you find a parent which has node has its left child
        while node.parent:
            if node.parent.left is node:#keep checking if node is the left child of node.parent
                break
            #its a right child, so go up
            node = node.parent
    # A return value of None means node does not have successor, i.e., node is
    # the rightmost node in the tree.
    return node.parent

def find_successor_naive(node: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    in_process = [(node, False)]#initial node
    successor_flag = False
    defNode = node
    while in_process:#run while stack is not empty
        node, children_added = in_process.pop()
        if node:
            if children_added:#if node just popped is not False then add it to result
                if successor_flag:
                    return node
                if defNode == node:
                    successor_flag = True
            else:
                in_process.append((node.right, False))
                in_process.append((node, True))
                in_process.append((node.left, False))

    #proceeed only if the defNode has no right child
    node = defNode
    if node.parent:
        #if parent's left child is node than parent is the successor
        #else keep moving up until you find a parent which has node has its left child
        while node.parent:
            if node.parent.left is node:
                break
            node = node.parent
            # return node.parent
    return node.parent


@enable_executor_hook
def find_successor_wrapper(executor, tree, node_idx):
    node = must_find_node(tree, node_idx)

    result = executor.run(functools.partial(find_successor, node))

    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('9-09-successor_in_tree.py',
                                       'successor_in_tree.tsv',
                                       find_successor_wrapper))
