import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))

"""
Leetcode 518. Coin Change 2
https://leetcode.com/problems/coin-change-2/

Knapsack problem
Write a program for the knapsack problem that seldcts a subset of items that has maximum value ans satisfies the weight
constraint. All items have integer weights and values. Return the value of the subset
Note: Each Item can be taken only once (bounded knapsack)
Logic:
    Similar to coin chain problem II in leetcode, but here each item can be taken once. unlike coin change 
    So the decision goes like this, either we take the weight and value and move one by adding its value or we bypass it
Time and Space: O(weight X number of items) aka O(wn)
"""
#my take, topdown
def optimum_subject_to_capacity_mem(items: List[Item], capacity: int) -> int:
    m = len(items)
    @functools.cache
    def dp(cap, index):

        if cap == 0:
            return 0
        elif index == m:
            return 0
        else:
            if cap >= items[index].weight:#important
                return max(dp(cap - items[index].weight, index + 1) + items[index].value, dp(cap, index + 1))#here we either include that or not include that
            else:
                return dp(cap, index + 1)
    return dp(capacity, 0)

def optimum_subject_to_capacity_ori(items: List[Item], capacity: int) -> int:

    # Returns the optimum value when we choose from items[:k + 1] and have a
    # capacity of available_capacity.
    @functools.lru_cache(None)
    def optimum_subject_to_item_and_capacity(k, available_capacity):
        if k < 0:
            # No items can be chosen.
            return 0

        without_curr_item = optimum_subject_to_item_and_capacity(
            k - 1, available_capacity)
        with_curr_item = (0 if available_capacity < items[k].weight else
                          (items[k].value +
                           optimum_subject_to_item_and_capacity(
                               k - 1, available_capacity - items[k].weight)))
        return max(without_curr_item, with_curr_item)

    return optimum_subject_to_item_and_capacity(len(items) - 1, capacity)

#dont recomment, use above solutions
#bottom up solution, inspired from bottom up solution of coin change ii  problem,. just one difference, each row has unique item, that can be used 
#only once, hence we use i - 1 at line 72
def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    m = len(items)
    cache = [[0] * (capacity + 1) for _ in range(m)]
    #base cases:
    for weight in range(capacity + 1):
        if items[0].weight <= weight:
            cache[0][weight] = items[0].value
        else:
            cache[0][weight] = 0
    #subtracted to zero
    for i in range(1, m):
        # for weight in range(1, capacity + 1):
        for weight in range(capacity, -1, -1): # use this instead of above
            if items[i].weight <= weight: #take the weight, remember, we cannot use the item again, hence i - 1 in both
                    cache[i][weight] = max(cache[i - 1][weight], cache[i - 1][weight - items[i].weight] + items[i].value)
            else:#that weight cannot be taken
                    cache[i][weight] = cache[i - 1][weight]

    return cache[-1][-1]

#variant 1
"""
Solve above problem in O(w) space constraint
Logic:
    Since we are only using the previous cell ( i - 1) all the time, hence we  can just keep on updating the same row

    Note cache[weight - item.weight] might be overridden if 'item.weight > 0'. Therefore we can't use this value for the current 
    iteration.To solve it, we can change our inner loop to process in the reverse direction. This will ensure that whenever we 
    change a value in cache[], we will not need it anymore in the current iteration. Hence value wont be adding up
"""
def optimum_subject_to_capacity_(items: List[Item], capacity: int) -> int:
    # m = len(items)
    cache = [0] * (capacity + 1)

    for item in items:
        for weight in range(capacity, -1, -1): # we should move in reverse, see explanation above
            if item.weight <= weight: #take the weight, 
                cache[weight] = max(cache[weight], cache[weight - item.weight] + item.value)

    return cache[-1]

#variant 2
"""
My logic, find the minimum weight, divide the given weight w by that min weight, that will give you the lower limit of C,
now to find the upper limit, take the C mod min(weights), and try to find that if remainder weight can be created or not
"""

