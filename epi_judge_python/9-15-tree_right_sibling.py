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
Time: O(n), space O(1)
We need to ensure that we process nodes level-by-level, left to right traversing. . Traversing a level in which
the level_next field is set is trivial. When we complete that level, next level is starting node's left child.
Remember: level traversing can be done only using loops
"""
def construct_right_sibling(tree: BinaryTreeNode) -> None:
    def populate_children_next_field(start_node):
        while start_node and start_node.left:# we need to assume that it is perfect binary tree, hence startting from left
            # Populate left child's next field.
            start_node.left.next = start_node.right
            # Populate right child's next field if start_node is not the last
            # node of level.
            start_node.right.next = start_node.next and start_node.next.left#fist condition makes sure that next exist for start node
            #before accessing next property, else error will be thrown when exising left, for example root node doesnt 
            # has next property node
            start_node = start_node.next#now move to the next node in the same level using the next property of that node

    while tree and tree.left:
        populate_children_next_field(tree)
        tree = tree.left

#brute force, this can also work on non perfect tree too
# Use this for Variant 2 also. I dont care about space
# time: O(n), space O(n)
from collections import deque
def construct_right_sibling_brute(tree):
    if not tree:
        return None
    node_deque = deque([(tree, 0)])
    # last = None
    #you can do by level ordering
    while node_deque:
        # result.append([])
        last = None
        queu_len = len(node_deque)
        for i in range(queu_len):
            node, depth = node_deque.popleft()
            # if len(result[depth]):#do the linking here
            #     result[depth][-1].next = node
            if last:
                last.next = node
            last = node
            # result[depth].append(node)
            if node.left:
                node_deque.append((node.left, depth+1))
            if node.right:
                node_deque.append((node.right, depth+1))
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
