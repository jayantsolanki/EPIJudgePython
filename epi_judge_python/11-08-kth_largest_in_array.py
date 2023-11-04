
import operator
import random
from typing import List, Tuple

from test_framework import generic_test

"""
QUICKSELECT
Design an algo for finding the kth largest element in an array.
Logic:
    We try to find the element in that array itself by rearranging the elements using a pivot
    There are many different versions of quickSort that pick pivot in different ways:
    - Always pick the first element as a pivot
    - Always pick the last element as a pivot
    - Pick a random element as a pivot
    - Pick median as a pivot

    We select an element at random (the pivot), and partition the array element which are less or greater than that
    pivot. In the end we have lesser element to the left or pivot and greater element to the right
    If elements are distinct, than there are can be any other element == pivot. 
    Now, if there are exactly k - 1 elements to the right, then pivot is the kth largest element.
    If right side has more than k -1 elements, then we reduce the search space to right side and discard left side and pivot
    If right side has lesser than k -1 elements, than we discard right side and pivot and search space the left side elements
    We again pick new pivot and repeat the process on smaller subarrays until we find kth largest element
#For k largest, array will be arranged in decreasing order
"""

# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
#worst case scenario is O(n^2), possible only when randomly selected pivot is smallest or the 
# largest value in current subarray
#probabilty of worst case decreases exponentially on longer array, hence the randomization 
# have almost certain O(n) time of algo
# #Time: O(n), derivation: T(n) = O(n) + O(n/2)= this solves to O(n)
def find_kth_largest(k: int, A: List[int]) -> int:
    def find_kth(comp):#O(n)
        # Partition A[left:right + 1] around pivot_idx, returns the new index of
        # the pivot, new_pivot_idx, after partition. After partitioning,
        # A[left:new_pivot_idx] contains elements that are "greater than" the
        # pivot, and A[new_pivot_idx + 1:right + 1] contains elements that are
        # "less than" the pivot.
        #
        # Note: "greater than" and "less than" are defined by the comp object.
        #
        # Returns the new index of the pivot element after partition.
        #
        """
            technique:
            1- copy the pivotValue in variable and then exchange the pivot value at pivot index to rightmost index value
            2 - initial newpivotindex = left, this new index will store the correct position of pivot value after partitioning
            3 - iterate from left to right - 1 index
                3a- check if the current value is greater than pivot, if true then swap A[left] A[newPivotindex]
                after end of loop swap rightmost element with value at newpivotindex and return this newpivotindex
        """
        def partition_around_pivot_original(left, right, pivot_idx):
            pivot_value = A[pivot_idx]
            new_pivot_idx = left#write_idx
            A[pivot_idx], A[right] = A[right], A[pivot_idx]#move the value at pivot_idx to rightmost side
            for i in range(left, right):#iterate through all the elements except the rightmost
                if comp(A[i], pivot_value):#this moves larger value to the left
                    A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]
                    new_pivot_idx += 1
            A[right], A[new_pivot_idx] = A[new_pivot_idx], A[right]
            #move the pivot value to its correct place now.
            #all values before new_pivot_idx are greater than pivot_value
            return new_pivot_idx
        def partition_around_pivot(left, right, pivot_idx):#based on dutch flag problem
            pivot_value = A[pivot_idx]
            right = right + 1
            equal = left
            while equal < right:
                if A[equal] > pivot_value:#move larger element to left
                    A[left], A[equal] = A[equal], A[left]
                    left = left + 1
                    equal = equal + 1
                elif A[equal] < pivot_value:
                    right -= 1
                    A[right], A[equal] = A[equal], A[right]
                else:
                    equal = equal + 1
            return equal - 1

        left, right = 0, len(A) - 1
        # T(n) = n + n/2 + n/4 ... = O(n) for average case, on every iteration pivot is moved 
        # to mid of the remaining array
        # Worst case: you keep on finding a pivot which is either largest or smallest, after moving 
        # it to it scorrect position it 
        # becomes this: n + (n - 1) + (n-2 )+ (n-3 )....  = O(n^2)
        while left <= right: 
            # Generates a random integer in [left, right].
            #note that k will be always within  [left, right], since you are altering left and right below
            pivot_idx = random.randint(left, right)
            #here the divide and conquer is based on newpivot index
            new_pivot_idx = partition_around_pivot(left, right, pivot_idx)#here the divide and conquer is based on newpivot index
            if new_pivot_idx == k - 1:
                return A[new_pivot_idx]
            elif new_pivot_idx > k - 1:
                right = new_pivot_idx - 1
            else:  # new_pivot_idx < k - 1
                left = new_pivot_idx + 1

        raise IndexError('no k-th node in array A')
    # this is comp definition, if k largest better to use greater than, no need to adjust k
    return find_kth(operator.gt) 