#variant 3
"""
Fractional Knapsack problem
Use greedy approach
Logic:
    The basic idea of the greedy approach is to calculate the ratio value/weight for each item and sort the item on 
    basis of this ratio. Then take the item with the highest ratio and add them until we can't add the next item 
    as a whole and at the end add the next item as much as we can. Which will always be the optimal solution to this problem.
Time complexity: O(n log n) 
"""
from typing import List
def fractional_knapsack(items: List[Item], capacity: int):
    fractionVal = []
    for key, item in enumerate(items):
        fractionVal.append((item.value//item.weight, key))
    # fractionVal.sort(reverse = True)
    #or use this
    fractionVal.sort(reverse = True, key = lambda val: val[0])
    TotalVal = 0
    for item in fractionVal:#remember, you can add each item only once
        if capacity >= items[item[1]].weight: #accessing weight by index
            TotalVal += items[item[1]].value
            capacity -= items[item[1]].weight
        else:
            #find fractional portion needed, this two lines or next one, either of them
            # fractional_portion = capacity/items[item[1]].weight
            # fractional_value = int(fractional_portion * items[item[1]].value)
            fractional_value = int(capacity * item[0])
            TotalVal += fractional_value
            break
    return TotalVal


fractional_knapsack([Item(10, 60), Item(40, 40), Item(20, 100), Item(30, 120)], 50)

#variant 4
"""
Divide the spoils fairly
Similar to 1755. Closest Subsequence Sum
https://leetcode.com/problems/closest-subsequence-sum/
    #check https://www.geeksforgeeks.org/meet-in-the-middle/
    # O(n2^(n/2))
"""
def minAbsDifference(nums: List[int]) -> int:
    goal = sum(nums) // 2
    m = len(nums)
    result = set()
    #Finds all possible subset sums of integers in set half of the nums
    def dp(arr, i, total):#generates
        if i == len(arr):
            # print(total)
            result.add(total)
            return
        else:
            dp(arr, i + 1, total + arr[i])
            dp(arr, i + 1, total)
            
    dp(nums[:m//2], 0, 0)#first half
    sum1 = result.copy()
    result = set()
    dp(nums[m//2: ], 0, 0)#second half
    sum2 = result.copy()
    sum2 = sorted(sum2)
    ans = float('Inf')
    # for each possible sum of the 1st half, find the sum in the 2nd half
    # that gives a value closest to the goal using binary search
    group_1 = 0
    group_2 = 0
    for item in sum1:
        index = bisect.bisect_left(sum2, goal - item)
        if index < len(sum2):
            ans = min(ans, abs(goal - (item + sum2[index]))) #goal - s1 - s2, s2 here is sum2[index]
            # group_1, group_2 = item, sum2[index]
            group_1, group_2 = item + sum2[index], sum(nums) - (item + sum2[index])
        if 0 < index:
            ans = min(ans, abs(goal - (item + sum2[index - 1])))
            # group_1, group_2 = item, sum2[index - 1]
            group_1, group_2 = item + sum2[index - 1], sum(nums) - (item + sum2[index - 1])
            #sum2[index] is the smallest number in sum2 that's larger than or equal to remain(goal - item) and sum2[index-1] 
            #is the largest number in sum2 that's smaller than remain. In order to find the 
            #smallest absolute difference we need to consider both numbers (if they exist).

            #resultant sum could be larger than goal or less than goal, first if condition meb find both larger or msaller
            #second if coniditon will find smaller. We take the min abs of both
    return (group_1, group_2)

#variant 5
"""
Divide spoils fairly, with additional constraint that thieves have same number of items
2035. Partition Array Into Two Arrays to Minimize Sum Difference
https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/
"""
import bisect
def minimumDifference(nums: List[int]) -> int:
    goal = sum(nums) // 2
    m = len(nums)
    result = set()
    def dp(arr, i, total, count):#generates
        if i == len(arr):
            # print(total)
            if count == m // 2:#only storing those sum which has elements of size n
                result.add(total)
            return
        else:
            dp(arr, i + 1, total + arr[i], count + 1)
            dp(arr, i + 1, total, count)
            
    #now try to find the sum which is closer to the goal
    closest_sum = float('Inf')
    dp(nums, 0, 0, 0)
    result = sorted(result)
    print(result)
    
    index = bisect.bisect_left(result, goal)
    
    if index < len(result):
        if abs(result[index]  - goal) < abs(closest_sum - goal):
            closest_sum = result[index] 
    if index > 0:
        if abs(result[index - 1]  - goal) < abs(closest_sum - goal):
            closest_sum = result[index - 1] 

    return abs( sum(nums) - 2* closest_sum)

# variant 6
"""
416. Partition Equal Subset Sum
https://leetcode.com/problems/partition-equal-subset-sum/
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal
"""
def canPartition_mem1(nums: List[int]) -> bool:
    totalSum = sum(nums)
    if totalSum % 2 == 1:
        return False
    nums.sort(reverse = True)# we can iterate from large to small values to prune our DFS
    # @lru_cache(maxsize=None)
    @functools.cache
    def dp(i, S):
        if S == 0:
            return True
        elif i == len(nums):
            return False
        else:
            #needs some pruning, this one is uselss and time consuming
            if S - nums[i] < 0:
                return dp(i + 1, S)
            else:
                return dp(i + 1, S - nums[i]) or dp(i + 1, S) #use or not these |
            # if S >= nums[i]:
            #     return dp(i + 1, S - nums[i]) or dp(i + 1, S)
            # else:
            #     return dp(i + 1, S)
        
    return dp(0, totalSum // 2)
#custom cache, better
def canPartition(nums: List[int]) -> bool:
    totalSum = sum(nums)
    if totalSum % 2 == 1:
        return False
    nums.sort(reverse = True)# we can iterate from large to small values to prune our DFS
    # @lru_cache(maxsize=None)
    cache = {}
    def dp(i, S):
        if S == 0:
            return True
        elif i == len(nums):
            return False
        elif S not in cache:
            #needs some pruning, this one is uselss and time consuming
            if S - nums[i] < 0:
                cache[S] =  dp(i + 1, S)
            else:
                cache[S] =  dp(i + 1, S - nums[i]) or dp(i + 1, S) #use or not these |
            # if S >= nums[i]:
            #     return dp(i + 1, S - nums[i]) or dp(i + 1, S)
            # else:
            #     return dp(i + 1, S)
        return cache[S]
        
    return dp(0, totalSum // 2)
#dp solution
def canPartition_iter1(nums: List[int]) -> bool:
    totalSum = sum(nums)
    if totalSum % 2 == 1:#odd sums cant have even partition
        return False
    needed_sum = totalSum // 2
    cache = [[False] * (needed_sum + 1) for _ in range(len(nums))]
    
    for i in range(len(nums)):
        # for j in range(needed_sum + 1):
        for j in range(needed_sum, -1, -1):#this or above
            if i ==0 and j ==0: #important because cache[0][0] needs to be true, that is sums can be reached 0
                cache[i][j] = True
                continue
            if j >= nums[i]:
                cache[i][j] = cache[i - 1][j] | cache[i - 1][j - nums[i]]
            else:
                cache[i][j] = cache[i - 1][j]
    return cache[-1][-1]# == needed_sum


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('16-06-knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
