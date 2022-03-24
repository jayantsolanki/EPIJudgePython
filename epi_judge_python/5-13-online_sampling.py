import functools
import itertools
import random
from typing import Iterator, List

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient, check_sequence_is_uniformly_random,
    compute_combination_idx, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook

"""
Design a program that takes as input a size k, and reds packets, continuously maintaining
a uniform random subset of size k of the read packets
Time: O(k), space: O(1)
"""
# Assumption: there are at least k elements in the stream.
def online_random_sample(stream: Iterator[int], k: int) -> List[int]:

    # Stores the first k elements.
    running_sample = list(itertools.islice(stream, k))#islice(iterable, start, stop, step): always takes first k elements
    # Have read the first k elements.
    num_seen_so_far = k
    for x in stream:
        num_seen_so_far += 1
        # Generate a random number in [0, num_seen_so_far - 1], and if this
        # number is in [0, k - 1], we replace that element from the sample with
        # x.
        idx_to_replace = random.randrange(num_seen_so_far)
        if idx_to_replace < k:
            running_sample[idx_to_replace] = x
    return running_sample

online_random_sample(range(20), 5)#this is a bad example for input, since the numbers can be repeated

@enable_executor_hook
def online_random_sample_wrapper(executor, stream, k):
    def online_random_sample_runner(executor, stream, k):
        results = executor.run(
            lambda:
            [online_random_sample(iter(stream), k) for _ in range(100000)])

        total_possible_outcomes = binomial_coefficient(len(stream), k)
        stream = sorted(stream)
        comb_to_idx = {
            tuple(compute_combination_idx(stream, len(stream), k, i)): i
            for i in range(binomial_coefficient(len(stream), k))
        }
        return check_sequence_is_uniformly_random(
            [comb_to_idx.get(tuple(sorted(result)), 0) for result in results],
            total_possible_outcomes, 0.01)

    run_func_with_retries(
        functools.partial(online_random_sample_runner, executor, stream, k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('5-13-online_sampling.py',
                                       'online_sampling.tsv',
                                       online_random_sample_wrapper))
