import functools
import random
from typing import List

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient, check_sequence_is_uniformly_random,
    compute_combination_idx, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook

"""
Implement an algorithm that takes as input an array of distinct elements and a size, and returns a subset of the given 
size and array elements
All subsets should be equally likely. Return the result in input array itself
Time: O(k), space: O(1 )
Logic: build one index at a time, then replace that index with index at 0, then go on
"""
def random_sampling(k: int, A: List[int]) -> None:

    for i in range(k):
        # Generate a random index in [i, len(A) - 1].
        # r = random.randint(i, len(A) - 1) # Return a random integer N such that a <= N <= b
        #this and above are same, this line is same as choice(range(start, stop, step)), ignores last value(stop)
        r = random.randrange(i, len(A)) 
        A[i], A[r] = A[r], A[i]#this is the key, this makes sure that all numbers are equally likely to appear
    return A[:k]

random_sampling(2, [3,7,5,11])

# Pythonic solution
def random_sampling_pythonic(k, A):
    A[:] = random.sample(A, k)


@enable_executor_hook
def random_sampling_wrapper(executor, k, A):
    def random_sampling_runner(executor, k, A):
        result = []

        def populate_random_sampling_result():
            for _ in range(100000):
                random_sampling(k, A)
                result.append(A[:k])

        executor.run(populate_random_sampling_result)

        total_possible_outcomes = binomial_coefficient(len(A), k)
        A = sorted(A)
        comb_to_idx = {
            tuple(compute_combination_idx(A, len(A), k, i)): i
            for i in range(binomial_coefficient(len(A), k))
        }

        return check_sequence_is_uniformly_random(
            [comb_to_idx[tuple(sorted(a))] for a in result],
            total_possible_outcomes, 0.01)

    run_func_with_retries(
        functools.partial(random_sampling_runner, executor, k, A))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('5-12-offline_sampling.py',
                                       'offline_sampling.tsv',
                                       random_sampling_wrapper))
