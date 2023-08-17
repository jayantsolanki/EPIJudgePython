import bisect
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
Write a program that takes a sorted array and a key and returns the index of first occurrence of that key, 
otherwise returns -1 if key not found in the array.
Logic:
    If we see any index i with element equal to k, then we do know that no subsequent elements can be the first k
    Therefore we discard all elements with index i + 1 or more. Thus we maintain a candidate set (array left after discard others)
Time: O(logn), this because each iteration reduces the size of candate array by half
"""
def search_first_of_k(A: List[int], k: int) -> int:

    left, right, result = 0, len(A) - 1, -1
    # A[left:right + 1] is the candidate set.
    while left <= right:
        # mid = (left + right) // 2
        mid = left + (right - left) // 2
        if A[mid] > k:
            right = mid - 1
        elif A[mid] == k:
            result = mid
            right = mid - 1  # Nothing to the right of mid can be solution.
        else:  # A[mid] < k.
            left = mid + 1
    return result


# Pythonic solution, awesome
def search_first_of_k_pythonic(A, k):
    i = bisect.bisect_left(A, k)#returns i where A[i:n-1] >= k
    return i if i < len(A) and A[i] == k else -1 # awesome

# variant 1
"""
Design an efficient algorithm that takes a sorted array and a key, and finds the index of the first occurence of an element greater than that key
Logic: Find the rightmost k and its index and return index + 1
"""

def find_gt(A: List[int], k: int):
    left, mid, right, result = 0, 0, len(A) - 1, -1
    while left <= right:
        mid = left + (right - left)//2
        if A[mid] < k:
            left = mid + 1
        elif A[mid] == k:
            result = mid
            left = mid + 1
            
        else:
            right = mid - 1
    #return (result + 1) if (result > -1 and result < len(A) - 1) else -1
    # return (result + 1) if (result !=len(A) - 1) else -1
    return (result + 1) if (result !=len(A)) else -1

#pythonic solution
# https://docs.python.org/3.9/library/bisect.html
def find_gt_pythonic(A: List[int], k: int):

    i = bisect.bisect_right(A, k)
    # if i != len(A):
    #     # result = i if A[i] != k else i - 1 , same result
    #     return i
    return i if i != len(A) else -1



find_gt([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 401)
find_gt_pythonic([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 401)

# variant 2
"""
https://www.youtube.com/watch?v=HtSuA80QTyo&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=4&ab_channel=MITOpenCourseWare
https://leetcode.com/problems/find-peak-element/submissions/
http://www.dsalgo.com/2013/03/find-local-minima-in-array.html
Explanation: 
    First we need to understand that if in an array of unique(important) integers first two numbers are decreasing and last two 
    numbers are increasing there ought to be a local minima. Why so? We can prove it in two ways. First we will do it 
    by negation (contradiction). If first two numbers are decreasing, and there is no local minima, that means 3rd number is less than 
    2nd number. otherwise 2nd number would have been local minima. Following the same logic 4th number will have to be 
    less than 3rd number and so on and so forth. So the numbers in the array will have to be in decreasing order. 
    Which violates the constraint of last two numbers being in increasing order. This proves by negation that there 
    need to be a local minima.

    We can prove this in some other way also. Suppose we represent the array as a 2-D graph where the index of the numbers in the array represents the x-coordinate. and the number represents the y-coordinate. Now for the first two numbers, derivative will be negative, and for last two numbers derivative will be positive. So at some point the derivative line will have to cross the x axis. As the array contains only unique elements there cannot be a derivative point on the x axis. Because that will mean that two consecutive index having same number. So for any intersection of x axis by the derivative line will be a local minima.

    We will solve this problem in O(log n) time by divide and conquer method. We will first check the mid index of the array. If it is smaller than its left and right, then it is the answer. If it is bigger than the left number then from start to left we have a subproblem, and as we proved already that starting with decreasing and ending with increasing sequence array will have to have a local minima, we can safely go to the left subarray. Otherwise if mid is bigger than its right, then we go to the right subarray. This way we guarantee a O(log n) algorithm to find any of the local minima present in the array.

