import functools
import random
import math

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    check_sequence_is_uniformly_random, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook


def zero_one_random():
    # return random.randrange(2)#returns 0 or 1
    # return random.choice([0,1])#returns 0 or 1
    return random.randint(0,1)


def uniform_random(lower_bound: int, upper_bound: int) -> int:
    # TODO - you fill in here.
    number_of_outcomes = upper_bound - lower_bound #this also works
    # number_of_outcomes = upper_bound - lower_bound + 1
    iter = math.floor(math.log(number_of_outcomes, 2))+1 #iter gives the size of binary digits to get those outcomes
    while True:
        result = 0
        for i in range(iter):#construct a number which is three bits size
            result  = (result << 1)| zero_one_random()#absorb 0 or 1 from right side and at the same time push existing 0 or 1 towards left
        # if result < number_of_outcomes:#if not then try again
        if result <= number_of_outcomes:#if not then try again, this also works
            break
        # if (lower_bound <= lower_bound + result <= upper_bound):
        #     break
    return result+lower_bound


@enable_executor_hook
def uniform_random_wrapper(executor, lower_bound, upper_bound):
    def uniform_random_runner(executor, lower_bound, upper_bound):
        result = executor.run(
            lambda:
            [uniform_random(lower_bound, upper_bound) for _ in range(100000)])

        return check_sequence_is_uniformly_random(
            [a - lower_bound for a in result], upper_bound - lower_bound + 1,
            0.01)

    run_func_with_retries(
        functools.partial(uniform_random_runner, executor, lower_bound,
                          upper_bound))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('4-10-uniform_random_number.py',
                                       'uniform_random_number.tsv',
                                       uniform_random_wrapper))
