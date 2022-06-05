import functools
import random
from typing import Dict, List

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient, check_sequence_is_uniformly_random,
    compute_combination_idx, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook

"""
WAP that takes input positive integer n and a size k <=n, and returns a size-k subset of {0,1,2,3,4,...n-1}
"""
#you can use offline random sampling, but this could be O(n) for both time and space, since the original array needs to be generated first
# in order to reduce it to the O(k)  
#
def random_subset(n: int, k: int) -> List[int]: 

    changed_elements: Dict[int, int] = {}
    for i in range(k):#no need to create an array, unlike in problem 5.12
        # Generate a random index between i and n - 1, inclusive.
        rand_idx = random.randrange(i, n)
        #now try to get the index which has been mapped to this random number
        rand_idx_mapped = changed_elements.get(rand_idx, rand_idx)#second parameter is default value, in case index doesnt exist
        #now see if curernt index is mapped or not, return the value of random number if mapped
        i_mapped = changed_elements.get(i, i)# initially A[i] = i, these are untouchd ones
        changed_elements[rand_idx] = i_mapped # this makes sure if the number is repeated it wont get stored again
        changed_elements[i] = rand_idx_mapped
    return [changed_elements[i] for i in range(k)]


@enable_executor_hook
def random_subset_wrapper(executor, n, k):
    def random_subset_runner(executor, n, k):
        results = executor.run(
            lambda: [random_subset(n, k) for _ in range(100000)])

        total_possible_outcomes = binomial_coefficient(n, k)
        comb_to_idx = {
            tuple(compute_combination_idx(list(range(n)), n, k, i)): i
            for i in range(binomial_coefficient(n, k))
        }
        return check_sequence_is_uniformly_random(
            [comb_to_idx.get(tuple(sorted(result)), 0) for result in results],
            total_possible_outcomes, 0.01)

    run_func_with_retries(
        functools.partial(random_subset_runner, executor, n, k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('5-15-random_subset.py', 'random_subset.tsv',
                                       random_subset_wrapper))
