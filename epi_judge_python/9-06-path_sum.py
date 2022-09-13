# from binary_tree_node import BinaryTreeNode
from binarytree import Node
BinaryTreeNode = Node #creating synonym
from test_framework import generic_test


"""
traverse the tree, keeping track of difference of the root -to-node path sum and the target value
call this the remaining weight. As soon as we encounter a leaf and the remaining weight is equal to leaf data, we return true.
Short circuit evaluation of the check ensures that we donot processes additional leaves
"""
def has_path_sum(tree: BinaryTreeNode, remaining_weight: int) -> bool:

    if not tree:
        return False
    if not tree.left and not tree.right:  # Leaf. chgeck if the leaf adds up to the sum or not
        return remaining_weight == tree.data
    # Non-leaf.
    #short circuiting is done using OR, it will keep on traversing until first leaf with True encountered
    return (has_path_sum(tree.left, remaining_weight - tree.data)
            or has_path_sum(tree.right, remaining_weight - tree.data))


#variant 1
"""
https://leetcode.com/problems/path-sum/
112. Path Sum
Write a progrm which takes the sam inputs as in above problem and returns all the paths to leaves whose weight equals s.
Type of recursion
"""
def has_path_sum_variant_v1(node: BinaryTreeNode, weight: int):
    paths = []
    path = []
    def has_path_sum(tree: BinaryTreeNode, remaining_weight: int) -> bool:

        if not tree:
            return #dead end
        if not tree.left and not tree.right:  # Leaf. check if the leaf adds up to the sum or not
            if remaining_weight == tree.val:
                path.append(tree.val)
                paths.append(path[:])#add a copy of the path array
                path.pop()
            return
        # Non-leaf.
        path.append(tree.val)
        has_path_sum(tree.left, remaining_weight - tree.val)
        has_path_sum(tree.right, remaining_weight - tree.val)
        path.pop()#pop the current node since backtracking now
        # return False
    has_path_sum(node, weight)
    return paths

def has_path_sum_variant(node: BinaryTreeNode, weight: int):
    paths = []
    def has_path_sum(tree: BinaryTreeNode, remaining_weight: int, path) -> bool:

        if not tree:
            return #dead end
        if not tree.left and not tree.right:  # Leaf. check if the leaf adds up to the sum or not
            if remaining_weight == tree.val:
                paths.append(path + [tree.val])
            return
        # Non-leaf.
        has_path_sum(tree.left, remaining_weight - tree.val, path + [tree.val])
        has_path_sum(tree.right, remaining_weight - tree.val, path + [tree.val])
    has_path_sum(node, weight, [])
    return paths

root = BinaryTreeNode(314)
root.left = BinaryTreeNode(6)
root.right = BinaryTreeNode(2)
root.right.left = BinaryTreeNode(2)
root.right.right = BinaryTreeNode(275)
root.left.left = BinaryTreeNode(271)
root.left.right = BinaryTreeNode(561)
root.left.left.left = BinaryTreeNode(28)
root.left.left.right = BinaryTreeNode(0)
root.left.right.right = BinaryTreeNode(3)
root.left.right.right.left = BinaryTreeNode(17)
root.right.right.right = BinaryTreeNode(28)
root.right.left.right = BinaryTreeNode(1)
root.right.left.right.left = BinaryTreeNode(401)
root.right.left.right.right = BinaryTreeNode(257)
root.right.left.right.left.right = BinaryTreeNode(641)
print(root)
print(has_path_sum_variant(root, 619))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('9-06-path_sum.py', 'path_sum.tsv',
                                       has_path_sum))
