from typing import List

from test_framework import generic_test

"""
WAP to that computes the maximum profit that can be made by buying and selling a share at most twice.
The second buy must be made on another date after the first sale
I will suggest to go for version 3
"""

"""
Brute:
Max profit with at most two transactions =
       MAX {max profit with one transaction and subarray price[0..i] +
            max profit with one transaction and subarray price[i+1..n-1]  }
i varies from 0 to n-1.
Maximum possible using one transaction can be calculated using the following O(n) algorithm 
The maximum difference between two elements such that the larger element appears after the smaller number
The time complexity of the above simple solution is O(n2)
"""

"""
We can do this O(n) time complexity and O(n) sapce complexity, using the following Efficient Solution. 
The idea is to store the maximum possible profit of every subarray and solve the problem in the following two phases.
1) Create a table profit[0..n-1] and initialize all values in it 0.
2) Traverse price[] from left to right and update profit[i] such that profit[i] stores maximum profit such that profit[i] 
    contains maximum achievable profit from two transactions in subarray price[0..i].
3) Traverse price[] from right to left and update profit[i] such that profit[i] stores maximum profit achievable from one transaction in subarray price[i..n-1]
4) Return profit[n-1]

To do step 3, we need to keep track of the maximum price from right to left side, and to do step 2, 
we need to keep track of the minimum price from left to right. 
Why we traverse in reverse directions? The idea is to save space, in the third step, 
we use the same array for both purposes, maximum with 1 transaction and maximum with 2 transactions. 
---Not application....After iteration i, the array profit[0..i] contains the maximum profit with 1 transactions, 
and profit[i+1..n-1] contains profit with two transactions.---
In step 3, when we move backward, we keep track of sum of both profits: M[i] = B[i] + F[i-1]
Since, the first profite should be taken a day earlier, hence i-1
"""


def buy_and_sell_stock_twice(prices: List[float]) -> float:

    max_total_profit, min_price_so_far = 0.0, float('Inf')
    first_buy_sell_profits = [0.0] * len(prices)
    # forward phase,. For each day, we record maximum profit if we sell on that
    # day
    for i, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)
        max_total_profit = max(max_total_profit, price - min_price_so_far)
        first_buy_sell_profits[i] = max_total_profit

    # backward phase. For each day, find the maximum profit if we make the
    # second buy on that day
    max_price_so_far = float('-Inf')
    for i, price in reversed(list(enumerate(prices[1:], 1))):
    #for i, price in reversed(list(enumerate(prices[0:], 1))): this also works
        # list(enumerate([11,12,13,14,15], 1))  = [(1, 11), (2, 12), (3, 13), (4, 14), (5, 15)]
        # list(enumerate([11,12,13,14,15])) = [(0, 11), (1, 12), (2, 13), (3, 14), (4, 15)]
        max_price_so_far = max(max_price_so_far, price)
        max_total_profit = max(
            max_total_profit,
            (max_price_so_far - price) + first_buy_sell_profits[i-1] # adding both profits
            # M[i] = B[i] + F[i-1]
        )
    return max_total_profit

"""
Another take, easier to understand for my poor mind
"""

def buy_and_sell_stock_twice_v2(prices):

    max_total_profit, max_total_profit2, min_price_so_far = 0.0, 0.0, float('Inf')
    first_buy_sell_profits = [0.0] * len(prices)
    profits_reversed = [0.0] * len(prices)
    overall_profit = [00.]*len(prices)
    # forward phase,. For each day, we record maximum profit if we sell on that
    # day
    for i, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)
        max_total_profit = max(max_total_profit, price - min_price_so_far)
        first_buy_sell_profits[i] = max_total_profit

    # backward phase. For each day, find the maximum profit if we make the
    # second buy on that day
    print(first_buy_sell_profits)
    max_price_so_far = float('-Inf')
    # for i, price in reversed(list(enumerate(prices[1:]))):#had to use list, since you cannot reverse enumerate directlty
    for i in range(len(prices)-1, 0, -1):#had to use list, since you cannot reverse enumerate directlty
        max_price_so_far = max(max_price_so_far, prices[i])
        max_total_profit2 = max(max_total_profit2, max_price_so_far - prices[i])
        print(prices[i], max_total_profit2, i)
        # profits_reversed.append(max_total_profit2)
        profits_reversed[i] = max_total_profit2 
        overall_profit[i] = profits_reversed[i] + first_buy_sell_profits[i-1] # M[i] = B[i] + F[i-1]
        max_total_profit = max(max_total_profit, overall_profit[i])
        # F is profit in first pass (left to right), B is profit in second pass, right to left
    print(profits_reversed)
    print(overall_profit)
    return max_total_profit

# concise version of above
def buy_and_sell_stock_twice_v3(prices):

    max_total_profit, max_total_profit2, min_price_so_far = 0.0, 0.0, float('Inf')
    first_buy_sell_profits = [0.0] * len(prices)
    # forward phase,. For each day, we record maximum profit if we sell on that
    # day
    for i, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)
        max_total_profit = max(max_total_profit, price - min_price_so_far)
        first_buy_sell_profits[i] = max_total_profit

    # backward phase. For each day, find the maximum profit if we make the
    # second buy on that day
    max_price_so_far = float('-Inf')
    for i in range(len(prices)-1, 0, -1):#go till second element, since first is not need, need to buy and sell twice, 
        # cant happen on day 1 itself
        max_price_so_far = max(max_price_so_far, prices[i])
        max_total_profit = max(max_total_profit, (max_price_so_far - prices[i]) + first_buy_sell_profits[i-1])
        # i used max_total_profit, saved one variable haha
        # max_total_profit = max(max_total_profit, max_total_profit2 + first_buy_sell_profits[i-1])
    return max_total_profit

print(buy_and_sell_stock_twice_v3([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))
print(buy_and_sell_stock_twice([12,11,13,9,12,8,14,13,15]))
print(buy_and_sell_stock_twice_v3([12,11,13,9,12,8,14,13,15]))


"""
Variant: 1
Solve above problem O(n) time complexity O(1) space complexity
"""
def buy_and_sell_stock_twice_v4 (prices):

# if __name__ == '__main__':
#     exit(
#         generic_test.generic_test_main('5-07-buy_and_sell_stock_twice.py',
#                                        'buy_and_sell_stock_twice.tsv',
#                                        buy_and_sell_stock_twice))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('5-07-buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice_v3))
