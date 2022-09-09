import collections
import functools
import math
from typing import List
import itertools
import bisect
import random 
from test_framework import generic_test
from test_framework.random_sequence_checker import run_func_with_retries
from test_framework.test_utils import enable_executor_hook
import numpy 

#you run below function X times and see each element in the List return with count corresponding to their probability
#naive implementation
#time: O(n). space: O(1)
def nonuniform_random_number_generation_naive(values: List[int],
                                        probabilities: List[float]) -> int:
    r = random.random()#first generate the random number, 
    p = 0
    for i in range(len(probabilities)):#create pdf on the fly, then check where the value belongs
        p = p + probabilities[i]#making a pdf graph
        if r < p:#yes less than, instead of <=
            return values[i]

#book implementation
#time: O(logn). space: O(n)
def nonuniform_random_number_generation(values: List[int],
                                        probabilities: List[float]) -> int:

    prefix_sum_of_probabilities = list(itertools.accumulate(probabilities)) # space and time O(n), cumulative additions
    interval_idx = bisect.bisect(prefix_sum_of_probabilities, random.random()) #time: O(logn) #similar to bisect.bisect_right, gives the right side of limit
    return values[interval_idx]


#variant
#dont understand this problem
#generate number based on exponent probability distribution
def nonuniform_random_number_generation_exponenent(N) -> int:
    data = numpy.random.exponential(5, size=N)
    return data
nonuniform_random_number_generation_exponenent(10)

@enable_executor_hook
def nonuniform_random_number_generation_wrapper(executor, values,
                                                probabilities):
    def nonuniform_random_number_generation_runner(executor, values,
                                                   probabilities):
        N = 10**6
        result = executor.run(lambda: [
            nonuniform_random_number_generation(values, probabilities)
            for _ in range(N)
        ])

        counts = collections.Counter(result)
        for v, p in zip(values, probabilities):
            if N * p < 50 or N * (1.0 - p) < 50:
                continue
            sigma = math.sqrt(N * p * (1.0 - p))
            if abs(float(counts[v]) - (p * N)) > 5 * sigma:
                return False
        return True

    run_func_with_retries(
        functools.partial(nonuniform_random_number_generation_runner, executor,
                          values, probabilities))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            '5-16-nonuniform_random_number.py', 'nonuniform_random_number.tsv',
            nonuniform_random_number_generation_wrapper))
