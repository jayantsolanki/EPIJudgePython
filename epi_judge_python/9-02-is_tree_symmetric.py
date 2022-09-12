# from binary_tree_node import BinaryTreeNode
import collections
from test_framework import generic_test
from binarytree import Node
BinaryTreeNode = Node #creating synonym

#no need to create mirror tree, just find out that the subtreees are mirror or not
# as soon as one fails exit
#time : O(n), space O(h)
#logic BFS aka level order traversal
def is_symmetric_ori(tree: BinaryTreeNode) -> bool:
    def check_symmetric(subtree_0, subtree_1):
        if not subtree_0 and not subtree_1:
            return True
        elif subtree_0 and subtree_1:
            return (subtree_0.data == subtree_1.data
                    and check_symmetric(subtree_0.left, subtree_1.right)
                    and check_symmetric(subtree_0.right, subtree_1.left))
        # One subtree is empty, and the other is not.
        return False

    return not tree or check_symmetric(tree.left, tree.right)

#we check right child for left with left child or right, and vice versa, and recurse on those
def is_symmetric_simple(tree: BinaryTreeNode) -> bool:
    def check_symmetric(left, right):
        if not left and not right:#if both nodes are null, they are symmetric still
            return True
        elif left and right:
            return (left.data == right.data #shortcircuiting
                    and check_symmetric(left.left, right.right)
                    and check_symmetric(left.right, right.left))
        # One subtree is empty, and the other is not.
        else:#if either of them are None, then not symmetric
            return False

    return not tree or check_symmetric(tree.left, tree.right)
# BFS iterative
"""
Instead of recursion, we can also use iteration with the aid of a queue. Each two consecutive nodes in the queue should
 be equal, and their subtrees a mirror of each other. Each time, two nodes are extracted and their values compared. 
 Then, the right and left children of the two nodes are inserted in the queue in opposite order.
"""
def is_symmetric(tree: BinaryTreeNode) -> bool:
        if not tree:
            return True
        node_deque = collections.deque([tree.left, tree.right])#important, dont insert root
        # node_deque.append(tree.left)
        # node_deque.append(tree.right)
        while node_deque:
            node1 = node_deque.popleft()
            node2 = node_deque.popleft()
            if not node1 and not node2:
                continue
            elif not node1 or not node2:#either of them are None
                return False
            elif node1.data != node2.data:
                return False
            else:
                node_deque.append(node1.left)
                node_deque.append(node2.right)
                node_deque.append(node1.right)
                node_deque.append(node2.left)
        return True
                

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('9-02-is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
