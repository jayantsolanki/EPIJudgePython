from functools import cache
from typing import List
import bisect

from test_framework import generic_test

"""
Leetcode: 300. Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/
There is also a nlogn solution using Binary Search
Find the longest nondecreasing subsequence #note it is not strictly decreasing unlike in leetcode
Write a program that takes as input an array of numbers and returns the length of a longest nondecreasing 
subsequence in the array.

A subsequence is a sequence that can be derived from an array by deleting some or no elements 
without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of 
the array [0,3,1,6,2,2,7]

Logic:
    Express the longest nondecreasing subsequence ending at an entry in terms of the longest nondecreasing
    subsequence appearing in the subarray consisting of preceding elements.
Time: O(n^2)
Space: O(n)
"""
#my take, top_down, a bit poor to O(n^2), TLE in leetcode
#here we use the j index to track the value we need to compare with, if lesser value found we switch the j, , also we dont switch
#the j for other dp recursion
def longest_nondecreasing_subsequence_length_slowmem(nums: List[int]) -> int:
    m = len(nums)
    maxglobal = 0
    @cache
    def dp(i, j):
        if i == 0:
            return 1
        else:
            ans = 0#note this
            if nums[j] >= nums[i - 1] : #not strictly decreasing
                ans =  dp(i - 1, i - 1) + 1
            ans = max(dp(i - 1, j), ans)
            return ans
    for i in range(m - 1, -1 , -1):#have to try for every position and return the one which is max
        maxglobal = max(dp(i, i), maxglobal)
    return maxglobal
#here we use the basic backtracking, and find longest subsequence found at a specific index i, , in the end we run for loop to return the max among them
def longest_nondecreasing_subsequence_length_mem2(nums: List[int]) -> int:
    m = len(nums)
    maxglobal = 0
    @cache
    def dp(i):
        if i == m-1:#if we reached here, that means this move was legal, hence return 1
            return 1
        else:
            maxVal = 1#note this
            for j in range(i + 1, m):
                if nums[i] <= nums[j]:
                    maxVal =  max(maxVal, dp(j) + 1)
                    
            return maxVal

    for i in range(m):#have to try for every position and return the one which is max
        maxglobal = max(dp(i), maxglobal)
    return maxglobal

#bottom up, my favorite, mentally run the forloop in your mind for this example, 
# [1,3,6,7,9,4,10,5,6]
"""
Logic:
    Let's say we know dp[0], dp[1], and dp[2]. How can we find dp[3] given this information? Well, since dp[2] represents 
    the length of the longest increasing subsequence that ends with nums[2], if nums[3] > nums[2], then we can simply take 
    the subsequence ending at i = 2 and append nums[3] to it, increasing the length by 1. The same can be said for nums[0] 
    and nums[1] if nums[3] is larger. Of course, we should try to maximize dp[3], so we need to check all 3. Formally, 
    the recurrence relation is: dp[i] = max(dp[j] + 1) for all j where nums[j] < nums[i] and j < i.
"""
def longest_nondecreasing_subsequence_length(nums: List[int]) -> int:
    m = len(nums)
    #let's say that cache[i] represents the length of the longest increasing subsequence that ends with the ith element
    #notice it says 'ends', hence we need to find the longest uptil that value at index i
    cache = [1] * m
    maxVal = 0
    for i in range(m):#important, logic since in below forloop you need to refer to previous calculated
        # cache values
        for j in range(i):#start checking for values before nums[i]
            if nums[j] <= nums[i]:#this checks if the value before the index i is lesser than add one to the calculation
                cache[i] = max(cache[j] + 1, cache[i])#cache[i] repeatedly gets updated, this is the recurrence state
        maxVal = max(cache[i], maxVal)
    #cache contains length of longest subsequences for each value starting at index i
    return maxVal

#important, nlogn
#idea here is that longest increasing subsequence will be naturally ordered (sorted in ascending order)
#so let an array store this sorted orderd. For any incoming number, it will either sit in the end or in mid somewhere, so idea
# here is to find the its position using bisect_left, and place it there.
# https://leetcode.com/problems/longest-increasing-subsequence/discuss/1326308
def lengthOfLIS_binary(nums: List[int]) -> int:
    sub = []
    for num in nums:
        i = bisect_left(sub, num)

        # If num is greater than any element in sub
        if i == len(sub):
            sub.append(num)
        
        # Otherwise, replace the first element in sub greater than or equal to num
        else:
            sub[i] = num
    
    return len(sub)

#variant 1
"""
Write a program that takes as input an array of numbers and returns a longest nondecreasing subsequence in the array
Just check if cache[i] is greater then maxVal, then append the number at index i into result array
"""
def longest_nondecreasing_subsequence_length_seq(nums: List[int]) -> int:
    m = len(nums)
    #let's say that cache[i] represents the length of the longest increasing subsequence that ends with the ith element
    #notice it says 'ends', hence we need to find the longest uptil that value at index i
    cache = [1] * m
    result = []
    maxVal = 0
    for i in range(m):#important, logic since in below forloop you need to refer to previous calculated
        # cache values
        for j in range(i):#start checking for values before nums[i]
            if nums[j] <= nums[i]:#this checks if the value before the index i is lesser than add one to the calculation
                cache[i] = max(cache[j] + 1, cache[i])#cache[i] repeatedly gets updated, this is the recurrence state
        if maxVal < cache[i]:
            maxVal = cache[i]
            result.append(nums[i])
        # maxVal = max(cache[i], maxVal)
    #cache contains length of longest subsequences for each value starting at index i
    # #generating the sequence:
    print(cache)
    print(result)
    # 

    return maxVal

