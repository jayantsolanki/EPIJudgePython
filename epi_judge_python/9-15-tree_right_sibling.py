import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class BinaryTreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.next = None  # Populates this field.

# Assumption perfect binary tree needed
"""
Write a program that takes a perfect binary tree, and sets each node's level-next field to 
the node on its right, if one exists.
Leetcode 116 https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
Time: O(n), space O(1)
We need to ensure that we process nodes level-by-level, left to right traversing. . Traversing a level in which
the level_next field is set is trivial. When we complete that level, next level is starting node's left child.
Remember: level traversing can be done only using loops
"""
def construct_right_siblingd(tree: BinaryTreeNode) -> None:
    def populate_children_next_field(start_node):
        #second condition is redundant
        #iterate using next attribute
        # we need to assume that it is perfect binary tree, hence starting from left
        while start_node and start_node.left:
            # Populate left child's next field.
            start_node.left.next = start_node.right
            # Populate right child's next field if start_node is not the last
            # node of level.
            if start_node.next:
                start_node.right.next = start_node.next.left
            # start_node.right.next = start_node.next and start_node.next.left
            # #first condition makes sure that next exist for start node
            #before accessing next property, else error will be thrown when exising left, for example root node doesnt 
            # has next property node
            start_node = start_node.next#now move to the next node in the same level using the next property of that node
    #we do it level by level, current level does the next  linking for below level. Hence we go down until one level
    while tree and tree.left:
        #above the leaf
        populate_children_next_field(tree)
        tree = tree.left

#brute force, this can also work on non perfect tree too
# Use this for Variant 2 also. I dont care about space
# time: O(n), space O(n)
from collections import deque
#using BFS
def construct_right_sibling(tree):
    if not tree:
        return None
    node_deque = deque([tree])
    # prev = None
    #you can do by level ordering
    while node_deque:#done using single queue
        # result.append([])
        prev = None
        queu_len = len(node_deque)
        for i in range(queu_len):
            node = node_deque.popleft()
            # if len(result[depth]):#do the linking here
            #     result[depth][-1].next = node
            if prev:
                prev.next = node
            prev = node
            # result[depth].append(node)
            if node.left:
                node_deque.append(node.left)
            if node.right:
                node_deque.append(node.right)
    #now linking the items
    # for items in result:
    #     for i in range(0, len(items) - 1):
    #         items[i].next = items[i + 1]

    


def traverse_next(node):
    while node:
        yield node
        node = node.next
    return


def traverse_left(node):
    while node:
        yield node
        node = node.left
    return


def clone_tree(original):
    if not original:
        return None
    cloned = BinaryTreeNode(original.data)
    cloned.left, cloned.right = clone_tree(original.left), clone_tree(
        original.right)
    return cloned


@enable_executor_hook
def construct_right_sibling_wrapper(executor, tree):
    cloned = clone_tree(tree)

    executor.run(functools.partial(construct_right_sibling, cloned))

    return [[n.data for n in traverse_next(level)]
            for level in traverse_left(cloned)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('9-15-tree_right_sibling.py',
                                       'tree_right_sibling.tsv',
                                       construct_right_sibling_wrapper))