Let A be an unsorted array of n unique integers, with A[0] >= A[1] and A[n-2] <= A[n-1]. Call an index i a local minimum if A[i] 
is less than or equal to its neighbours, i.e.,  A[i -1] > A[i] < A[i + 1]. How would you efficiently find a local minimum, 
if one exists?
Logic: 
    look at the middle element of the array. If it's a local minimum, return it. Otherwise, at least one adjacent value must be smaller than this one. Recurse in the half of the array containing that smaller element (but not the middle).
"""
#Answer is always there
def local_min(A):#size will be at least three, #this is for a special case
    #check for validity
    if A[0] < A[1] or A[-2] > A[-1]:
        return "Not a valid array, A[0] >= A[1] and A[n-2] <= A[n-1]"
    left, mid, right = 0, 0, len(A) - 1
    result = -1
    while left <= right:
        mid = left + (right - left)//2
        print(mid)
        if A[mid] < A[mid - 1] and A[mid] < A[ mid + 1]:
            result = mid
            break
        elif A[mid - 1] > A[mid] > A[mid + 1]:#move towards descending series, actually  second condition not needed
            left = mid + 1
        # A[mid+1] < A[mid]: Jayant 05AUG2023
        else:#A[mid - 1] < A[mid] < A[mid + 1] or A[mid - 1] < A[mid] > A[mid + 1] 
            right = mid - 1
    
    return A[result] if result!= -1 else result

local_min([9,7,2,8,5,6,7,8]) # 2, 5, 3 are the answers
local_min([700,699, 122,82, 83, 500]) # 2 is the answer
local_min([10, 9, 8, 10])
local_min([9,7,2,8,9,4,3,11]) # 2, 5, 3 are the answers
local_min([10, 9, 11])
local_min([10, 9, 11, 7, 20])
local_min([12, 11, 7, 20])

#find local valley, You may imagine that nums[-1] = nums[n] = -∞
def findValleyElement(A: List[int]) -> int:
    if len(A) == 1:
        return 0
    # if A[0] > A[1] or A[-2] < A[-1]:
    #     return -1
    left, mid, right = 0, 0, len(A) - 1
    result = -1
    while left <= right:
        mid = left + (right - left)//2
        # if A[mid] > A[mid - 1] and A[mid] > A[ mid + 1]:
        if (mid == 0 and A[mid] < A[mid + 1]) or (mid == len(A) -1 and A[mid] < A[mid - 1]) or (A[mid] < A[mid - 1] and A[mid] < A[ mid + 1]):
            result = mid
            break
        # when (A[mid] < A[mid - 1] and A[mid] < A[ mid + 1]) is false, if below is true or 
        elif A[mid] > A[mid + 1]:##go for descending,  A[mid] > A[ mid + 1]
            left = mid + 1
        # when (A[mid] < A[mid - 1] and A[mid] < A[ mid + 1]) is false, if below is true
        else:##go for ascending #A[mid] > A[mid - 1]
            right = mid - 1

    return result
#above code re-written, You may imagine that nums[-1] = nums[n] = -∞
def findValleyElementv2(A: List[int]) -> int:
    if len(A) == 1:
        return 0
    # if A[0] > A[1] or A[-2] < A[-1]:
    #     return -1
    left, mid, right = 0, 0, len(A) - 1
    result = -1
    if (A[0] < A[1]):#edge cases
        return 0
    if (A[len(A) - 1] < A[len(A) - 2]):#:#edge cases
        return len(A) - 1
    while left <= right:
        mid = left + (right - left)//2
        # if A[mid] > A[mid - 1] and A[mid] > A[ mid + 1]:
        if (A[mid] < A[mid - 1] and A[mid] < A[ mid + 1]):
            result = mid
            break
        # when (A[mid] < A[mid - 1] and A[mid] < A[ mid + 1]) is false, if below is true or 
        elif A[mid] > A[mid + 1]:##go for descending,  A[mid] > A[ mid + 1]
            left = mid + 1
        # when (A[mid] < A[mid - 1] and A[mid] < A[ mid + 1]) is false, if below is true
        else:##go for ascending #A[mid] > A[mid - 1]
            right = mid - 1

    return result

#find local peak, facebook, array elements are not distinct, and no boundary condition, You may imagine that nums[-1] = nums[n] = -∞
#check refined code in leetcode
# https://leetcode.com/problems/find-peak-element/submissions/
def findPeakElement(A: List[int]) -> int:#local peak or local maxima
    if len(A) == 1:
        return 0
    # if A[0] > A[1] or A[-2] < A[-1]:
    #     return -1
    left, mid, right = 0, 0, len(A) - 1
    result = -1
    while left <= right:
        mid = left + (right - left)//2
        # if A[mid] > A[mid - 1] and A[mid] > A[ mid + 1]:
        if (mid == 0 and A[mid] > A[mid + 1]) or (mid == len(A) -1 and A[mid] > A[mid - 1]) or (A[mid] > A[mid - 1] and A[mid] > A[ mid + 1]):
            result = mid
            break
        #If this element happens to be lying in a descending sequence of numbers. or a local falling slope
        #(found by comparing nums[i] to its right neighbour), it means that the peak will always lie towards the left 
        # of this element and vice versa
        #If the middle element, midmid lies in an ascending sequence of numbers, or a rising slope
        # (found by comparing nums[i] to its right neighbour), it obviously implies that the peak lies towards 
        #the right of this element
        #above (A[mid] > A[mid - 1] and A[mid] > A[ mid + 1]) will be false when  A[mid] < A[ mid + 1], so below elsif will run
        elif A[mid] < A[mid + 1]:#ascending 
            left = mid + 1
        #above (A[mid] > A[mid - 1] and A[mid] > A[ mid + 1]) will be false when  A[mid -] > A[ mid], so below else will run
        else:#descending
            right = mid - 1
    return result
    
#another verison 
def findPeakElementv2(A: List[int]) -> int:
    if len(A) == 1:
        return 0
    left, mid, right = 0, 0, len(A) - 1
    result = -1
    if (A[0] > A[1]):#edge cases
        return 0
    if (A[len(A) - 1] > A[len(A) - 2]):#:#edge cases
        return len(A) - 1
    while left <= right:
        mid = left + (right - left)//2
        if A[mid] < A[mid - 1]:
            right = mid - 1
        elif A[mid] < A[mid + 1]:
            left = mid + 1
        else:
            result = mid
            break
    return result
#find maxima
# https://leetcode.com/problems/peak-index-in-a-mountain-array/solution/
# Also a variant in Problem 11-02
#there wont be two maximas
def peakIndexInMountainArray(arr: List[int]) -> int:
    if len(arr) < 3:
        return False
    left, right, mid = 0, len(arr) -1, 0
    while left <= right:
        mid = left + (right - left) // 2
        # if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
        if  arr[mid - 1] < arr[mid] > arr[mid + 1] :
            return mid
        elif arr[mid] < arr[mid + 1]:#go towards ascending
            left = mid + 1
        else:
            right = mid
    return -1


#variant 3
"""
Design an algo which takes a sorted array A of integers, and int K, and returns the interval enclosing k, i.e., the pair of integers L and U such that L is the first occurence of k and L is the last occurence of k. If K does not appear, return [-1, -1].
Example: A = [1,2,2,4,4,4,7,11,11,13], k = 11, return [7,8] 
"""

def first_and_last(A, k):
    left, mid, result, right = 0, 0, -1, len(A) - 1
    while left <= right:#finding leftmost
        mid = left + (right - left)//2
        if A[mid] == k:
            right = mid - 1
            result = mid
        elif A[mid] > k:
            right = mid - 1
        else:
            left = mid + 1
    L = result
    left, mid, result, right = 0, 0, -1, len(A) - 1
    while left <= right:#finding rightmost
        mid = left + (right - left)//2
        if A[mid] == k:
            left = mid + 1
            result = mid
        elif A[mid] > k:
            right = mid - 1
        else:
            left = mid + 1
    U = result
    return [L, U]

def first_and_last_pythonic(A, k):
    i = bisect.bisect_left(A, k)
    L = i if i!=len(A) and A[i] == k else -1
    j = bisect.bisect_right(A, k)
    U = j - 1 if A[j - 1] == k else -1

    return [L, U]

first_and_last( [1,2,2,4,4,4,7,11,11,13], k = -111)
first_and_last_pythonic( [1,2,2,4,4,4,7,11,11,13], k = -111)

#variant 4
"""
https://stackoverflow.com/questions/7380629/perform-a-binary-search-for-a-string-prefix-in-python
Design an algo which tests if p is the prefix of string in an array of sorted strings
A = ["ab", "abd", "abdf", "abz"]
P = "abd"
This requires custom comparator
Logic:
    Since, strings are sorted, directly compare them like number (lexicographically), use binary search concept
