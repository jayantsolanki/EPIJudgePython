from typing import List

from test_framework import generic_test

"""
NOTE:
Since k sum problem have Time complexity: O(n^(k-1)), so sorting should be done for problem start with 3 sum and more.
Sorting not needed for 2 sum if using hashmaps. If already sorted then use sliding window technique

IF sorted then use sliding window, if unsorted then use hashmap
Leetcode: 15. 3Sum
https://leetcode.com/problems/3sum/
https://leetcode.com/problems/3sum-closest
https://leetcode.com/problems/3sum-smaller
https://leetcode.com/problems/4sum/ #use recursion to bring down the probme to 2sum

Three Sum problem
Design an algo that takes as input an Array and a number, and determines if there are three entries in the
array (not necessarily distinct position) which add up to the specified number.
Logic:
    First we sort the array    .
    We use two_sum method as a helper function. Idea is to lower the count to two needed element for two sum.
    We can do this by iterating over a loop and send t - A[i] to the two_sum function. Tada!!!
Time: O(n^2)
Space: O(1) 
"""

"""
Leetcode: 167. Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Leetcode: 1. Two Sum
https://leetcode.com/problems/two-sum/
Two sum:
Logic:
    We presume the array is sorted. 
    Maintain a subarray which is guaranteed to hold a solution if it exits. This subarray is initialized to the entire array, 
    and iteratively shrunk from one side or the other. Shrinking make sure sortedness of the array. If required sum is greater 
    than A[leftmost] + A[rightmost], then we increase the index of leftmost, since thats the only way we can increase the some.
    If required sum less than  A[leftmost] + A[rightmost] then we decease the index of rightmost index.
Time: O(n)
Space: O(1)
"""
def two_sum(A, t):
    i, j = 0, len(A) - 1

    while i <= j: #we can reuse the same element twice, hence  <=
        if A[i] + A[j] == t:
            return True
        elif A[i] + A[j] < t:
            i += 1
        else:
            j -= 1

# two_sum([-2, 1, 2, 4, 7, 11], 13)

def has_three_sum(A: List[int], t: int) -> bool:
    A.sort()
    for i in range(len(A)):
        if two_sum(A, t - A[i]):
            return True
    return False

# has_three_sum([11, 2, 5, 7, 3], 21)

#variant 1
"""
Solve the problem  when three elements must be distinct.
Example:  [5, 2, 3, 4, 3] and t = 9, aceeptable answ = [2, 3, 4] or [2, 4, 3]
Logic, change the <= to < and track for index match
"""
def two_sum_distinct(A, t, l):
    i, j = l + 1, len(A) - 1

    while i < j: 
        if A[i] + A[j] == t and i != l and j != l:
            return True
        elif A[i] + A[j] < t:
            i += 1
        else:
            j -= 1

# two_sum([-2, 1, 2, 4, 7, 11], 13)

def has_three_sum_distinct(A: List[int], t: int) -> bool:
    A.sort()
    for i in range(len(A)):
        if two_sum_distinct(A, t - A[i], i):
            return True
    return False
has_three_sum_distinct([11, 2, 5, 7, 3], 21)
has_three_sum_distinct([5, 2, 3, 4, 3], 9)

#another
def threeSum_1_distinct(nums: List[int]) -> List[List[int]]:
    target = 0
    def two_sum_distinct(A, t, l):
        i, j = l + 1, len(A) - 1 #start from l + 1

        while i < j: 
            if A[i] + A[j] == t:
                result.add(tuple(sorted([A[l], A[i], A[j]])))
                i +=1
                j -= 1
                # return True
            elif A[i] + A[j] < t:
                i += 1
            else:
                j -= 1

    nums.sort()
    result = set()
    for i in range(len(nums)):
        if nums[i] > 0:#since we have already sorted it, so no use to go further becasue rest fo those will be positive
            break
        two_sum_distinct(nums, target - nums[i], i)
    return result

