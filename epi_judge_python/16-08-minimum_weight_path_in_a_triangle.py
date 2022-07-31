from functools import cache
from typing import List

from test_framework import generic_test

"""
Leetcode: 120. Triangle
https://leetcode.com/problems/triangle/
Similar to https://leetcode.com/problems/maximum-number-of-points-with-cost/, 1937. Maximum Number of Points with Cost
Write a program that takes as input a triangle of numbers and returns the weight of a minimum weight path.
Note: you may move to either index i or index i + 1 on the next row
Logic:
    Just note the possible moves for next row, and recurse from there, do take note of first column, last column and last 
    row edge cases
Time complexity: O(n^2), Space O(n^2)
"""
#my take, 
def minimum_path_weight_mem(triangle: List[List[int]]) -> int:
    height = len(triangle)
    
    @cache
    def check_down(i, j):
        if i == height:
            return 0
        elif j == len(triangle[i]):
            return 0
        else:
            # you may move to either index i or index i + 1 on the next row
            return triangle[i][j] + min(check_down(i+1, j), check_down(i+1, j+1))
        
    return check_down(0, 0)

#bottom_up
# Time and Space O(height^2)
def minimum_path_weight_iter1(triangle: List[List[int]]) -> int:
    if len(triangle) == 0:
        return 0
    height = len(triangle)
    cache = [[0] * len(triangle[j]) for j in range(height)]
    cache[0][0] = triangle[0][0]
    minima = cache[0][0]

    for i in range(1, height):
        minima = float('Inf')
        for j in range(len(triangle[i])):
            if i == 1:#second row
                cache[i][j] = triangle[i][j] + cache[i - 1][0]
            elif j - 1 >= 0 and j <= i - 1:#neither first column or last column
                cache[i][j] = triangle[i][j] + min(cache[i - 1][j], cache[i - 1][j - 1])
            elif j - 1 >= 0 and j > i - 1: # last column
                cache[i][j] = triangle[i][j] + cache[i - 1][j - 1]
            else: #first column
                cache[i][j] = triangle[i][j] + cache[i - 1][j]
            minima = min(cache[i][j], minima)
    return minima
#improved Space O(height)
def minimum_path_weight(triangle: List[List[int]]) -> int:
    if len(triangle) == 0:
        return 0
    height = len(triangle)
    cache = [0] * height
    cache[0] = triangle[0][0]
    minimum_weight_to_current_row = triangle[0][0]

    for i in range(1, height):
        minimum_weight_to_current_row = float('Inf')
        for j in range(len(triangle[i]) - 1, - 1, -1):# you have to do in reverse, since result caclualted in nonreverse 
            #order wont work, try to do it manually on copy, you will know
            if i == 1:#second row
                cache[j] = triangle[i][j] + cache[0]
            elif j - 1 >= 0 and j <= i - 1:#neither first column or last column
                cache[j] = triangle[i][j] + min(cache[j], cache[j - 1])
            elif j - 1 >= 0 and j > i - 1: # last column
                cache[j] = triangle[i][j] + cache[j - 1]
            else: #first column
                cache[j] = triangle[i][j] + cache[j]
            minimum_weight_to_current_row = min(cache[j], minimum_weight_to_current_row)
            # print(i, j, cache, minimum_weight_to_current_row)
    return minimum_weight_to_current_row


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            '16-08-minimum_weight_path_in_a_triangle.py',
            'minimum_weight_path_in_a_triangle.tsv', minimum_path_weight))
