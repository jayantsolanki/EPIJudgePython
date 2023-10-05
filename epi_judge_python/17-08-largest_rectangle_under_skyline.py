from typing import List

from test_framework import generic_test

"""
https://leetcode.com/problems/largest-rectangle-in-histogram/
Compute the largest rectangle under the skyline.
Let A be an array representing the heights of adjacent buildings of unit width. Design an algo to compute
the area of the largest rectangle contained in this skyline.
"""

#mthod 1 Divide and Conquer, causing TLE in last two, since the array is sorted those last two 
"""
This approach relies on the observation that the rectangle with maximum area will be the maximum of:
    a. The widest possible rectangle with height equal to the height of the shortest bar.
    b. The largest rectangle confined to the left of the shortest bar(subproblem).
    c. The largest rectangle confined to the right of the shortest bar(subproblem).
Average case O(nlogn), worst if sorted O(n^2)
"""
def calculate_largest_rectangle_div_and_con(heights: List[int]) -> int:
    i, j = 0, len(heights) - 1
    def calc_area(left, right):
        # print(left, right)
        if left > right:
            return 0
        else:
            shortest_bar = heights[left]
            shortest_bar_index = left
            for index in range(left, right + 1):#this is problematic, since it will change the index because it is using slice
                if shortest_bar > heights[index]:
                    shortest_bar_index = index
                    shortest_bar = heights[index]
            width = right - left + 1
            area = shortest_bar * width
            # return
            return max(area, calc_area(left, shortest_bar_index - 1), calc_area(shortest_bar_index + 1, right))
    return calc_area(i, j)

# calculate_largest_rectangle([1, 4, 2, 5, 6, 3, 2, 6, 6, 5, 2, 1, 3])

"""
Using pointers
Logic:
    We create a list of pillars which can support a rectangle. Idea here is to use a stack.
    We iterate from first index to last. Suppose we are at A[i], any rectangles which have greater height that A[i], cannot be supported by A[i]'s height.
    That is A[i] block any further addition of pillar to a previous high rectangle. So, before appending index i, into stack, we start popping up the indices
    whose heights >= A[i], since we are now constructing piller for a different height rectangle, whose height == A[i]'s height.
    Generalizing, we advance through indices, and add those without popping any previous items from stack, provided that they can be supporting 
    pillars of the exisitng rectangle. And pop those items whose height >= current index to be added. Whenever a building is removed from the active pillar
    set, we know  exactly how far to the right the largest rectangle that is supports goes to. When we remove a blocked building from the active pillar set, to
    find how far to the left its largest supported rectangle extends, we simple look for the closest active pillar that has a lower height.
    Note, while, popping those bigger buildings, keep track of the width and height and calculate the area of buildings being popped out.
    Here you will find the max.
Time O(n), Space O(n), exactly n push and n pops
"""
def calculate_largest_rectangle(heights: List[int]) -> int:

    pillar_indices: List[int] = []
    max_rectangle_area = 0
    # By appending [0] to heights, we can uniformly handle the computation for
    # rectangle area here.
    for i, h in enumerate(heights + [0]):#important, last value is zero, this will force stack to be emptied
        while pillar_indices and heights[pillar_indices[-1]] >= h:
            height = heights[pillar_indices.pop()]
            width = i if not pillar_indices else i - pillar_indices[-1] - 1 # - 1 because we are counting from the index ahead of the one which has been popped
            max_rectangle_area = max(max_rectangle_area, height * width)
        pillar_indices.append(i)#we are appending index only
    return max_rectangle_area

#variant 1
"""
Find the largest square under the skyline.
Logic:
    For sqaure we only consider width which is >= height, and then for calculating area, we just use height ** 2
"""
def calculate_largest_square(heights: List[int]) -> int:

    pillar_indices: List[int] = []
    max_rectangle_area = 0
    # By appending [0] to heights, we can uniformly handle the computation for
    # rectangle area here.
    for i, h in enumerate(heights + [0]):#important, last value is zero, this will force stack to be emptied
        while pillar_indices and heights[pillar_indices[-1]] >= h:
            height = heights[pillar_indices.pop()]
            width = i if not pillar_indices else i - pillar_indices[-1] - 1 # - 1 because we are counting from the index ahead of the one which has been popped
            if width >= height: #only calculate area if width is >= height else don't
                max_rectangle_area = max(max_rectangle_area, height * height)
            else:
                continue
        pillar_indices.append(i)#we are appending index only
    return max_rectangle_area

calculate_largest_square([1, 4, 2, 5, 6, 3, 2, 6, 6, 5, 2, 1, 3])
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('17-08-largest_rectangle_under_skyline.py',
                                       'largest_rectangle_under_skyline.tsv',
                                       calculate_largest_rectangle))
