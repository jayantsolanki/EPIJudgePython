from functools import cache
from test_framework import generic_test

"""
Leetcode 62. Unique Paths
https://leetcode.com/problems/unique-paths/
Write a program that counts how many ways you can go from the top-left to the bottom-right of a 2-D array.
Logic:
    you can reach position(i, j) either from position(i-1, j) or position(i, j - 1) Thats all
    Remember; If i == 0 or j == 0, there is only one way to get to position(i, j) from the origin
Time and Space = O(mn)
"""
#top_down
def number_of_ways_mem(m: int, n: int) -> int:
    @cache
    def dp(i, j):#we walk backwards
        if i == 0 and j == 0:#why setting this to 1, because once we reach the first row or column, we only
            #go up or left in one way
            return 1
        elif i < 0 or j < 0:#optional edge case for boundary check
            return 0
        else:
            return dp(i - 1, j) + dp(i, j- 1)
    return dp(m - 1, n - 1)

#bottom-up
#start building from base cases
def number_of_ways(m: int, n: int) -> int:

    cache = [[0] * n for _ in range(m)]
    
    #setting base cases
    for i in range(m):#first col = 1
        cache[i][0] = 1
    for j in range(n): #first row =1
        cache[0][j] = 1
        
    for i in range(1, m):
        for j in range(1, n):
            cache[i][j] = cache[i - 1][j] + cache[i][j - 1]
    
    return cache[-1][-1]

#variant 1, solve it in O(min(m,n)) space
#space efficient, since we need to track two places, one place is on the same column a row above, and other place
# is in same row a index place behind, hence we store the first place in a variable and refer second place from same
# cache array
def number_of_ways_space_efficient(m, n):
    if n < m: # m is supposed to be small at the end
        n, m = m, n

    cache = [1] * m # think in terms of trasnpose, the shorter side become the columns
    for _ in range(1, n):
        prev_res = 0
        for j in range(m):
            cache[j] += prev_res
            prev_res = cache[j]
    return cache[m - 1]

#variant  2
"""
Leetcode: 63. Unique Paths II
https://leetcode.com/problems/unique-paths-ii/
Solve the same problem in presence of obstacles, specified by a boolean 2d array, where the presence of a true
value represents and obstacle.
Logic:
    In topdown approach, once we encounter a obstacle, we stop going forward in that direction
    In bottom-up approach, once a find a obstacle, we dont go right any more in that row, if obstacle was at right
    similarly, we dont go down anymore in that column, if obstacle is just below current position

"""
from typing import List
#topdown
def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    if obstacleGrid[0][0] == 1:
        return 0
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    @cache
    def dp(i, j):#we walk backwards
        if obstacleGrid[i][j] == 1:#this should remain at the top, because obstacle can be at top row or first column
            return 0
        elif (i == 0 and j == 0):#why setting this to 1, because once we reach the first row or column, we only
            #go up or left in one way
            return 1
        else:
            ans = 0
            if i - 1 >= 0 and obstacleGrid[i - 1][j] != 1:#stop going up in that column if obstacle found
                ans = dp(i - 1, j)
            if j - 1 >= 0 and obstacleGrid[i][j - 1] != 1: # stop going left in that row if obstacle encountered
                ans += dp(i, j - 1)
            return ans
    return dp(m - 1, n - 1)
#bottom-up
def uniquePathsWithObstacles_iter(obstacleGrid: List[List[int]]) -> int:
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    cache = [[0] * n for _ in range(m)]
    
    #setting base cases
    for i in range(m):#first col = 1
        if obstacleGrid[i][0] != 1:
            cache[i][0] = 1
        else:#break because after obstacles is encountered you can go anymore left in cells after that obstacle
            break
    for j in range(n): #first row =1
        if obstacleGrid[0][j] != 1:
            cache[0][j] = 1
        else:#break because after obstacles is encountered you can go anymore down in cells after that obstacle
            break
        
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] != 1:
                cache[i][j] = cache[i - 1][j] + cache[i][j - 1]
            else:
                cache[i][j] = 0
                    
    return cache[-1][-1]

#variant 3
"""
A fisherman is in a rectangular sea. The value of each fish at point(i, j) in the sea is specified by array of mxn A.
Find maximum catch a fisherman can have before it reaches bottom-right of that array. Fisherman can go right or down only at 
a time.
Similar to 64. Minimum Path Sum, https://leetcode.com/problems/minimum-path-sum/
"""
#topdown
def maxPathSum_mem2(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    
    @cache
    def dp(i, j):#we walk backwards
        if i == 0 and j == 0:# because once we reach the first row or column, we only
            #go up or left in one way
            return grid[i][j]
        elif i < 0 or j < 0:
            return float("-Inf")
        else:
            return max(dp(i - 1, j), dp(i, j - 1)) + grid[i][j]
    return dp(m - 1, n - 1)

#bottom_up
# we start from bottom, and add extra row and column as padding
def maxPathSum(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    
    cache = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m - 1, -1 , -1):
        for j in range(n - 1, -1 , -1):
            if  j == n - 1:
                cache[i][j] = cache[i + 1][j] + grid[i][j]
            elif i == m - 1:
                cache[i][j] = cache[i][j  + 1] + grid[i][j]
            else:
                cache[i][j] = min(cache[i + 1][j], cache[i][j + 1]) + grid[i][j]
    return cache[0][0]

# #variant 4
# """
# Same at above, but now, fisherman can bang and end its trip at any point, he must still move down or right
# """
# def maxPathSum_mem3(grid: List[List[int]]) -> int:
#     m, n = len(grid), len(grid[0])
    
#     @cache
#     def dp(i, j):#we walk forward
#         if i == m - 1 and j == n - 1:#why setting this to 1, because once we reach the first row or column, we only
#             #go up or left in one way
#             return grid[i][j]
#         elif i >= m or j >= n:
#             return float("Inf")
#         else:
#             return min(dp(i + 1, j), dp(i, j + 1)) + grid[i][j]
#     return dp(0, 0)

#variant 5
"""
Write a program which takes as input a positive integer k and computes the number of decimal numbers of length k that are monotone
"""
'''
def monotoneIncreasingDigits_wrong(n: int) -> int:
    n = str(n)
    m = len(n)
    @cache
    def dp(i):
        if i == m:
            return 1
        else:
            if i + 1 < m and int(n[i] <= n[i + 1]):
                return max(dp(i + 1), dp(i + 1) + 1)
            else:
                return dp(i + 1)
        
    return dp(0)
'''
#correct version
def monotoneIncreasingDigits(n: int) -> int:
    n = str(n)
    m = len(n)
    count = 1
    maxCount = 1
    for i in range(1, m):
        if n[i] >= n[i - 1]:
            count = count + 1
        else:
            maxCount = max(count, maxCount)
            count = 1
    return max(count, maxCount)
        



# monotoneIncreasingDigits(3456123)
# monotoneIncreasingDigits(1203)
# monotoneIncreasingDigits(4312)
# monotoneIncreasingDigits(2410212345)

#variant 6:
"""same as above but strictly monotone
"""
def monotoneIncreasingDigits(n: int) -> int:
    n = str(n)
    m = len(n)
    count = 1
    maxCount = 1
    for i in range(1, m):
        if n[i] > n[i - 1]:
            count = count + 1
        else:
            maxCount = max(count, maxCount)
            count = 1
    return max(count, maxCount)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('16-03-number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