# find_kth_largest(2, [3, 1, -1, 5, 4])
# The numbering starts from one, i.e., if A = [3, 1, -1, 2] then
# find_kth_smallest(1, A) returns -1, find_kth_smallest(2, A) returns 1,
# find_kth_smallest(3, A) returns 2, and find_kth_smallest(4, A) returns 3.
def find_kth_smallest(k, A):
    def find_kth(comp):
        # Partition A[left:right + 1] around pivot_idx, returns the new index of
        # the pivot, new_pivot_idx, after partition. After partitioning,
        # A[left:new_pivot_idx] contains elements that are "greater than" the
        # pivot, and A[new_pivot_idx + 1:right + 1] contains elements that are
        # "less than" the pivot.
        #
        # Note: "greater than" and "less than" are defined by the comp object.
        #
        # Returns the new index of the pivot element after partition.
        def partition_around_pivot(left, right, pivot_idx):
            pivot_value = A[pivot_idx]
            new_pivot_idx = left
            A[pivot_idx], A[right] = A[right], A[pivot_idx]
            for i in range(left, right):
                if comp(A[i], pivot_value):
                    A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]
                    new_pivot_idx += 1
            A[right], A[new_pivot_idx] = A[new_pivot_idx], A[right]
            return new_pivot_idx

        left, right = 0, len(A) - 1
        # T(n) = n + n/2 + n/4 ... = O(n) for average case, on every iteration pivot is moved 
        # to mid of the remaining array
        # Worst case: you keep on finding a pivot which is either largest or smallest, 
        # after moving it to it scorrect position it 
        # becomes this: n + (n - 1) + (n-2 )+ (n-3 )....  = O(n^2)
        #in below code you decide the limit left and right based on pivot index when it 
        # is moved to its proper position
        while left <= right:#at every iteration you are reducing the search space
            # Generates a random integer in [left, right].
            #note that k will be always within  [left, right], since you are altering left and right below
            pivot_idx = random.randint(left, right) 
            new_pivot_idx = partition_around_pivot(left, right, pivot_idx)
            if new_pivot_idx == k - 1:
                return A[new_pivot_idx]
            elif new_pivot_idx > k - 1:
                right = new_pivot_idx - 1
            else:  # new_pivot_idx < k - 1.
                left = new_pivot_idx + 1
        raise IndexError('no k-th node in array A')

    return find_kth(operator.lt)


