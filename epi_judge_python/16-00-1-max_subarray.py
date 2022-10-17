from typing import List


"""
Explantion for n(n+1)/2 total subarrays: https://math.stackexchange.com/questions/1194584/the-total-number-of-subarrays
An array of size n can have n subarray starting from 0 to n-1, 1 to n-1, 2 to n-2, and ... n-1 to n-1 Total = n
Similarly,array of size n-1 can have n -1 subarrays, starting from 0 to n - 2, 1 to n - 2, ... n-2 to n-2, Total n -1
so going on, array of size 1 will have subarrays of 1. 0 to 0. Total 1
Hence all size subaarys =  n + (n-1) + (n-2) + ... + 1 = n(n+1)/2

Trying to explain in layman terms.

Let's say f(0) = 0

f(1) = 1
f(2) = 3
f(3) = 6
f(4) = 10
f(5) = 15   
By observation, you can see that each result is just an addition of previous result and current number.

f(n) = n + f(n-1)


This is just from my experience. It's more relevant when the follow up question is about applying the solution to real world constraints, e.g. if the input data are too large to fit into a single machine's memory. Using Approach 2, sure the algorithm can keep fetching the data from disk for a chunk of data at a time, but it's limited to a single machine.

With divide-conquer approach, the large data can be broken into smaller chunks and distributed to more machines to compute and then it aggregates the results from all those machines at a later stage for the final answer. Then even though in theory, Approach 3 is less efficient, it's more horizontally scalable, i.e. by adding more machines of smaller specs to solve the problem.

For example Approach 3 can be extended by returning 3 values, max subarray starting from left, max subarray starting from right, and max subarray anywhere in between. This allows the coordinate/aggregator to quickly compute the combined sum without having to store 2 halves of the data in memory.
"""


#method 1, divide and conquer.
"""
Divide and conquer algorithms involve splitting up the input into smaller chunks until they're small enough to be easily solved, and then combining the solutions to get the final overall solution. If you're unfamiliar with them, check out this explore card.

If we were to split our input in half, then logically the optimal subarray either:

    Uses elements only from the left side
    Uses elements only from the right side
    Uses a combination of elements from both the left and right side

Thus, the answer is simply the largest of:

    The maximum subarray contained only in the left side
    The maximum subarray contained only in the right side
    The maximum subarray that can use elements from both sides
Time complexity is same as merge/quick sort, T(n) = 2T(n/2) + O(n), O(n) is the max_crossing_subarray method
hence O(nlogn) using masters theorem
Space: O(logn)
"""
#use https://pythontutor.com to understand
def maxSubArray(nums: List[int]) -> int:
    def max_crossing_subarray(nums, left, mid, right): #this function find max in subarray num[left, right], this include mid
        curr = best_left_sum = best_right_sum = 0

        # Iterate from the middle to the beginning.
        for i in range(mid - 1, left - 1, -1):
            curr += nums[i]
            best_left_sum = max(best_left_sum, curr)

        # Reset curr and iterate from the middle to the end.
        curr = 0
        for i in range(mid + 1, right + 1):
            curr += nums[i]
            best_right_sum = max(best_right_sum, curr)

        # The best_combined_sum uses the middle element and
        # the best possible sum from each half.
        return nums[mid] + best_left_sum + best_right_sum

    def findBestSubarray(nums, left, right):
        # Base case - empty array.
        if left >= right:
            return float('-Inf')

        mid = left + (right - left) // 2


        # Find the best subarray possible from both halves.
        left_half = findBestSubarray(nums, left, mid - 1)
        right_half = findBestSubarray(nums, mid + 1, right)
        best_combined_sum = max_crossing_subarray(nums, left, mid, right)

        # The largest of the 3 is the answer for any given input array.
        return max(best_combined_sum, left_half, right_half)
    
    # Our helper function is designed to solve this problem for
    # any array - so just call it using the entire input!
    return findBestSubarray(nums, 0, len(nums) - 1)

maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
maxSubArray([-2, 1, -3])


#method 3, brute force N^2
"""
Basically you start creating subarray, first with start index zero, and end index goes upto n-1
then start_index = 1, end index goes upto n - 1, in meantime keep track of the largest sum encountered
repeat till start_index = n-1
"""
def maxSubArray_brute(nums: List[int]) -> int:
        max_subarray_sum = float('-Inf')
        for i in range(len(nums)): #i here is the start index
            current_subarray_sum = 0
            for j in range(i, len(nums)):
                current_subarray_sum += nums[j]
                max_subarray_sum = max(max_subarray_sum, current_subarray_sum)
        
        return max_subarray_sum

maxSubArray_brute([-2, 1, -3, 4, -1, 2, 1, -5, 4])
maxSubArray_brute([-2, 1, -3])


#method 2: Dynamic Programming Yay!!!! Kadane Approach
"""
tldr;
 better way of phrasing the solution in prose is: when visiting a number in the array, it's worth resetting the current subarray to only the currently visited number if the currently visited number is larger than the sum of it and the previous subarray. So in the example [8, -19, 5, -4, 20], when we get to visiting number 5, the current subarray is [8, -19]. Adding 5 to the current subarray brings a total of -6, but 5 is bigger than -6 so it is more worthwhile to just reset the subarray to just [5]

Elaborate
    Lets assume you have an array which is carrying the max subarray at index i, that is B[i], now when we encounter
    element at j, where i < j, call A[j], only either of the two things can happen for array tracking the max subarray 
    that ends at index j ( # this is greedy approach)
        1 - either A[j] itself is bigger or  
        2 - B[i-1] + A[i]
    Therefore B[i] = max(A[i], B[i - 1] + A[i]), second item B[i - 1]+A[i], because it has to be a subarray, or start fresh
    from A[i], since A[i] larger than B[i - 1] + A[i]\

    Note: since subarrays must be contiguous, they must either be an individual element or involve elements from left
"""
#this is O(n) time and O(n) space
def maxSubArray_dp(nums: List[int]) -> int:
    B = [nums[0]]
    max_subarray_sum = max(float('-Inf'), B[-1])
    for item in nums[1:]:
        B.append(max(item, B[-1] + item))  # this is greedy approach, reseting to current item or sum
        max_subarray_sum = max(B[-1], max_subarray_sum) 
    return max_subarray_sum
maxSubArray_dp([-2, 1, -3, 4, -1, 2, 1, -5, 4])
maxSubArray_dp([-2, 1, -3])

#this is O(n) time and O(1) space
def maxSubArray_dp_2(nums: List[int]) -> int:
    local_max_subarray_sum = float('-Inf') #no need to put infinite
    max_subarray_sum = float('-Inf')
    for item in nums:
        local_max_subarray_sum = max(item, local_max_subarray_sum + item) # this is greedy approach
        max_subarray_sum = max(local_max_subarray_sum, max_subarray_sum)
    return max_subarray_sum
maxSubArray_dp_2([-2, 1, -3, 4, -1, 2, 1, -5, 4])
maxSubArray_dp_2([-2, 1, -3])