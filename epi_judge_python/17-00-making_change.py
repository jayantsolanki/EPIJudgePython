from test_framework import generic_test


"""
Write a program to find minimum number of coins for a change (US coins)
Logic:
    Greedy strategy will work here, since they are US coins
    We pick the highest coins first
"""
def change_making(cents: int) -> int:
    total_count = 0
    coins = [100, 50, 25, 10, 5, 1] #must be sorted in reverse
    for coin in coins:
        total_count += cents // coin
        cents = cents % coin
    return total_count

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('17-00-making_change.py', 'making_change.tsv',
                                       change_making))
