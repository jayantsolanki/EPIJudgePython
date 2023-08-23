from typing import List

from test_framework import generic_test

#time: O(n), space: O(n)
# Given a array A of n elements and a permutation P, apply P to A
#logic: keep on swapping untill p[i] = i. then move to next index in A, that is i + 1
def apply_permutation(perm: List[int], A: List[int]) -> None:
    for i in range(len(A)):
        while perm[i] != i:#if perm[i] == i, then it means that this is the actual place itself, no change or swapping needed
            A[perm[i]], A[i] = A[i], A[perm[i]] # swapping array elements
            perm[perm[i]], perm[i] = perm[i], perm[perm[i]] # swapping permutation array elements
    return

#variant 1 NOT WORKING
"""
As a a followup do this without using any changes in the perm array and no additional space
"""

def apply_permutation_v2(perm: List[int], A: List[int]) -> None:
    nextSwap = perm[0]
    for key, val in enumerate(perm):
        # nextSwap = perm[key]
        if(nextSwap!=key):
            A[nextSwap], A[key] = A[key], A[nextSwap] # swapping array elements 
            nextSwap = perm[nextSwap]
        
    print(A)
    return
apply_permutation_v2([2,0,1,3], ['a', 'b', 'c', 'd'])
apply_permutation_v2([2,0,3,1], ['a', 'b', 'c', 'd'])



"""
Inverse of permutation: This represents the orignal order of the array when this inverse permutation is applied
['a','b','c','d','e'], permute [1,0,3,4,2] to ['b','a','e','c','d']
Its inverse is [1,0,4,2,3]
Given permutation is: 591826473 To get the inverse of this first write down the position of 1 It is in the 3rd position . SO inverse starts as "3 ...". Next locate 2 in the permutation. It is in the 5th position. So inverse expands to "35...." Similarly go on chasing 3,4 etc and note down their positions and build the inverse permutation.
https://math.stackexchange.com/questions/2999320/how-can-i-find-the-inverse-of-a-permutation
0 is at 1, 1 is at 0, 2 is at 4, 3 is at 2, 4 is at 3, hence [1, 0, 4, 2, 3]
So if you appliy the inverse permutation array on giuven permutation, you well get array in original order
Original_order_array = [A[i] for i in inverse_perm_result]. Dont try to apply code from book
"""
def find_inverse_permutation(A) -> None:
    pos = {}#its a dictionary
    for key, val in enumerate(A):#first get the positions
        pos[val] = key
    A.sort()
    for key, val in enumerate(A):
        print(pos[val])
    return

find_inverse_permutation([1,0,3,4,2])
find_inverse_permutation([2, 3, 4, 5, 1])


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('5-10-apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
