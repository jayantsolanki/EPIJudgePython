from typing import List

from test_framework import generic_test, test_utils

"""
Write a program which takes as input an array of distinct integers and generates all permutations of that array. 
No permutation of the array may appear more that once.
Logic:
    Start by A[0] element, then recurse on A[1:] and so on, the trick is once the A[i] element is selected, swap it
    so that it wont come again in further recrsion of A[i+1:]
    Computing all permutations beginiing  with A[0] entails computing all permutations of A[1, n-1], which suggests
    the use of recursion. To compute all permutations beginning with A[1] we swap A[0] with A[1] and copute all permutations
    of the updated A[1, n-1]. We then restore the originla state before embarking on computing all permutation beginning A[2].

    More simple reasoning for swapping: Let A = [7, 3, 5], when we need to fill position 0, we can pick 7 or 3 or 5. If we pick 
    7, whose index is 0, we then move to number rest of set availble to pick for position 1, in thos 7 wont be encounted again since 0 < 1,2. Now,  when 3 is selected for position 0, and then we move to position 1, we need to swap it before we move to position 2,
    because 3 will be encounted again, since its index is 1. Hence we recursing we always swap value at current fill position with
    value at index decided by for loop. But once we return from recursio and move to next index decided by for loop, we need to restore the swap. Overall if A is 3 length, then position at 0 will be swapped 3 times, position at 1 will be swapped 2 times and so on.
Time: C(n) = 1 + nC(n-1) for n >= 1, with C(0) = 1. Expanding C(n) = 1 + n + n(n-1) + n(n-1)(n-2) + factorial(n) = O(nfactorial(n))
Rational= factorial(n) items genreated and we spent O(n) time to store each one
Space = O(nfactorial(n))
"""
def permutations_ori(A: List[int]) -> List[List[int]]:
    def directed_permutations(i):
        if i == len(A) - 1:
            result.append(A.copy()) #this takes O(n)
            return

        # Try every possibility for A[i].
        for j in range(i, len(A)): #this takes O(factorial(n))
            A[i], A[j] = A[j], A[i]#swapping is important, because we dont want the same number to be encountered
            # Generate all permutations for A[i + 1:].
            directed_permutations(i + 1)
            A[i], A[j] = A[j], A[i]

    result: List[List[int]] = []
    directed_permutations(0)
    return result

def permutations(A: List[int]) -> List[List[int]]:
    def gen_permutation(i):
        if i == len(A) - 1:
            temp[i] = A[i]
            result.append(temp.copy())  #this takes O(n)
            return
        for index in range(i, len(A)): #this takes O(factorial(n))
            # print(index)
            temp[i] = A[index]
            A[i], A[index] = A[index], A[i]#swapping is important, because we dont want the same number to be encountered
            gen_permutation(i + 1)
            A[i], A[index] = A[index], A[i]#restore the number back to its original place, so that further recursion bracnh 
            #will not be impacted
            # Think of it as moving back up in the tree to explore the next branch. When we moved down of one level, we swapped 2 elements (1st swap in the code). So when we go back up in the tree we need to swap these 2 elements back to their original order at the parent node level (2nd swap in the code). This is called backtracking = done exploring a branch, let's go back up and explore more branches.
    
    result: List[List[int]] = []
    temp = [None] *len(A)
    gen_permutation(0)
    return result

permutations([1, 2, 3])

#variant 1
"""
Generate permutations when repeat numbers present
Logic:
    Using Array permutation example from page 57, 5.11, a bit modified to include duplicates
"""
def nextPermutation(nums: List[int]):
    """
    Do not return anything, modify nums in-place instead.
    """
    inversion_point = len(nums) - 2
    
    while(inversion_point >= 0 and nums[inversion_point] >= nums[inversion_point + 1]):#for non distinct add the equality sign
        inversion_point -= 1
    if inversion_point == -1:
        # return nums[::-1]#return ascending order if not found
        # print("Reverse", list(reversed(nums)))
        return list(reversed(nums))
        # return []
    

    for i in range(len(nums) -1, inversion_point, -1):
        if nums[i] > nums[inversion_point]:
            nums[inversion_point], nums[i] = nums[i], nums[inversion_point]
            break
    #now sort the suffix in ascending order
    nums[inversion_point+1:] = reversed(nums[inversion_point+1:])
    return nums
def permuteUnique(nums: List[int]) -> List[List[int]]:
    if not nums:
        return []
    result = []
    A = nums[:]
    while True:
        result.append(A[:])
        A = nextPermutation(A)
        if A[:] == nums[:]:
        # if not A:
            break
    return result

permuteUnique([1,2,3])
permuteUnique([1,2,3, 1])

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('15-04-permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
