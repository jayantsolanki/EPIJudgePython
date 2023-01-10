from typing import List

from test_framework import generic_test

"""
MAX Difference Problem:
WAP that takes an array denoting the daily stock price and returns the maximum profit that could be made
by buying and then selling on share of that stock. There is no need to buy if no profit is possible
Example: [310, 315, 275, 295, 260, 270, 290, 230, 255, 250], so buy at 260 and sell at 290, profit of 30
Logic: Focus on maximum difference, instead of min and max
Logic: maximum profit can be made by selling on specifc day is determined  by the minimum of the stock prices over the previous days 
Iterate through S, keeping track of minimum price seen so far.
Below algo has time complexity of O(n)
"""


def buy_and_sell_stock_once(prices: List[float]) -> float:
    min_price_so_far, max_profit = float('Inf'), 0.0
    # print("price, min_price_so_far, max_profit, max_profit_sell_today")
    for price in prices:#iterate thorugh days keeping track of minimum element seen thus far
        min_price_so_far = min(min_price_so_far, price)
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)#overall max profit
        # print(price, min_price_so_far, max_profit, max_profit_sell_today)
    return max_profit

print(buy_and_sell_stock_once([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))

"""
WAP that takes an array of integers and finds the length of a longest subarray all of whose enteries are equal
Can be done in O(n) I believe
"""

def longestSubArray(A):
    if not A:
        return 0
    count = 1 # well it will be at least one haha!
    longest = 1

    for i in range(1, len(A)):
        if A[i-1]!=A[i]:
            longest = max(longest, count)
            count = 1
        else:
            count += 1
    return max(longest, count)# using max here too, for edge case, element at last


print(longestSubArray([310, 310, 310, 20, 310, 310, 315, 275, 295, 260, 270, 270, 270, 290, 230, 255, 255, 255, 255, 255]))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('5-06-buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
