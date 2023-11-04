from typing import List

from test_framework import generic_test
# Easy heuristic:

# if you discard mid for the next iteration (i.e. l = mid+1 or r = mid-1) then use while (l <= r).
# if you keep mid for the next iteration (i.e. l = mid or r = mid) then use while (l < r)
# https://leetcode.com/problems/single-element-in-a-sorted-array/solution/1155561

# Another

# if you are returning from inside the loop, use left <= right
# if you are reducing the search space, use left < right and finally return a[left]
# https://leetcode.com/problems/single-element-in-a-sorted-array/solution/670414


"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Design an algo  for finding the position of the smallst element in a cyclically sorted array.
Intuition for shifted sorted array: Example: A = [378, 478, 550, 631, 103, 203, 220, 234, 279, 368]
    Since it is  shifted, the max element is not at the last position. 631 is max, so every element
    on or before 631 will always be greater than A[n - 1](last element). Hence to find the smaller element we need to 
    search in towards right, excluding that element itself, hence left = mid + 1. Conversely, since it is shifted, and we find a element 
    smaller than A[n-1], then rest of smaller elements will be always on or left to that element. Hence to find smaller element
    we need to search towards left including that element too, since that may be the smallest., hence right = mid
There is a point in the array at which you would notice a change. This is the point which would help us in this question. We call this the Inflection Point(Answer)
All the elements to the left of inflection point > first element of the array. 
All the elements to the right of inflection point < first element of the array. 
Assume all elements are distinct
Time: O(logn)
Note: problem cannot be solved in log n time if elements repeated
Logic:  
    for any mid, if A[mid] > A[n-1], n-1 being last index, then the minimum value must be the index after mid, in range [mid+1, n-1], here left becomes mid + 1. Conversely, if A[mid] < A [n  - 1], then no value can be in range [mid + 1, n - 1], here 
    right becomes mid and acts as the boundary for new subarray
Ex: [378, 478, 550, 631, 103, 203, 220, 234, 279, 368], ans = index 4
"""
def search_smallest_v2(A: List[int]) -> int:

    left, right = 0, len(A) - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] > A[right]: #right is acts like n - 1 index of that subarray
            # Minimum must be in A[mid + 1:right + 1].
            left = mid + 1
        else:  # A[mid] < A[right].
            # Minimum cannot be in A[mid + 1:right + 1] so it must be in A[left:mid + 1].
            right = mid
    # Loop ends when left == right.
    return left#inflection point

#for my simple mind, i will stick to left<= right, and return result from while loop
def search_smallest(A: List[int]) -> int:
    if (len(A) == 1):
        return 0
    left, right = 0, len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        """
        Explanation:
        mid == 0  and  A[mid] < A[mid + 1]: if the smallest element is towards leftmost, i.e., array is not shifted
        mid == len(A) - 1 and A[mid] < A[mid - 1]: if the smallest element is towards rightmost
        A[mid] < A[mid + 1] and A[mid] < A[mid - 1]: if smallest element is in between
        """
        #inflection point
        if (mid == 0 and A[-1] > A[mid] < A[mid + 1]) or (mid == len(A) - 1 and A[mid - 1] > A[mid] < A[0]) or (A[mid - 1] > A[mid] < A[mid + 1]):
            return mid
        elif A[mid] > A[right]:
            # Minimum must be in A[mid + 1:right + 1] since A[left] - A[mid] is already sorted without rotation
            left = mid + 1
        else:  # A[mid] < A[right].
            # Minimum cannot be in A[mid + 1:right + 1] so it must be in A[left:mid].
            right = mid - 1
    # Loop ends when left == right.
    return -1

search_smallest([378, 478, 550, 631, 103, 203, 220, 234, 279, 368])
search_smallest([7, 8, 9, 10, 11, 12, 13, 14, 1, 2, 3, 4, 5, 6])
search_smallest([1, 2, 3, 4, 5, 6])
search_smallest([2, 3, 4, 5, 6, 1])
search_smallest([1])
search_smallest([3,4,5,1,2])

#variant 1, find the mountain
"""
https://leetcode.com/problems/peak-index-in-a-mountain-array/
A sequence is strictly ascending if each element is greater that its predecessor. Suppose it is known that an 
Array A consists of a stricly ascending sequence follwed by strictly descending sequence. 
Then design an algo for finding the max(global peak or global maxima) element in A
Length should be at least 3
"""
def mountain_peak(A: List[int]) -> int:

    left, right = 0, len(A) - 1
    while left <= right:
        mid  = left + (right + left) // 2
        if A[mid] > A[mid + 1] and A[mid] > A[mid - 1]:
            return A[mid]
        elif A[mid] < A[mid + 1]:#follow the ascending order, move right
            left = mid + 1
        else:#follow the ascending order, move left
            right = mid - 1 # here mid - 1 because if A[mid] < A[mid - 1], then that mid cant be the asnwer

    return -1

mountain_peak([0,1,0])
mountain_peak([0,2,1,0])
mountain_peak([0,2,1,-1, -2, -3, -4, -5, -6, -7])
mountain_peak([0,10,5,2])


# Variant 2 - Method 1
"""
https://leetcode.com/problems/search-in-rotated-sorted-array/
Design an algo O(logn) for finding the position of an element k in cyclically sorted array of distinct elements
Logic: 
    Two binary searches
    Find the inflexion point or the smallest value
    Then use the samllest value to correctly determine in what range the k sits, and run binary search in that range
