from typing import List

# from binary_tree_node import BinaryTreeNode
from binarytree import Node
BinaryTreeNode = Node #creating synonym
from test_framework import generic_test


"""
use stack to do it. Get the current node, mark it false until its left and right node has been checked
Then, visit its left node and repeat the same process, until every node has been true. While popping if
you find a node which is already marked true, then insert it into a traversal result array
Note that each node is added two times in the _in_process array, first as a child (false) and later has the root of its children (true)
Logic: O(n), Space O(h)
"""
def inorder_traversal(tree: BinaryTreeNode) -> List[int]:

    result = []

    in_process = [(tree, False)]#initial node
    while in_process:#run while stack is not empty
        node, left_subtree_traversed = in_process.pop()
        if node:
            if left_subtree_traversed:#if node just popped is not False then add it to result
                result.append(node.data)
            else:
                in_process.append((node.right, False))#in process
                in_process.append((node, True))#fully processed
                in_process.append((node.left, False))#in process
    return result


#variant 1
"""
write a non recursive function which takes as input a binary tree and performs preorder traversal of the tree
"""
def preorder_traversal(tree: BinaryTreeNode) -> List[int]:

    if not tree:
        return []
    result = []
    stackList = [(tree, False)]     
    
    while stackList:
        current_node, status = stackList.pop()
        
        if current_node:#making sure it is not None
            if status:
                result.append(current_node.val)
            else:#get its left and right nodes
                # stackList.extend([(current_node.right, False), (current_node, True), (current_node, False)])
                stackList.append((current_node.right, False))
                stackList.append((current_node.left, False))
                stackList.append((current_node, True))
    return result

#variant 2
"""
write a non recursive function which takes as input a binary tree and performs postorder traversal of the tree
"""
def postorder_traversal(tree: BinaryTreeNode) -> List[int]:
    if not tree:
        return []
    result = []
    stackList = [(tree, False)]     
    
    while stackList:
        current_node, status = stackList.pop()
        
        if current_node:#making sure it is not None
            if status:
                result.append(current_node.val)
            else:#get its left and right nodes
                # stackList.extend([(current_node.right, False), (current_node, True), (current_node, False)])
                stackList.append((current_node, True))
                stackList.append((current_node.right, False))
                stackList.append((current_node.left, False))
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('9-07-tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))
