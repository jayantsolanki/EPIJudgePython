from operator import inv
from typing import List

from test_framework import generic_test

"""
Although, it is better to generate permutations in lexicographically sorted order using D.E. Knuth algorithm. 
Here elements are distinct
The next permutation of an array of integers is the next lexicographically greater permutation of its integer.

Write a program that takes input a permutation, and returns the next permutation under the dictionary ordering
If permutation is the last permutation then return the empty array
Define permutation p to appear before permutation q if in the first place where p and q differ in their array
representation, starting from index 0 the corresponding entry for p is less than that for q
Start from the right and look at the longest decreasing series. We cannot get the next permutation just by modifying this
series, since it is already at maximum.
We want to create the permutation just larger than the current one. Therefore, we need to replace the number at k with 
the number which is just larger than itself among the numbers lying to its right section.
Steps:
1 - find index k such that p[k] < p[k+1] and entries after index k appear in decreasing order (important)
2 - find the small p[l] in the decreasing entries which is greater tha p[k]
3 - swap p[k], p[l]
4 -  reverse the entries sequence after position k
time: O(n), space: O(1)
"""
def next_permutation(perm: List[int]) -> List[int]:

    # Find the first entry from the right that is smaller than the entry
    # immediately after it.
    inversion_point = len(perm) - 2
    while (inversion_point >= 0
           and perm[inversion_point] >= perm[inversion_point + 1]):
        inversion_point -= 1
    if inversion_point == -1:
        return []  # perm is the last permutation.
    
    # or this
    # inversion_point = len(perm) - 1
    # while (inversion_point >= 1
    #        and perm[inversion_point - 1] >= perm[inversion_point ]):
    #     inversion_point -= 1
    # if inversion_point == 0:
    #     return []  # perm is the last permutation.
    # inversion_point -= 1

    # Swap the smallest entry after index inversion_point that is greater than
    # perm[inversion_point]. Since entries in perm are decreasing after
    # inversion_point, if we search in reverse order, the first entry that is
    # greater than perm[inversion_point] is the entry to swap with.
    # for i in reversed(range(inversion_point + 1, len(perm))):
    for i in range(len(perm) -1, inversion_point, -1):
        if perm[i] > perm[inversion_point]:
            perm[inversion_point], perm[i] = perm[i], perm[inversion_point]
            break

    # Entries in perm must appear in decreasing order after inversion_point,
    # so we simply reverse these entries to get the smallest dictionary order.
    # perm[inversion_point + 1:] = reversed(perm[inversion_point + 1:])
    perm[inversion_point + 1:] = perm[inversion_point + 1:][:: -1]
    return perm


print(next_permutation([6,2,1,5,4,3,0]))
print(next_permutation([6,2,3,5,1,4,0]))
print(next_permutation([6,2,2,5,4,2,0]))
print(next_permutation([6,2,5,5,4,3,0]))


#variant1
'''
Leetcode 60. Permutation Sequence
https://leetcode.com/problems/permutation-sequence/
Compute the kth permutation under dictionary ordering, starting from the identity permutation; smallest in the permutation
that is the first permutation in dictionary ordering
Logic: I think I should repeatedly call previous function for kth times
'''

def kth_permute(A, n):
    if A == []:
        return []
    if n == 1:
        return A
    else:
        return kth_permute(next_permutation(A), n-1)


print(kth_permute([6, 2, 3, 0, 1, 4, 5], 2))
print(kth_permute([1, 2, 3], 5))


#variant2
"""


Given a permutation p, return the permutation corrsponding to the previous permutation of p
Logic: I think we just need to retrace the steps backward
"""
def reverse_permutation(perm):
    inversion_point = len(perm) - 2
    while (inversion_point >= 0 and perm[inversion_point] < perm[inversion_point + 1]):#finding first non decreasing
        inversion_point -= 1
    if inversion_point == -1:
        return []  # perm is the identity number. 

    for i in reversed(range(inversion_point + 1, len(perm))):
        if(perm[i] < perm[inversion_point]):#now find the number just smaller than the inversion one
            perm[i], perm[inversion_point] = perm[inversion_point], perm[i]
            break
    perm[inversion_point+1:] = reversed(perm[inversion_point+1:])
    return perm

print(reverse_permutation([3, 2, 1]))
print(reverse_permutation([6, 2, 3, 0, 1, 4, 5]))
print(reverse_permutation([6, 2, 3, 0, 1, 5, 4]))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('5-11-next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
