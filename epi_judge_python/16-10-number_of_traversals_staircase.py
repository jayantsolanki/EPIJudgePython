from functools import cache
from test_framework import generic_test

"""
Leetcode: 70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/

Write a program which takes as inputs n and k and returns the number of ways in which you can get to your destinations.
Logic:
    We start from last step, if we reach step zero, then we mark that count as 1 for that specific combination
    Similarly, we try to generate as many as combo using for loop and recursion, we can use same step size as many times
    This problem is that why different then coin change problem for finding different combos of coins required to reach a 
    specfic value, since in coin change, we are not concerned for the order of coin used. But here in climbing
    we are concerend over the order of steps used. Refer 16-01-number_of_score_combinations.py
Time: O(nk), since we take O(k) time to file in each entry, k is less, it can be O(n)
Space: O(n)
"""
#topdown
def number_of_ways_to_top(top: int, maximum_step: int) -> int:
    @cache
    def climb(steps_left):
        if steps_left == 0:#this means you have reached your destination
            return 1
        elif steps_left < 0:
            return 0
        else:
            ans = 0
            for step in range(1, maximum_step + 1):
                ans += climb(steps_left - step)
            return ans
    return climb(top)

#bottom up, not able to figure out
# def number_of_ways_to_top(top: int, maximum_step: int) -> int:
#     if top == 1:
#         return 1
        
#     # An array that represents the answer to the problem for a given state
#     # dp = [0] * (top + 1)
#     dp = [[0] * (top + 1) for _ in range(maximum_step + 1)]
#     dp[0][0] = 1
#     for i in range(maximum_step + 1): #setting base case sum = 0 equals 1
#         dp[i][0] = 1
#     # dp[1] = 1 # Base cases #dp[0] not used
#     # dp[2] = 2 # Base cases
#     # for i in range(1, top + 1):
#     #     for j in range(1, maximum_step + 1):
#     #         print(i, j)
#     #         if j <= i:
#     #             dp[j][i] = dp[j - 1][i] + dp[j][i - j]
#     #         else:
#     #             dp[j][i] = dp[j - 1][i]
#     #         print(dp)
#     for i in range(1, top + 1):
#         for j in range(1, maximum_step + 1):
#             print(i, j)
#             if j <= i:
#                 dp[j][i] = dp[j][i - j] + dp[j][i - 1]
#             else:
#                 dp[j][i] = dp[j][i - 1]
#             print(dp)

#     return dp[maximum_step][top]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('16-10-number_of_traversals_staircase.py',
                                       'number_of_traversals_staircase.tsv',
                                       number_of_ways_to_top))