"""
def search_k_in_cyclic_array(A: List[int], k: int) -> int:
    if len(A) == 1:
        return 0 if A[-1] == k else -1
    left, right = 0, len(A) - 1
    smallest = -1
    while left <= right:
        mid = (left + right) // 2
        """
        Explanation:
        mid == 0  and  A[mid] < A[mid + 1]: if the smallest element is towards leftmost, i.e., array is not shifted
        mid == len(A) - 1 and A[mid] < A[mid - 1]: if the smallest element is towards rightmost
        A[mid] < A[mid + 1] and A[mid] < A[mid - 1]: if smallest element is in between
        """
        if (mid == 0 and A[-1] > A[mid] < A[mid + 1]) or \
            (mid == len(A) - 1 and A[mid - 1] > A[mid] < A[0]) or \
                (A[mid - 1] > A[mid] < A[mid + 1]):
            smallest = mid
            break
        elif A[mid] > A[right]:
            # Minimum must be in A[mid + 1:right + 1].
            left = mid + 1
        else:  # A[mid] < A[right].
            # Minimum cannot be in A[mid + 1:right + 1] so it must be in A[left:mid + 1].
            right = mid - 1
    
    #Now check if target lies in that A[smallest] and A[-1] then check binary search here
    # else binary serach in other A[0] - A[smallest - 1]
    if k == A[smallest]:
        return smallest
    elif k >= A[smallest] and k <= A[-1]:
        left, right = smallest, len(A) - 1
    else:#lies in other subarray
        left, right = 0, smallest - 1

    while(left <= right):
            mid = (left + right) // 2
            if A[mid] == k:
                return mid
            elif A[mid] > k:
                right = mid - 1
            else:
                left = mid + 1

    # Loop ends when left == right.
    return -1

search_k_in_cyclic_array([378, 478, 550, 631, 103, 203, 220, 234, 279, 368], 550)
search_k_in_cyclic_array([7, 8, 9, 10, 11, 12, 13, 14, 1, 2, 3, 4, 5, 6], 4)
search_k_in_cyclic_array([1, 2, 3, 4, 5, 6], 6)
search_k_in_cyclic_array([2, 3, 4, 5, 6, 1], 1)

# Variant 2 - Method 2
"""
https://leetcode.com/problems/search-in-rotated-sorted-array/
Design an algo O(logn) for finding the position of an element k in cyclically sorted array of distinct elements.
Logic: 
    One pass binary search
    Formula: If a sorted array is shifted, if you take the middle, always one side will be sorted. 
    Take the recursion according to that rule.

    1- take the middle and compare with target, if matches return.
    2- if middle is smaller than right side, it means mid - right is sorted & Binary search can be applied on right side.
        2a- if [mid] < target <= [right] then do recursion with mid + 1 (left), right
        2b- (mid - right) side is sorted, but target not in here, search on left right side 
        {left, mid - 1(right)} => Here one is NOT claiming that left side is sorted. We are NOT 
        applying binary search here per-se. We are just reducing our search space since we are 
        sure that element is NOT in the part 2a. The next iteration in this method would try to 
        figure out which part of the subarray needs to be looked into.
    3- if middle is greater than right side, it means left side (left - mid) is sorted
        3a- if [left] <= target < [mid] then do recursion with left , mid - 1 (right)
        3b- left side is sorted, but target not in here, search on right side i.e. 
        {mid  + 1(left) (right)} => Here one is NOT claiming that right side is sorted. 
        We are NOT applying binary search here per-se. We are just reducing our search space 
        since we are sure that element is NOT in the part 3a. The next iteration in this 
        method would try to figure out which part of the subarray needs to be looked into.
"""
def search_k_in_cyclic_array_method_2(A: List[int], k: int) -> int:
    if len(A) == 1:
        return 0 if A[-1] == k else -1
    left, right = 0, len(A) - 1
    while left <= right:
        
        mid = left + (right - left)//2
        if A[mid] == k:
            return mid
        elif A[mid] < A[right]: #this is unshifted array A[mid, right]
            if k > A[mid] and k <= A[right]:#if k lies inside that array,  #equal to sign important
                left = mid  + 1
            else: #mid to right is unrotated sorted but target not there
                right = mid - 1
        else:#A[left] - A[mid] is unshifted sorted array
            if k < A[mid] and k >= A[left]: #equal to sign important
                right = mid - 1
            else:
                left = mid + 1
    return - 1



search_k_in_cyclic_array_method_2([378, 478, 550, 631, 103, 203, 220, 234, 279, 368], 550)
search_k_in_cyclic_array_method_2([7, 8, 9, 10, 11, 12, 13, 14, 1, 2, 3, 4, 5, 6], 4)
search_k_in_cyclic_array_method_2([1, 2, 3, 4, 5, 6], 6)
search_k_in_cyclic_array_method_2([2, 3, 4, 5, 6, 1], 1)


# Variant 2-mod:
"""
81. Search in Rotated Sorted Array II
Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
"""
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('11-03-search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
