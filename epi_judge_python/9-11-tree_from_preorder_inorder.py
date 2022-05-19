from typing import List
import importlib  
# from binary_tree_node import BinaryTreeNode
bt= importlib.import_module("9-00-tree_traversal")
BinaryTreeNode = bt.BinaryTreeNode
from test_framework import generic_test

"""
Given inorder and preorder traversal of a binary tree having unique nodes, write a program to
reconstruct the tree.
Logic:
    The two key observations are:

    Preorder traversal follows Root -> Left -> Right, therefore, given the preorder array preorder, we have easy access to the root which is preorder[0].

    Inorder traversal follows Left -> Root -> Right, therefore if we know the position of Root, we can recursively split the entire array into two subtrees.

    We will design a recursion function: it will set the first element of preorder as the root, and then construct the entire tree. To find the left and right subtrees, it will look for the root in inorder, so that everything on the left should be the left subtree, and everything on the right should be the right subtree. Both subtrees can be constructed by making another recursion call.

    It is worth noting that, while we recursively construct the subtrees, we should choose the next element in preorder to initialize as the new roots. This is because the current one has already been initialized to a parent node for the subtrees

    Build a hashmap to record the relation of value -> index for inorder, so that we can find the position of root in constant time.
    Initialize an integer variable preorderIndex to keep track of the element that will be used to construct the root.
    Implement the recursion function arrayToTree which takes a range of inorder and returns the constructed binary tree:
    if the range is empty, return null;
    initialize the root with preorder[preorderIndex] and then increment preorderIndex;
    recursively use the left and right portions of inorder to construct the left and right subtrees.

    Time: O(n), space O(n+h), size of hash table and max depth of tree
"""

def binary_tree_from_preorder_inorder_v2(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:

    node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}

    # Builds the subtree with preorder[preorder_start:preorder_end] and
    # inorder[inorder_start:inorder_end].
    def binary_tree_from_preorder_inorder_helper(preorder_start, preorder_end,
                                                 inorder_start, inorder_end):
        if preorder_end <= preorder_start or inorder_end <= inorder_start:
            return None

        root_inorder_idx = node_to_inorder_idx[preorder[preorder_start]]
        left_subtree_size = root_inorder_idx - inorder_start
        return BinaryTreeNode(
            preorder[preorder_start],
            # Recursively builds the left subtree.
            binary_tree_from_preorder_inorder_helper(
                preorder_start + 1, preorder_start + 1 + left_subtree_size,
                inorder_start, root_inorder_idx),
            # Recursively builds the right subtree.
            binary_tree_from_preorder_inorder_helper(
                preorder_start + 1 + left_subtree_size, preorder_end,
                root_inorder_idx + 1, inorder_end))

    return binary_tree_from_preorder_inorder_helper(preorder_start=0,
                                                    preorder_end=len(preorder),
                                                    inorder_start=0,
                                                    inorder_end=len(inorder))

# much easier to understand                                                    
# from leetcode; https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/
# Time: O(n), space O(n+h), size of hash table and max depth of tree
def binary_tree_from_preorder_inorder(preorder: List[int], inorder: List[int]) -> BinaryTreeNode:
    preorder_index = 0
    # build a hashmap to store value -> its index relations
    # inorder_index_map = {}
    inorder_index_map = {data: i for i, data in enumerate(inorder)}
    # for index, value in enumerate(inorder):
    #     inorder_index_map[value] = index

    def array_to_tree(left, right):
        nonlocal preorder_index # see this, very important, it works in exactly the same way as the global statement, except that it is used to refer to variables that are neither global nor local to the function.
        # if there are no elements to construct the tree
        if left > right: return None

        # select the preorder_index element as the root and increment it
        root_value = preorder[preorder_index]
        root = BinaryTreeNode(root_value)#creating the node


        preorder_index += 1

        # build left and right subtree
        # excluding inorder_index_map[root_value] element because it's the root
        root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
        root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

        return root



    return array_to_tree(0, len(preorder) - 1)

