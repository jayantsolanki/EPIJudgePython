from functools import cache
from typing import List

from test_framework import generic_test

"""
Leetcode: 518
https://leetcode.com/problems/coin-change-2
# https://leetcode.com/problems/climbing-stairs/, Leetcode 70. Climbing Stairs
Write a program that takes a final score and scores for individual plays, and returns the number of
combinations of plays that result in the final score.
Similar to coin change method to erach a specific amount
Logic:
    For topdown, our solutions can be divided into two sets,
        1) Solutions that cointain the coin/score at the end of the coins array 
        2) Solutions that don't contain that coin/score
        Above two will be the recurrence state transition. With coin index and amount at the state variables being used

    For bottom up, we use the tabluation method, which has the same recurrence transition as above
    https://www.youtube.com/watch?v=_fgjrs570YE&ab_channel=TusharRoy-CodingMadeSimple
    Here we create a 2-d array, whose row signify the combination of coins going to be used, for example
    if coins are [1, 2, 3], then the 2-d array will have 3 rows where eaach consecutive row represents:
    coin 1, coin 1 and coin 2, coin 1 2, and 3. That is row 1 will use only coin 1 to sum up the total amount
    row 2 will use either coin 1 or coin 2 or both to sum total amount, and so on. To get sum 0 with coins {1,2,3} 
    there is only one way that is using nothing. We should try to observe that addition of new coin will not affect 
    previous permutations, only new permutations will be added.Remember this.
    There are two choices for every coin (to include it in our set or to exclude it) 
    1.Include it(when we include it,the equal amount is subtracted from our amount combinations[amount -coin])
    2.Exclude it( No deduction form the amount combination(amount))
Time complexity = O(nm), same for space
"""



#top_down method
#here just pass the index that has to be excluded
def num_combinations_for_final_score_mem(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    # individual_play_scores.sort()#optional            
    # #larger coins/score divide the amount less times than smaller coins. 
    #This reduces the overall branching factor if the recursion starts with them                 
    num_scores = len(individual_play_scores)
    @cache
    def dp(s, i):
        if s == 0:#found the desired amount
            return 1
        elif i == num_scores or s < 0:
            return 0
        else:
            #Our solutions can be divided into two sets,
            #   1) Solutions that contain the coin/score at the end of the coins array 
            #   2) Solutions that don't contain that coin/score
            return dp(s - individual_play_scores[i], i) + dp(s, i+1)#basically you use that coin/score at i and you didnt use that coin/score at i
    return dp(final_score, 0)

#bottom-up
def num_combinations_for_final_score_ori(final_score: int,
                                     individual_play_scores: List[int]) -> int:

    # One way to reach 0.
    num_combinations_for_score = [[1] + [0] * final_score
                                  for _ in individual_play_scores]
    for i in range(len(individual_play_scores)):
        for j in range(1, final_score + 1):
            without_this_play = (num_combinations_for_score[i - 1][j]
                                 if i >= 1 else 0)
            with_this_play = (
                num_combinations_for_score[i][j - individual_play_scores[i]]
                if j >= individual_play_scores[i] else 0)
            num_combinations_for_score[i][j] = (without_this_play +
                                                with_this_play)
    return num_combinations_for_score[-1][-1]


#bottom-up dp, simple
#bottom-up my preferred, Time and Space O(n.k), where n is total sum/scores, k is number of scoring/coins needed
def num_combinations_for_final_score_iter2(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    dp = [[0 for _ in range((final_score + 1))] for _ in range(len(individual_play_scores))]#each column signify sum to be created
    # each item in that array will store the number of ways to create the sum at i, j
    for i in range(len(individual_play_scores)): #setting base case sum = 0 equals 1
        dp[i][0] = 1

    for i in range(len(individual_play_scores)):#important to have this on top
        for j in range(1, final_score + 1):
            if individual_play_scores[i] <= j:#important, to check negative
                dp[i][j] = dp[i - 1][j]+ dp[i][j - individual_play_scores[i]]
            else:
                dp[i][j] = dp[i - 1][j]#current coin is greater, hence just use the lesser coins
    return dp[-1][-1]


#variant 1
"""
Solve the same problem using O(s) time
"""
#Second bottom-up try
# Time O(nk) and Space O(n), where n is total sum
#memory optimized and time optmized
"""
Since we are just copying the previous row and editing it , we can just reuse single row 
https://www.youtube.com/watch?v=jaNZ83Q3QGc&t=311s&ab_channel=StephenO%27Neill
I would say the dp formula dp[x] += dp[x - coin] can be explained as
The combination of i number of coins to make change for j amount = The combination when we not using ith coin to make 
change for j amount + The combination when we use ith coin to make change for j amount.

It likes knapsack problem, calculate the result when we pick the current coin and not pick it and get the total
"""
def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    dp = [0 for _ in range((final_score + 1))]
    dp[0] = 1

    for score in individual_play_scores:
        # prev = dp[:]
        for x in range(1, final_score + 1):
            if score <= x:
                dp[x] = dp[x]+ dp[x - score]
    return dp[-1]
    

#variant 2
"""
Similar to stairs climbing ways
Write a program that takes a final score and scores for individual plays, and returns the number of sequences of plays that
result in the final score. It is a permutation not combination like previous ones
Logic, invert the loop, since we need to reuse the coins, inverting the loop gives us the chance to reuse someother coins
"""
# dp approach
def num_combinations_for_final_score_sequences(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    dp = [0 for _ in range((final_score + 1))]
    dp[0] = 1
    for x in range(1, final_score + 1):
        for score in individual_play_scores:
            if score <= x:
                dp[x] = dp[x]+ dp[x - score]
    return dp[-1]
num_combinations_for_final_score_sequences(12, [2, 3, 7]) #18
#recursion approach (top down)

def num_combinations_for_final_score_sequences_mem(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    @cache
    def dp(s):
        if s == 0:#found the desired amount
            return 1
        elif s < 0:
            return 0
        else:
            #Our solutions can be divided into two sets,
            #   1) Solutions that cointain the coin/score at the end of the coins array 
            #   2) Solutions that don't contain that coin/score
            ans = 0
            for score in individual_play_scores:
                ans += dp(s - score)
            return ans
    return dp(final_score)                                  

num_combinations_for_final_score_sequences_mem(12, [2, 3, 7]) #18

#variant 3:
"""
Suppose the final score is given in the form (s, s'), that is , Team 1 scores s and team 2 scores s' points. How would 
you compute the number of distinct scoring sequences which result in this score? For example, if the final score is (6, 3)
then Team 1 scores 3, team 2 scores 3, Team 1 scores 3, is a scoring sequence which result in the score.
It is a permuttion problem. 
Total permutation  =  number of sequence in first team X number of sequence in the second team
"""

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('16-01-number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))