"""

def check_prefix(A: List[str], p: str):
    left, mid, right, result = 0, 0, len(A) -1 , -1
    # while left <= right:
    #     mid = left + (right - left) // 2
    #     if len(A[mid]) < len(p):#only check if the length are same or word is bigger
    #         left = mid + 1
    #     elif p < A[mid][:len(p)]:
    #         right = mid - 1
    #     elif p == A[mid][:len(p)]:
    #         return mid
    #     else:
    #         left = mid + 1
    #above works
    while left <= right:
        mid = left + (right - left) // 2
        if p < A[mid][:len(p)]:
            right = mid - 1
        elif p == A[mid][:len(p)]:
            return mid
        else:
            left = mid + 1
    #above works
    #this doesnt work
    # while left <= right:
    #     mid = left + (right - left) // 2
    #     if p < A[mid]:
    #         right = mid - 1
    #     elif p == A[mid]:
    #         return mid
    #     else:
    #         left = mid + 1
    return result

check_prefix(["ab", "abd", "abdf", "abz"], 'abd')
check_prefix(["ab", "abc", "abdf", "abz"], 'abd')
check_prefix(["ab", "abc", "abbdf", "abz"], 'abd')

#variant 5:
"""
Design an algo which returns all the strings if p is the prefix of string in an array of sorted strings 
#based on Variant 3 algo for L and U
"""
def return_prefix(A: List[str], p: str):
    left, mid, right, result = 0, 0, len(A) -1 , -1
    while left <= right:
        mid = left + (right - left) // 2
        if p < A[mid][:len(p)]:
            right = mid - 1
        elif p == A[mid][:len(p)]:
            result =  mid
            right = mid - 1
        else:
            left = mid + 1
    L = result
    left, mid, right, result = 0, 0, len(A) -1 , -1
    while left <= right:
        mid = left + (right - left) // 2
        if p < A[mid][:len(p)]:
            right = mid - 1
        elif p == A[mid][:len(p)]:
            result =  mid
            left = mid + 1
        else:
            left = mid + 1
    U = result
    
    return [L, U]

return_prefix(["ab", "abd", "abdf", "abz"], 'abd')
return_prefix(["ab", "abc", "abdf", "abz"], 'abd')
return_prefix(["ab", "abc", "abbdf", "abz"], 'abd')

#alternative: using bisect. Important
class PrefixCompares(object):
     def __init__(self, value):
         self.value = value
     def __lt__(self, other):
         return self.value < other[0:len(self.value)]
    #  def __gt__(self, other):
    #      return self.value[0:len(self.value)] > other
    #above also works
     def __gt__(self, other):
         return self.value > other[0:len(self.value)]
# import bisect
names = ['adam', 'bob', 'bob', 'bob', 'bobby', 'bobert', 'chris']
names.sort()
key = PrefixCompares('bob')
leftIndex = bisect.bisect_left(names, key)
rightIndex = bisect.bisect_right(names, key)
print(names[leftIndex:rightIndex])#interval is leftindex, and rightindex - 1, subsetting is correct

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('11-01-search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