#variant 2
"""
Leetcode: 18. 4Sum
https://leetcode.com/problems/4sum/
Logic:
    Just use backtrack, and to speed up, use 2-sum method for k == 2
Time: O(n^k - 1) or O(n^3) for 4-sum problem
Space: O(k)
"""
def kSum(nums: List[int], target: int, k) -> List[List[int]]:
    nums.sort()#important
    m = len(nums)
    count = k
    result = set()
    # @cache
    def twoSum(nums: List[int], target: int, curr) -> List[List[int]]:
        i, j = 0, len(nums) - 1 #start from l + 1

        while i < j: 
            if nums[i] + nums[j] > target# or ( j < len(nums) - 1 and nums[j + 1] == nums[j]):
                j -= 1  

            elif nums[i] + nums[j] < target# or ( i > 0 and nums[i - 1] == nums[i]):
                i += 1
            else:
                result.add(tuple(sorted(curr + [nums[i], nums[j]])))
                i += 1
                j -= 1
        return
    def backtrack(i, curr, S):
        # if S == target and len(curr) == count:
        #     result.add(tuple(sorted(curr)))
        #     return
        if  count - len(curr) == 2:
            twoSum(nums[i:], target - S, curr)
            return
        elif i == m:
            return
        else:

            for j in range(i, m):

                # if nums[j] >= 0 and target < 0 and S + nums[j] > target:
                #     break
                backtrack(j + 1, curr + [nums[j]], S + nums[j])
        return
    backtrack(0, [], 0)
    return result
kSum([1,0,-1,0,-2,2], 0, 4)

#variant 3
"""
Leetcode 16. 3Sum Closest
https://leetcode.com/problems/3sum-closest/
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is 
closest to target, abs(T - (A[p] + A[q] + A[r]) and A[p] <= A[q] <= A[r]). p, q and r should be distinct.
In the program i am returning SUM intead of array items, meaning is same
"""
#two pointer O(n^2) time
#cant use hash here, because we need to find the smallest diff
#we will track the smallest absolute difference between the sum and the target
def threeSumClosest(nums: List[int], target: int) -> int:
    closest_sum = float('Inf')
    min_diff = float('Inf')
    nums.sort()
    for l in range(len(nums)):
        i, j = l + 1, len(nums) - 1 #start from l + 1
        while i < j: 
            if min_diff > abs(target - (nums[i] + nums[j] + nums[l])):
                min_diff = abs(target - (nums[i] + nums[j] + nums[l]))
                closest_sum = nums[i] + nums[j] + nums[l]
                print(closest_sum, min_diff)
            if nums[i] + nums[j] + nums[l] > target:
                j -= 1
            elif  nums[i] + nums[j] + nums[l]< target:
                i += 1
            else:
                return  nums[i] + nums[j] + nums[l]
    return closest_sum    

#variant 4
"""
Leetcode: 259. 3Sum Smaller
https://leetcode.com/problems/3sum-smaller/
Write a proghram  that takes an array if integers A and and target T, and returns the numbers of 3-tuples
such that A[p] + A[q] + A[r] <= T and A[p] <= A[q] <= A[r].
"""
#sliding window problem
#you start scanning
def threeSumSmaller_slow(nums: List[int], target: int) -> int:
    nums.sort()
    count = 0
    print(nums)
    for l in range(len(nums)):
        # if nums[l] > target:
        #     break
        i, j = l + 1,  l + 2 #start from l + 1
        while i < j and j < len(nums): 
            while j < len(nums) and nums[i] + nums[j] + nums[l] < target:
                count += 1
                j = j + 1
            i = i + 1
            j = i + 1
    return count    
#optimized
#inspired from top
"""
    if nums[i] + nums[j] + nums[l] < target then
        nums[i] + nums[j-1] + nums[l] < target
        nums[i] + nums[j-2] + nums[l] < target
        nums[i] + nums[j-3] + nums[l] < target
        ....
        nums[i] + nums[i + 1] + nums[l] < target
        aka count += j - i
        Since array is sorted.Above is first batch of count, now we increament i = i + 1 and do the same process again
"""
def threeSumSmaller(nums: List[int], target: int) -> int:
    nums.sort()
    count = 0
    print(nums)
    for l in range(len(nums)):
        # if nums[l] > target:
        #     break
        i, j = l + 1,  len(nums) - 1 #start from l + 1
        while i < j: 
            if nums[i] + nums[j] + nums[l] < target:
                count += j - i#important
                i = i + 1
            else:
                j = j - 1
    return count

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('17-04-three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
