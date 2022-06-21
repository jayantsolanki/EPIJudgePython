# from binary_tree_node import BinaryTreeNode
import collections
from test_framework import generic_test

#lib
class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    # def __eq__(self, other):
    #     return equal_binary_trees(self, other)

    # def __repr__(self):
    #     return str(binary_tree_to_string(self))

    # def __str__(self):
    #     return self.__repr__()


"""
Write a program  that takes as input a binary tree and checks if the tree satisfies the BST property.
BST Property: Each node must have value >= all the values in left subtree and <= all the values in right subtree.
"""

#method 1:
"""
Logic:
    Check BST contraint on each subtree. Initial contraint comes from root.
    Generalisation: If all nodes in the tree must have value in range [l, u].
    If root is w, then is must lies in [l, u] range.  Similar left child of root must have value in range [l, w]
    right child in range [w, l]. Range percolates downward .
Time: O(n), Space: O(h), h is the height of the tree
"""
def is_binary_tree_bst_original(tree: BinaryTreeNode) -> bool:
    def are_keys_in_range(tree,
                          low_range=float('-inf'),
                          high_range=float('inf')):
        if not tree:#reached leaf
            return True
        elif not (low_range <= tree.data <= high_range):
            return False
        return (are_keys_in_range(tree.left, low_range, tree.data)
                and are_keys_in_range(tree.right, tree.data, high_range))

    return are_keys_in_range(tree)

#different way for above
def is_binary_tree_bst_amateur(tree: BinaryTreeNode) -> bool:
    def are_keys_in_range(tree,
                        low_range=float('-inf'),
                        high_range=float('inf')):
        if not tree:
            return True
        elif not (low_range <= tree.data <= high_range):
            return False
        left =  are_keys_in_range(tree.left, low_range, tree.data)
        if not left:
            return False
        right = are_keys_in_range(tree.right, tree.data, high_range)
        if not right:
            return False
        return True
    return are_keys_in_range(tree)

"""
Inorder traversal: this traversal gives sorted array, which is definitely a bst
We keep on checking current element with previous element encountereed during traversal, and exit if current < previous
Time and Space O(n)
"""
#using inorder
def is_binary_tree_bst_inorder(tree):
    def inorder_traversal(tree):
        if not tree:
            return True
        elif not inorder_traversal(tree.left):
            return False
        elif prev[0] and prev[0].data > tree.data:
            return False
        prev[0] = tree
        return inorder_traversal(tree.right)

    prev = [None]
    return inorder_traversal(tree)


#method 2:
"""
Doing check at depth level, BFS
Logic:
    We pop node and check for contraint, and pass down new contraints interval for left and right child in the queue
Time and Space O(n)
"""
#book
def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    QueueEntry = collections.namedtuple('QueueEntry', ('node', 'lower', 'upper'))
    TreeQueue = collections.deque([QueueEntry(tree, float('-Inf'), float('Inf'))])

    while TreeQueue:
        current_node = TreeQueue.popleft()
        if current_node.node:
            if not (current_node.lower <= current_node.node.data <= current_node.upper):
                return False
            TreeQueue.append(QueueEntry(current_node.node.left, current_node.lower, current_node.node.data))
            TreeQueue.append(QueueEntry(current_node.node.right, current_node.node.data, current_node.upper))
    return True

#simple
def is_binary_tree_bst_simple(tree: BinaryTreeNode) -> bool:
    QueueEntry = collections.namedtuple('QueueEntry', ('node', 'lower', 'upper'))
    TreeQueue = collections.deque()
    if tree:
        TreeQueue.append(QueueEntry(tree, float('-Inf'), float('Inf')))

    while TreeQueue:
        current_node = TreeQueue.popleft()
        if not (current_node.lower <= current_node.node.data <= current_node.upper):
            return False
        if current_node.node.left:
            TreeQueue.append(QueueEntry(current_node.node.left, current_node.lower, current_node.node.data))
        if current_node.node.right:
            TreeQueue.append(QueueEntry(current_node.node.right, current_node.node.data, current_node.upper))
    return True
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('14-01-is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
