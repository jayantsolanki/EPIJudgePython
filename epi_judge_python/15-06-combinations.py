from typing import List

from test_framework import generic_test, test_utils


#leetcode 77. Combinations
# https://leetcode.com/problems/combinations/
"""
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n]
Time: O(KC^kn), where k is size of subset, n is total size available. It is binomial combo formula. the only consuming part here is to append the built combination of length k to the output, hence multiple by k
Explanation: let's say, K==N==3
output would be -->
1 -> 2 -> 3 and only 3 calls were made which is O(N) which is O(K nCk) -> 3 * 1 = 3

Space: O(KC^kn)
"""

def combinations_ori(n: int, k: int) -> List[List[int]]:
    def directed_combinations(offset, partial_combination):
        if len(partial_combination) == k:
            result.append(partial_combination.copy())
            return

        # Generate remaining combinations over {offset, ..., n - 1} of size
        # num_remaining.
        num_remaining = k - len(partial_combination)
        i = offset
        while i <= n and num_remaining <= n - i + 1:
            directed_combinations(i + 1, partial_combination + [i])
            i += 1

    result: List[List[int]] = []
    directed_combinations(1, [])
    return result


#my take, similar to powerset solution X123 , except here the length is the cap
def combinations(n: int, k: int) -> List[List[int]]:
    result = []
    # input_list = [i + 1 for i in range(n)]
    def backtrack(start, curr):
        if len(curr) == k:
            result.append(curr[:])
            return
        for i in range(start, n):
            # curr.append(input_list[i])
            curr.append(i + 1)#same as above, no need to generate array list
            backtrack(i+1, curr)
            curr.pop()
    curr = []
    backtrack(0, curr)
    return result


#variant 1:
# https://leetcode.com/problems/combination-sum/
# variant2
# https://leetcode.com/problems/combination-sum-iii/


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            '15-06-combinations.py',
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
