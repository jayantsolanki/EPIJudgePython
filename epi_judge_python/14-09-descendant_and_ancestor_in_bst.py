import functools

from bst_node import BstNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook

#Test if three BST nodes are totally ordered; all keys unique
"""
Write a program which takes two nodes in a bst and a third node, the middle, and determines if one of the two nodes is 
a proper ancestor of the middle and the other is proper descendent of the middle. ( proper means given nodes are not 
equal to middle nodes)
Logic:
    Brute force is to check for middle via traversing from given nodes, checking if one is ancestor and other is descendent, 
    if both returns true then overall is true, if false, then swap and check for descendent for first and ancestor for second.
    In above as soon as we confirm ancestor, we start from middle to confirm the descendent. Also doing vice versa, overall 
    three max searches. Since if one fails we will swap and again start.
    In worst case time is O(h), since if we start from wrong node in confirming the ancestor, we will reach to the 
    deepest depth of the tree.

    To prevent above wrong node start search, we interleave searches, we one place in the search interchangeably for 
    both given nodes, looking for the middle node from them. As soon as we get the middle node, we start searching 
    for descendent.
    Time: O(d), d is difference between depth of ancestor and descendent (or distance between ancestor and descendent). 
    If the middle node doesnt have those two nodes as ancestor or descendent, then it will be O(h)

"""
def pair_includes_ancestor_and_descendant_of_m(possible_anc_or_desc_0: BstNode,
                                               possible_anc_or_desc_1: BstNode,
                                               middle: BstNode) -> bool:

    search_0, search_1 = possible_anc_or_desc_0, possible_anc_or_desc_1

    # Perform interleaved searching from possible_anc_or_desc_0 and
    # possible_anc_or_desc_1 for middle.
    while (search_0 is not possible_anc_or_desc_1 and search_0 is not middle
           and search_1 is not possible_anc_or_desc_0
           and search_1 is not middle and (search_0 or search_1)):#break if first node reaches second node or middle node, or 
           #second node reaches first node or middle node,  or both of the nodes reaches end
        if search_0:
            search_0 = (search_0.left
                        if search_0.data > middle.data else search_0.right)
        if search_1:
            search_1 = (search_1.left
                        if search_1.data > middle.data else search_1.right)

    # If both searches were unsuccessful, or we got from
    # possible_anc_or_desc_0 to possible_anc_or_desc_1 without seeing middle,
    # or from possible_anc_or_desc_1 to possible_anc_or_desc_0 without seeing
    # middle, middle cannot lie between possible_anc_or_desc_0 and
    # possible_anc_or_desc_1.
    if ((search_0 is not middle and search_1 is not middle) #return False if both of them not middle, or either of them reached other node
            or search_0 is possible_anc_or_desc_1
            or search_1 is possible_anc_or_desc_0):
        return False
    #same as above
    # if (not (search_0 is middle or search_1 is  middle) #return False if both of them not middle, or either of them reached other node
    #         or search_0 is possible_anc_or_desc_1
    #         or search_1 is possible_anc_or_desc_0):
    #     return False
        

    def search_target(source, target):
        while source and source is not target:
            source = source.left if source.data > target.data else source.right
        return source is target

    # If we get here, we already know one of possible_anc_or_desc_0 or
    # possible_anc_or_desc_1 has a path to middle. Check if middle has a path
    # to possible_anc_or_desc_1 or to possible_anc_or_desc_0.
    return search_target(
        middle, possible_anc_or_desc_1
        if search_0 is middle else possible_anc_or_desc_0)
    # below means if search_1 reached middle, then search for path to possible_anc_or_desc_1 and vice versa
    # return search_target(middle, possible_anc_or_desc_0) or search_target(middle, possible_anc_or_desc_1)


@enable_executor_hook
def pair_includes_ancestor_and_descendant_of_m_wrapper(executor, tree,
                                                       possible_anc_or_desc_0,
                                                       possible_anc_or_desc_1,
                                                       middle_idx):
    candidate0 = must_find_node(tree, possible_anc_or_desc_0)
    candidate1 = must_find_node(tree, possible_anc_or_desc_1)
    middle_node = must_find_node(tree, middle_idx)

    return executor.run(
        functools.partial(pair_includes_ancestor_and_descendant_of_m,
                          candidate0, candidate1, middle_node))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            '14-09-descendant_and_ancestor_in_bst.py',
            'descendant_and_ancestor_in_bst.tsv',
            pair_includes_ancestor_and_descendant_of_m_wrapper))
