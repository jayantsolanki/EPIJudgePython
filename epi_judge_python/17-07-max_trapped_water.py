from typing import List

from test_framework import generic_test

"""
Leetcode: 11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/
Write a program which takes as input an integer array and returns the pair of entries that trap the max amount of
water.
Logic:
    Remember: Whether you choose to move the higher or lower side, you're always going to be making the width smaller.
    Therefore we are trying to maximize the height.
    You have two heights H_left and H_right, and H_right < H_left, then we know we have two choices, we want 
    to move one of them. If we move the larger one, we cannot increase the height for the simple reason that 
    we are always limited by the shortest, and we would be decreasing j-i, the width as well.

    To clarify: let's say we kept the shortest forever, what would happen? Well, j-i would decrease, and either 
    we come across a taller block, which doesn't matter because our shorter one we kept only mattered, or we find 
    a shorter one, in which case that one matters.
    Either way we end up with a smaller area, so we must move the shorter one because moving the larger one cannot 
    give an increase in area.
Time: O(n), Space O(1)
"""
def get_max_trapped_water(heights: List[int]) -> int:
    max_vol = 0
    left, right = 0, len(heights) - 1

    while left < right:
        current_vol = (right - left) * min(heights[left], heights[right])
        if current_vol > max_vol:
            max_vol = current_vol
        #now decrement or increment
        if heights[left] > heights[right]: #move the min height towards right or left,hoping that you may find a longer height
            right -= 1
        else:
            left += 1
    return max_vol



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('17-07-max_trapped_water.py',
                                       'max_trapped_water.tsv',
                                       get_max_trapped_water))