# Variant 1, solve the problem using inorder and a postorder
"""
For example, for preorder traversal the first value is a root, then its left child, then its right child, etc. For postorder traversal the last value is a root, then its right child, then its left child
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/solution/
"""

def binary_tree_from_postorder_inorder(self, inorder: List[int], postorder: List[int]) -> BinaryTreeNode:
    def helper(in_left, in_right):
        # if there is no elements to construct subtrees
        if in_left > in_right:
            return None
        
        # pick up the last element as a root
        val = postorder.pop()
        root = BinaryTreeNode(val)

        # root splits inorder list
        # into left and right subtrees
        index = idx_map[val]

        # build right subtree#since in postorder, when moving backward, right node is encountered first just 
        # after root
        root.right = helper(index + 1, in_right)
        # build left subtree
        root.left = helper(in_left, index - 1)
        return root
    
    # build a hashmap value -> its index
    idx_map = {val:idx for idx, val in enumerate(inorder)} 
    return helper(0, len(inorder) - 1)

#variant 2
"""
https://en.wikipedia.org/wiki/Cartesian_tree
https://leetcode.com/problems/maximum-binary-tree/
A is list of n distinct numbers. Let the index of max value in A be m. Define the max-tree on A recursively to be the binary tree on the entries of A in which the root contains the maximum element of A, the left child is the max-tree on A[0,m-1] and the right child is the max-tree on A[m+1,n-1]. return empty tree if A is len 0. 
Time O(n)
https://stackoverflow.com/questions/27425711/create-max-tree-in-order-n
A couple of observations:

The provided array is the inorder traversal of the tree in question.
The tree has the max heap property, i.e. a node cannot have an ancestor with a lesser value than itself.

"""
from binarytree import Node
BinaryTreeNode = Node #creating synonym
# O(n^2) time
def constructMaximumBinaryTree(nums):
    if len(nums) == 0:
        return None
    
    new_val=max(nums)
    split_index=nums.index(new_val)
    node=BinaryTreeNode(new_val)

    node.left=constructMaximumBinaryTree(nums[:split_index])
    node.right=constructMaximumBinaryTree(nums[split_index+1:])

    return node

print(constructMaximumBinaryTree([3,2,1,6,0,5]))
print(constructMaximumBinaryTree([3,2,0, 1 ,6,5]))

# O(n) time
# https://leetcode.com/problems/maximum-binary-tree/discuss/258364/Python-O(n)-solution-with-explanation.
# Uses stack
"""
    For each new num, we make it into a TreeNode first.
    Then:

    If stack is empty, we push the node into stack and continue
    If new value is smaller than the node value on top of the stack, we append TreeNode as the right node of top of stack.
    If new value is larger, we keep poping from the stack until the stack is empty OR top of stack node value is greater than the new value. During the pop, we keep track of the last node being poped.
    After step 2, we either in the situation of 0, or 1, either way, we append last node as left node of the new node.
    After traversing, the bottom of stack is the root node because the bottom is always the largest value we have seen so far (during the traversing of list).
"""
"""
Anology is like this, since index to the left of max belongs to left and index to the right belongs to right, so as we move
in the given array list, we keep looking for the max, but working backwards, as in first local max , than next greater max, then next so on until we find the largest max. The reason i said working bacwards because, in the orginal question we need to find first largest max then second largest max then third so on. Based on the original question, elements to the left of local max goes left child and right goes right child. Stack mackes sure we can keep popping the last element to find the max encountered so far. 
Below is bottom up approach. The O(n2) one is top down appraoch
"""
def constructMaximumBinaryTree(nums): # it is similar to max Stack API
    stk = [BinaryTreeNode(nums[0])]
    for num in nums[1:]:
        node = BinaryTreeNode(num)
        if num<stk[-1].val:
            stk[-1].right = node
        else:
            while stk and stk[-1].val < num:#pop out every element less than current node and move it to left of node
                #because they would have been at left, since they were found before the current node in the list nums
                node.left = stk.pop()
            if stk:#if existing max greater than current node
                stk[-1].right = node
        stk.append(node)
    return stk[0]
print(constructMaximumBinaryTree([3,2,1,6,0,5]))
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('9-11-tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
