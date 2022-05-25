import bisect
from typing import List

from test_framework import generic_test

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
        mid = (left + right) // 2
        if A[mid] > k:
            right = mid - 1
        elif A[mid] == k:
            result = mid
            right = mid - 1  # Nothing to the right of mid can be solution.
        else:  # A[mid] < k.
            left = mid + 1
    return result


# Pythonic solution
def search_first_of_k_pythonic(A, k):
    i = bisect.bisect_left(A, k)
    return i if i < len(A) and A[i] == k else -1 # awesome

# variant 1
"""
Design an efficient algorithm that takes a sorted array and a key, and finds the index of the first occurence of an element greater that that key
"""

def find_gt(A: List[int], k: int):
    left, mid, right, result = 0, 0, len(A) - 1, -1
    while left <= right:
        mid = left + (right - left)//2
        if A[mid] < k:
            left = mid + 1
        elif A[mid] == k:
            left = mid + 1
            result = mid
        else:
            right = mid - 1
    return (result + 1) if (result > -1 and result < len(A) - 1) else -1

#pythonic solution
# https://docs.python.org/3.9/library/bisect.html
def find_gt_pythonic(A: List[int], k: int):
    result = -1
    i = bisect.bisect_right(A, k)
    # if i != len(A):
    #     # result = i if A[i] != k else i - 1 , same result
    #     return i
    return i if i != len(A) else result



find_gt([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], -14)
find_gt_pythonic([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], -14)

# variant 2
"""
http://www.dsalgo.com/2013/03/find-local-minima-in-array.html
Explanation: 
    First we need to understand that if in an array of unique(important) integers first two numbers are decreasing and last two 
    numbers are increasing there ought to be a local minima. Why so? We can prove it in two ways. First we will do it 
    by negation. If first two numbers are decreasing, and there is no local minima, that means 3rd number is less than 
    2nd number. otherwise 2nd number would have been local minima. Following the same logic 4th number will have to be 
    less than 3rd number and so on and so forth. So the numbers in the array will have to be in decreasing order. 
    Which violates the constraint of last two numbers being in increasing order. This proves by negation that there 
    need to be a local minima.
Let A be an unsorted array of n integers, with A[0] >= A[1] and A[n-2] <= A[n-1]. Call an index i a local minimum if A[i] 
is less than or equal to its neighbours, i.e.,  A[i -1] > A[i] < A[i + 1]. How would you efficiently find a local minimum, 
if one exists?
Logic: 
    look at the middle element of the array. If it's a local minimum, return it. Otherwise, at least one adjacent value must be smaller than this one. Recurse in the half of the array containing that smaller element (but not the middle).
"""
def local_min(A):#size will be at least three
    #check for validity
    if A[0] < A[1] or A[-2] > A[-1]:
        return "Not a valid array, A[0] >= A[1] and A[n-2] <= A[n-1]"
    left, mid, right = 0, 0, len(A) - 1
    result = -1
    while left <= right:
        mid = left + (right - left)//2
        if A[mid] < A[mid - 1] and A[mid] < A[ mid + 1]:
            result = mid
            break
        elif A[mid] >= A[mid + 1]:
            left = mid + 1
        else:
            right = mid - 1
    
    return A[result] if result!= -1 else result

local_min([9,7,2,8,5,6,7,8]) # 2, 5, 3 are the answers
local_min([700,699, 122,82, 83, 500]) # 2 is the answer
local_min([10, 9, 8, 10])
local_min([9,7,2,8,9,4,3,8]) # 2, 5, 3 are the answers

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

#alternative:
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
print(names[leftIndex:rightIndex])

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('11-01-search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