longest_nondecreasing_subsequence_length_seq([1,3,6,7,9,4,10,5,6])

#variant 2, 3, 4, 5 left out


#variant 6 Important
"""
Similar 845. Longest Mountain in Array https://leetcode.com/problems/longest-mountain-in-array/
Define a sequence of points in the plane to be ascending if each point is above and to the right of previous point.
Find max number of ascending points subset.
Logic
    The idea: Just simulate the process of climbing the mountains. One first walk up, then after reaching peaks, 
    one continues walking down until the valley. Then calculate the length that he/she has walked so far and 
    start another climbing. Repeat the process and we get the answer.
"""
def longest_ascend(A: List[int]) -> int:
        i = ans = 0
        real_base = 0
        real_peak = 0
        while i < len(A):
            base = i
            # walk up
            while i + 1 < len(A) and A[i] < A[i+1]:
                i += 1

            # check if peak is valid
            if i == base: 
                i += 1
                continue
            # update answer
            if i - base + 1 > ans:
                real_base = base
                real_peak = i
                ans = i - base + 1
            # ans = max(ans, i - base + 1)
        print(A[real_base: real_peak + 1])
        return ans
longest_ascend([2,1,4,7,3,2,5])

#variant 7: Important
"""
Solve longest subsequence in O(nlogn)
Leetcode: 300. Longest Increasing Subsequence
TLDR:
For those wondering why BS works, here's a rundown for ya:
Basically we keep extending the sequence long as we keep finding increasing elements. Soon as we find a smaller 
element, we replace it, emphasis on the word REPLACE . Replacing doesnt change the length, meaning that our longest 
length is kept intact, but the order of the elements get changed. Hence, we get the correct length, but not to correct LIS.
So, we increase our chances of getting increased length, by making sure to replace the last element in subsequence with a 
lesser element, that way we can still keep on growing the subsequence, because after removal of last element(which was greatest
encountered so far) with a lesser element, we increased the magnitude of allowed elements.

https://leetcode.com/problems/longest-increasing-subsequence/ Solution 3
Refer to this https://leetcode.com/problems/longest-increasing-subsequence/discuss/1326308/C%2B%2BPython-DP-Binary-Search-BIT-Solutions-Picture-explain-O(NlogN)

It appears the best way to build an increasing subsequence is: for each element num, if num is greater than 
the largest element in our subsequence, then add it to the subsequence. Otherwise, perform a linear scan 
through the subsequence starting from the smallest element and replace the first element that is greater 
than or equal to num with num. This opens the door for elements that are greater than num but less than 
the element replaced to be included in the sequence. (Important)

One thing to add: this algorithm does not always generate a valid subsequence of the input, but the length 
of the subsequence will always equal the length of the longest increasing subsequence. For example, with the 
input [3, 4, 5, 1], at the end we will have sub = [1, 4, 5], which isn't a subsequence, but the length is 
still correct. The length remains correct because the length only changes when a new element is larger than 
any element in the subsequence. In that case, the element is appended to the subsequence instead of replacing 
an existing element.

Here we did binary search to reduce the n to logn
"""
def lengthOfLIS(nums: List[int]) -> int:
    sub = []
    for num in nums:
        i = bisect.bisect_left(sub, num)

        # If num is greater than any element in sub
        if i == len(sub):
            sub.append(num)
        
        # Otherwise, replace the first element in sub greater than or equal to num
        else:
            sub[i] = num
    
    return len(sub)
lengthOfLIS([2,1,4,7,3,2,8])

def pathOfLIS(nums: List[int]):
    sub = []
    subIndex = []  # Store index instead of value for tracing path purpose
    path = [-1] * len(nums)  # path[i] point to the index of previous number in LIS
    for i, x in enumerate(nums):
        if len(sub) == 0 or sub[-1] < x:
            path[i] = -1 if len(subIndex) == 0 else subIndex[-1]
            sub.append(x)
            subIndex.append(i)
        else:
            idx = bisect.bisect_left(sub, x)  # Find the index of the smallest number >= x, replace that number with x
            path[i] = -1 if idx == 0 else subIndex[idx - 1]
            sub[idx] = x
            subIndex[idx] = i

    ans = []
    t = subIndex[-1]
    while t >= 0:
        ans.append(nums[t])
        t = path[t]
    return ans[::-1]
pathOfLIS([2,1,4,7,3,2,8])

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            '16-12-longest_nondecreasing_subsequence.py',
            'longest_nondecreasing_subsequence.tsv',
            longest_nondecreasing_subsequence_length))
