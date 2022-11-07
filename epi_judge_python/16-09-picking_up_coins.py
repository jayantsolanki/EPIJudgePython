from functools import cache
from typing import List

from test_framework import generic_test

"""
Pick up coins for maximum gain
Leetcode:877. Stone Game
https://leetcode.com/problems/stone-game/
Design an efficient algo for computing the maximum total value for the starting player in the pick-up-coins game
Note: it is for the player who starts first
Logic: 
    Since total values of coins are constant, use minmax theory, that is we pick the coin to maximize our gain, but make sure the way we pick 
    it in such a way that the options left for opponent will be have its gain minimized.
Time: O(n*2), because dp formula has two parameters, i will go from 0 to m /2, j will go from m to m/2 
Same for time
"""
#my way
def maximum_revenue(coins: List[int]) -> int:
    m = len(coins)
    # total = sum(coins)
    @cache
    def calc(i, j):
        if i > j:#stop picking once i > j
            return 0
        else:
            return max( coins[i] + min(calc(i + 2, j), calc(i + 1, j - 1)),  #i+2, means second player picks the next coin from same side picked by first player
                coins[j] + min(calc(i, j - 2), calc(i + 1, j - 1)))
    ans = calc(0, m - 1)
    return ans

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('16-09-picking_up_coins.py',
                                       'picking_up_coins.tsv',
                                       maximum_revenue))
