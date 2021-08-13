from typing import List

from test_framework import generic_test

"""
WAP that takes an array denoting the daily stock price and returns the maximum profit that could be made
by buying and then selling on share of that stock. There is no need to buy if no profit is possible
"""


def buy_and_sell_stock_once(prices: List[float]) -> float:
    min_price_so_far, max_profit = float('Inf'), 0.0

    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('5-06-buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
