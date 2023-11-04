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
Logic: Basically we use hash map to mimic swapping feature of program 5.12
you can use offline random sampling, but this could be O(n) for both time and space, since the original array needs to be generated first
in order to reduce it to the O(k)  
basically in below code we map index to randnumber and randnumber to index, both being keys of an array of size n
if randnumber is repeated during a new index then it will be pointed to that new index, and the older index it pointed to , that will point by new index
since index is increasing in the loop, there will be no repetition
"""

def random_subset_original(n: int, k: int) -> List[int]: 
    #below program similar to 5.12, where we need to exchange the elements. Since we dont know the elements early, we use hashmap
    changed_elements: Dict[int, int] = {}#used for tracking the swapped values
    for i in range(k):#no need to create an array, unlike in problem 5.12
        # Generate a random index between i and n - 1, inclusive.
        rand_idx = random.randrange(i, n)
        #now try to get the index which has been mapped to this random number previously, in case if it is repeated
        rand_idx_mapped = changed_elements.get(rand_idx, rand_idx)#second parameter is default value, in case index doesnt exist
        #now see if curernt index is mapped or not, return the value of random number if mapped
        i_mapped = changed_elements.get(i, i)# initially A[i] = i, these are untouched ones
        changed_elements[rand_idx] = i_mapped # this makes sure if the number is repeated it wont get stored again
        changed_elements[i] = rand_idx_mapped #map to whatever rand_ids was previously mapped
    return [changed_elements[i] for i in range(k)]

def random_subset(n: int, k: int) -> List[int]: 
    #below program similar to 5.12, where we need to exchange the elements. Since we dont know the elements early, we use hashmap
    changed_elements: Dict[int, int] = {}#used for tracking the swapped values
    for i in range(k):#no need to create an array, unlike in problem 5.12
        # Generate a random index between i and n - 1, inclusive.
        rand_idx = random.randrange(i, n)
        #now try to get the index which has been mapped to this random number previously, in case if it is repeated
        # rand_idx_mapped = changed_elements.get(rand_idx, rand_idx)#second parameter is default value, in case index doesnt exist
        #now see if curernt index is mapped or not, return the value of random number if mapped
        # i_mapped = changed_elements.get(i, i)# initially A[i] = i, these are untouched ones
        # changed_elements[rand_idx] = i_mapped # this makes sure if the number is repeated it wont get stored again
        # changed_elements[i] = rand_idx_mapped #map to whatever rand_ids was previously mapped

        #below is similar to A[i], A[r] = A[r], A[i] in program 5.12, 
        changed_elements[i], changed_elements[rand_idx] = changed_elements.get(rand_idx, rand_idx), changed_elements.get(i, i)
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
