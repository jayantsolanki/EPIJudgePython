from typing import List

from test_framework import generic_test, test_utils

"""
Leetcode: 22. Generate Parentheses, https://leetcode.com/problems/generate-parentheses/
"""

def generate_balanced_parentheses_ori(num_pairs: int) -> List[str]:
    def directed_generate_balanced_parentheses(num_left_parens_needed,
                                               num_right_parens_needed,
                                               valid_prefix,
                                               result=[]):
        if num_left_parens_needed > 0:  # Able to insert '('.
            directed_generate_balanced_parentheses(num_left_parens_needed - 1,
                                                   num_right_parens_needed,
                                                   valid_prefix + '(')
        if num_left_parens_needed < num_right_parens_needed:
            # Able to insert ')'.
            directed_generate_balanced_parentheses(num_left_parens_needed,
                                                   num_right_parens_needed - 1,
                                                   valid_prefix + ')')
        if not num_right_parens_needed:
            result.append(valid_prefix)
        return result

    return directed_generate_balanced_parentheses(num_pairs,
                                                  num_pairs,
                                                  valid_prefix='')

#############my take###################
"""
Idea is simple, you generate combination just like for subsets problem, key is to prune wrong branches and
make sure you are not going above the n parenthesis, that is for n, there will be n open parenthesis and n closed parenthesis
Time:
    The recursion tree in this problem is a binary tree where vertices represent incomplete sequences of brackets and edges represent the choice of the next bracket (either left or the right). The height of the tree is 2n, since we must branch once per bracket. So the number of vertices is at most 2^2n and the number of leaves is at most half the number of vertices of a perfect tree, so asymptotically O(2^2n). Additionally we do linear work per leaf to copy the sequence to output.

    A more complete analysis would take into account that some bracket choices are invalid, which leads to asymptotically fewer leaves in the tree. However since we are interested in upper bounds, it's still correct to say that time complexity is O(n*(2^2n)), even though it's not the most accurate upper bound.
"""
def generate_balanced_parentheses_(n):
    mapping = {1: '(', -1: ')'}
    mapping_count = {'(': 0, ')': 0}
    result = []
    def backtrack(curr, total):
        # print(curr)
        if len(curr) == n * 2 and total == 0:#total will be zero for a balanced parenthesis group, and you need total 2n parenthesis
            result.append("".join(curr))
            return
        for key, value in mapping.items():
            if total + key < 0 or total + key > n:#pruning non needed branches, 
                continue
            if mapping_count[value] > n: #pruning non needed branches, makin sure you dont cross n limit per parenthesis
                continue
            mapping_count[value] += 1
            curr.append(value)
            backtrack(curr, total + key)
            curr.pop()
            mapping_count[value] -= 1
    curr = []
    backtrack(curr, 0)
    return result

def generate_balanced_parentheses(n):#slight change in the way string generated, saves time
    mapping = {1: '(', -1: ')'}
    mapping_count = {'(': 0, ')': 0}
    result = []
    def backtrack(curr, total):
        if len(curr) == n * 2 and total == 0:#total will be zero for a balanced parenthesis group, and you need total 2n parenthesis
            result.append("".join(curr))
            return
        for key, value in mapping.items():
            if total + key < 0 or total + key > n:#pruning unneeded branches, 
                continue
            if mapping_count[value] > n: #pruning unneeded branches, makin sure you dont cross n limit per parenthesis
                continue
            mapping_count[value] += 1
            backtrack(curr + value, total + key)
            mapping_count[value] -= 1
    backtrack("", 0)
    return result
# generateParenthesis
# generateParenthesis(3)

def generate_balanced_parentheses_pythonic(num_pairs, num_left_open=0):
    if not num_pairs:
        return [')' * num_left_open]
    if not num_left_open:
        return [
            '(' + p for p in generate_balanced_parentheses_pythonic(
                num_pairs - 1, num_left_open + 1)
        ]
    else:
        return ([
            '(' + p for p in generate_balanced_parentheses_pythonic(
                num_pairs - 1, num_left_open + 1)
        ] + [
            ')' + p for p in generate_balanced_parentheses_pythonic(
                num_pairs - 1, num_left_open - 1)
        ])




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('15-07-enumerate_balanced_parentheses.py',
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))

#using DFS
def generateParenthesis(n) -> List[str]:
    ans = []
    def backtrack(S = [], left = 0, right = 0):
        if len(S) == 2 * n:
            ans.append("".join(S))
            return
        if left < n:
            S.append("(")
            backtrack(S, left+1, right)
            S.pop()
        if right < left:#important
            S.append(")")
            backtrack(S, left, right+1)
            S.pop()
    backtrack()
    return ans

generateParenthesis(3) #['((()))', '(()())', '(())()', '()(())', '()()()']