from test_framework import generic_test

# 509. Fibonacci Number, know all first 4 approaches, https://leetcode.com/problems/fibonacci-number/
#method 1 using recursion and memoization
# Time and Space : O(n)
cache = {}
def fibonacci_rec(n: int) -> int:
    
    if n <= 1:
        return n
    elif n not in cache:
        cache[n] = fibonacci_rec(n - 1) + fibonacci_rec(n - 2)
        # return cache[n]
    # else:
    return cache[n]
fibonacci_rec(3)

#method 2, iteration
# Time O(n) and and Space : O(1), using same caching but filling it bottomup fashion
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    fib_1 = 1
    fib_2 = 0
    for _ in range(2, n+1):
        fib = fib_1 + fib_2
        fib_1, fib_2 = fib, fib_1
    return fib


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('16-00-fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
