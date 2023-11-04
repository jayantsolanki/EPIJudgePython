import copy
import functools
import math
from typing import List

import importlib  
random_sampling = importlib.import_module("5-12-offline_sampling")
# from '5-12-offline_sampling' import random_sampling
from test_framework import generic_test
from test_framework.random_sequence_checker import (
    check_sequence_is_uniformly_random, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook

"""
Design an algorithm that creates uniformly random permutations of [0, 1, 2, 3, ... n-1]. 
You are given a random number generator that returns integers in the set [0, 1,2,3,4,...n-1] with equal probability. 
Use as few calls as possible.
Logic: 
A brute-force approach might be to iteratively pick a random number between the [0, n-1] range. If the number repeats we drop it, Use hash map to check if the number repeats.
Time is little challenging to analyse since number could be repeated. Early iterations will get more new values, but it takes long time to collect the last few values. This is a classic Coupon Collector problem. Time (nlogn) on average, Space O(n)
Better way:
We can avoid repeats by restricting the set from where we choose the random numbers (randrange(i, n-1))
same as offline sampling, but we do it for whole n, instead of kline sampling, but we do it for whole n, instead of k
time O(n)
"""

def compute_random_permutation(n: int) -> List[int]:

    permutation = list(range(n))
    random_sampling.random_sampling(n, permutation)
    return permutation


@enable_executor_hook
def compute_random_permutation_wrapper(executor, n):
    def compute_random_permutation_runner(executor, n):
        def permutation_index(perm):
            p = copy.deepcopy(perm)
            idx = 0
            n = len(p)
            while p:
                a = p.pop(0)
                idx += a * math.factorial(n - 1)
                for i, b in enumerate(p):
                    if b > a:
                        p[i] -= 1
                n -= 1
            return idx

        result = executor.run(
            lambda: [compute_random_permutation(n) for _ in range(1000000)])

        return check_sequence_is_uniformly_random(
            [permutation_index(perm) for perm in result], math.factorial(n),
            0.01)

    run_func_with_retries(
        functools.partial(compute_random_permutation_runner, executor, n))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('5-14-random_permutation.py',
                                       'random_permutation.tsv',
                                       compute_random_permutation_wrapper))
