from typing import List

from test_framework import generic_test

"""
WAP which takes an array of n integers, where A[i] denotes the maximum you can advance from index x, 
and return whether it is possible to advance to the last index starting from the beginning of the array
Below is O(n) time complexity algorithm, and also works on negative entries
Logic: as we iterate, we track the furthest index we can advance to, furthest we can advance is i + A[i]
It is a greedy algo
"""


def can_reach_end_ori(A: List[int]) -> bool:
    # TODO - you fill in here.
    furthest_reach_so_far, last_index = 0, len(A) - 1
    i = 0
    while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:#stop if i more than furthest distance reached so far, 
        #or furthest distances more than length of array
        furthest_reach_so_far = max(furthest_reach_so_far, A[i] + i)
        # print(i,furthest_reach_so_far)
        i += 1 #if i or current index tobe evaluated > furthest reach so far, that means no further can be moved, deadend

    return furthest_reach_so_far >= last_index

#another way
def can_reach_end(A: List[int]) -> bool:
    # TODO - you fill in here.
    furthest_reach_so_far, last_index = 0, len(A) - 1
    i = 0
    while furthest_reach_so_far < last_index:#stop if i more than furthest distance reached so far, 
        #or furthest distances more than length of array
        furthest_reach_so_far = max(furthest_reach_so_far, A[i] + i)
        if furthest_reach_so_far >= len(A)  - 1: #early stop
                return True
        if i >= furthest_reach_so_far: 
            return False
        # print(i,furthest_reach_so_far)
        i += 1 #if i or current index tobe evaluated > furthest reach so far, that means no further can be moved, deadend

    return True

print(can_reach_end([3, 3, 1, 0, 2, 0, 1])) # [3, 3, 1, 0, 2, 0, 1]	true	A valid advance sequence is: 0->1->4->6->6
print(can_reach_end([3, 2, 0, 0, 2, 0, 1])) # [3, 2, 0, 0, 2, 0, 1]	False
print(can_reach_end([1, 1, 1, 1, 1, 1, 1])) # true	

"""
Variant: WAP to compute the minimum number of steps needed to advance to the last location
Minimum steps means max reach to be find out for each point and have that only
"""
#wrong program
def number_of_steps(A: List[int]) -> bool:
    # TODO - you fill in here.
    furthest_reach_so_far, last_index = 0, len(A) - 1
    i = 0
    pathArray = []
    while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
        # furthest_reach_so_far = max(furthest_reach_so_far, A[i] + i)
        if furthest_reach_so_far < (A[i] + i):#this is indirectly finding the max
            furthest_reach_so_far = A[i] + i
            pathArray.append(A[i])
        i += 1
    if furthest_reach_so_far >= last_index:
        print(pathArray)
        return len(pathArray)+1
    else:
        return -1

print(number_of_steps([3, 3, 1, 0, 2, 0, 1])) # [3, 3, 1, 0, 2, 0, 1]	true	A valid advance sequence is: 0->1->4->6->6
print(number_of_steps([3, 2, 0, 0, 2, 0, 1])) # [3, 2, 0, 0, 2, 0, 1]	False
print(number_of_steps([1, 1, 1, 1, 1, 1, 1])) # true	
print(number_of_steps([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]))

# https://www.geeksforgeeks.org/minimum-number-of-jumps-to-reach-end-of-a-given-array/
# O(n^2)
def minJumps(arr, n):
    jumps = [0 for i in range(n)]
 
    if (n == 0) or (arr[0] == 0):
        return float('inf')
 
    jumps[0] = 0
 
    # Find the minimum number of
    # jumps to reach arr[i] from
    # arr[0] and assign this
    # value to jumps[i]
    for i in range(1, n):
        jumps[i] = float('inf')
        for j in range(i):
            #first condition to make sure thati can be reached from j, and second to make sure
            # j is not dead stop
            if (i <= j + arr[j]) and (jumps[j] != float('inf')):
                jumps[i] = min(jumps[i], jumps[j] + 1)
                break
    return jumps[n-1]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('5-04-advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