#Variant 1:
"""
Design an algo to find the median of an array
Use above algo and find the median based on count

The median of a sorted array of size N is defined as the middle element when N is odd and 
average of middle two elements when N is even. Since the array is not sorted here, we sort the array first, 
then apply above formula.
"""
def median_n(A):
    if len(A) % 2 == 1:
        # here  + 1 because k here begins with 1, i k begins with zero, then just use len(A)//2
        return find_kth_smallest(len(A) // 2 + 1, A) 
    else:
        return 0.5 * (find_kth_smallest(len(A) // 2, A) + find_kth_smallest((len(A) // 2) + 1, A)) 

median_n([3, 1, -1, 5, 4])

#Variant 2
"""
Design an algo for finding the kth largest element in array A in the presence of duplicates.
kth largest element is defined as A[k-1] when A is sorted in stable sorted manner, that is, if A[i] == A[j] and i < j
then A[i]  must appear before A[j] after stable sorting.
Logic:
    Just treat duplicate elements as larger and keep them at left side
"""
def find_kth_largest_for_duplicates(k: int, A: List[int]) -> int:
    def find_kth(comp):
        # Partition A[left:right + 1] around pivot_idx, returns the new index of
        # the pivot, new_pivot_idx, after partition. After partitioning,
        # A[left:new_pivot_idx] contains elements that are "greater than" the
        # pivot, and A[new_pivot_idx + 1:right + 1] contains elements that are
        # "less than" the pivot.
        #
        # Note: "greater than" and "less than" are defined by the comp object.
        #
        # Returns the new index of the pivot element after partition.
        #
        """
        technique:
        1 - copy the pivotValue in a variable and then exchange the pivot value at pivot index to rightmost index value
        3 - initial newpivotindex = left, this new index will store the correct position of pivot value after partitioning
        3 - iterate from left to right - 1 index
            3a- check if the current value is greater than pivot, if true then swap A[left] A[newPivotindex]
            after end of loop swap rightmost element with value at newpivotindex and return this newpivotindex
        """
        def partition_around_pivot(left, right, pivot_idx):
            pivot_value = A[pivot_idx]
            new_pivot_idx = left
            A[pivot_idx], A[right] = A[right], A[pivot_idx]
            for i in range(left, right):
                if comp(A[i], pivot_value):
                    A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]
                    new_pivot_idx += 1
            A[right], A[new_pivot_idx] = A[new_pivot_idx], A[right]
            return new_pivot_idx
        # def partition_around_pivot(left, right, pivot_idx):#based on dutch flag problem
        #     pivot_value = A[pivot_idx]
        #     right = right + 1
        #     equal = left
        #     while equal < right:
        #         if A[equal] >= pivot_value:#move larger element to left
        #             A[left], A[equal] = A[equal], A[left]
        #             left = left + 1
        #             equal = equal + 1
        #         elif A[equal] < pivot_value:
        #             right -= 1
        #             A[right], A[equal] = A[equal], A[right]
        #         else:#this actually never runs
        #             equal = equal + 1
        #     return equal - 1

        left, right = 0, len(A) - 1
        #in below code you decide the limit left and right based on pivot index when it is 
        # moved to its proper position
        # T(n) = n + n/2 + n/4 ... = O(n) for average case, on every iteration pivot is 
        # moved to mid of the remaining array
        # Worst case: you keep on finding a pivot which is either largest or smallest, after
        #  moving it to it scorrect position it 
        # becomes this: n + (n - 1) + (n-2 )+ (n-3 )....  = O(n^2)
        while left <= right:
            # Generates a random integer in [left, right].
            #note that k will be always within  [left, right], since you are altering left and right below
            pivot_idx = random.randint(left, right)
            #here the divide and conquer is based on newpivot index
            new_pivot_idx = partition_around_pivot(left, right, pivot_idx)
            if new_pivot_idx == k - 1:
                return A[new_pivot_idx]
            elif new_pivot_idx > k - 1:
                right = new_pivot_idx - 1
            else:  # new_pivot_idx < k - 1
                left = new_pivot_idx + 1

        raise IndexError('no k-th node in array A')
    #using greater or equal to, this is comp definition, if k largest better to use greater than, no need to adjust k
    return find_kth(operator.ge) 

find_kth_largest_for_duplicates(8, [3, 1, -1, 4, 5, 5, 5, 5])

#variant2.5
# This is probably a Microsoft interview question.
# https://stackoverflow.com/questions/11143401/kth-smallest-element-out-of-an-non-unique-sorted-array
# kth smallest element out of an non-unique sorted array
"""
Here's an O(kLogN) solution:

Approach 1:
Take a max heap & insert first k unique elements[can be easily checked]. Heapify the heap.
Now, when a new element is smaller than the head of the heap,replace head with this new element heapify it. 
At the last, the head of the heap indicates kth smallest element if size of the heap is k else kth smallest 
element doesn't exist.

Time complexity: O(NlogK)

Using a variation of Binary Search to find the last occurrence of a given value,
Use bisect_right to find the next element

Get 1st value - O(1).
Search for last occurrence of this value O(logN), then look at next element to get 2nd value - O(1).
Repeat until kth value is found.

So, get the first element, update counter = 1, now get the last position of that element using binary 
search than return the
index + 1 to get the second element, update counter = 2, keep doing for next and next

Approach 2[A better approach]:
The elements may be duplicated right. So, check for unique elements by comparing with its previous elements & 
stop if unique variables found so far counts to k.
Time complexity: O(N)
Space complexity: O(1)

"""


# variant 3, unable to work properly
"""
A number of apartments buildings are coming up on a new street. The postal service wants to place a single 
mailbox on the street.
Their objective is to minimize the total distance that residents have to walk to collect their mail each day.
*Different building may have different number of residents.
Devise an algo that computes where  to place the mailbox so as to minimize the total  distances, that 
residents travel to get to the mail box. Assume the input is specified as an array of buildings objects, 
where each building object has field indicating the 
number of residents in that building, and a field indicating the building's distance from the start of the street.
https://leetcode.com/problems/allocate-mailboxes/
https://stackoverflow.com/questions/44725690/algorithm-to-place-a-mailbox-to-minimize-the-total-distance-that-the-residents-t

https://www.quora.com/How-to-design-an-algorithm-to-place-a-mailbox-to-minimize-the-total-distance-
that-the-residents-travel-to-get-their-mail
The brute-force approach would be to treat each person in a building as being a separate 
building (at the same location as the building they are in), thereby reducing the problem to the 
case where you are trying to optimize for just buildings rather than people.

You can then use quickselect to solve this - the complexity though is O(W) where W is the total number 
of people. (Assume each building has at least one person.)

You can do mimic the quickselect algorithm to drive this down to O(n). The idea is to pick start with a
 building at random, see how many people are on either side. If that number is equal, great, you’re done. 
 Otherwise the point you want is to the left (if more people are on the left of the initial point) or on 
 the right (if more people are on the right). When you continue, you work on a subset of buildings (roughly half), 
 and you look not for the median anymore, specifically if you have to go to the right, you need the find where 
 the (W/2 - number on left)-th person is. (Essentially weighted median finding.) It’s randomized, expected time complexity is O(n).)

It is a weighted median problem

"""

def postbox_median(A):
    people = [x*y for x, y in A]
    total_people = sum(people)
    print(people, total_people)
    def find_kth(comp):
        # Partition A[left:right + 1] around pivot_idx, returns the new index of
        # the pivot, new_pivot_idx, after partition. After partitioning,
        # A[left:new_pivot_idx] contains elements that are "greater than" the
        # pivot, and A[new_pivot_idx + 1:right + 1] contains elements that are
        # "less than" the pivot.
        #
        # Note: "greater than" and "less than" are defined by the comp object.
        #
        # Returns the new index of the pivot element after partition.
        def partition_around_pivot(left, right, pivot_idx):
            pivot_value = A[pivot_idx][0] * A[pivot_idx][1]
            new_pivot_idx = left
            lw, rw = 0, 0
            A[pivot_idx], A[right] = A[right], A[pivot_idx]
            for i in range(left, right):
                if comp(A[i][0] * A[i][1], pivot_value):
                    lw = lw + A[i][0] * A[i][1]
                    A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]
                    new_pivot_idx += 1
            A[right], A[new_pivot_idx] = A[new_pivot_idx], A[right]
            return (new_pivot_idx, lw, rw)

        left, right = 0, len(A) - 1
        while left <= right:
            # Generates a random integer in [left, right].
            pivot_idx = random.randint(left, right)
            new_pivot_idx = partition_around_pivot(left, right, pivot_idx)
            if new_pivot_idx == k - 1:
                return A[new_pivot_idx]
            elif new_pivot_idx > k - 1:
                right = new_pivot_idx - 1
            else:  # new_pivot_idx < k - 1.
                left = new_pivot_idx + 1
        raise IndexError('no k-th node in array A')

    # return find_kth(operator.lt)


postbox_median([(2, 10), (1, 5), (3, 2), (10, 3), (5, 5), (4, 3), (8, 2)])

#Variant 4: 
#Implement a Quick sort in ascending order
def SortArray(nums):
    print(f"Original array: {nums}")
    def quickSelect(nums, left, right, pivot_idx):
        pivot = nums[pivot_idx]
        #swap rightmost with pivot
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        new_pivot_idx = left#write_idx
        for i in range(left, right):
            if nums[i] <= pivot:
                nums[new_pivot_idx], nums[i] = nums[i], nums[new_pivot_idx]
                new_pivot_idx += 1
        nums[new_pivot_idx], nums[right] = nums[right], nums[new_pivot_idx]
        return new_pivot_idx#this is the correct position

    def QuickSort(nums, left, right):
        if left <= right:
            pivot_idx = random.randint(left, right)#you can simple pass the right element also
            new_pivot_idx = quickSelect(nums, left, right, pivot_idx)
            QuickSort(nums, left, new_pivot_idx - 1)#now run on left side
            QuickSort(nums, new_pivot_idx + 1, right)#now run on right side
    
    QuickSort(nums, 0, len(nums) - 1)
    print(f"Sorted array: {nums}")

SortArray([3, 1, -1, 4, 5, 5, 5, 5])
             



#Check this problem for custom sort
# https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('11-08-kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
