import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

"""
WAP to delete duplicates from the a sorted array and return the number of valid numbers
O(n) complexity with O(1) space complexity
Logic: since array is sorted, repeated elements must appear one-after the another.
So we do not need an auxiliary data structure (dictionary) to check if an element
has appeared already (A[i]) == A[i-1]. We move just one element, rather than entire sub array to the left
"""


# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:
    if not A:
        return 0
    
    write_index = 1
    for i in range(1, len(A)):
        if A[write_index -1] != A[i]:#this updates the write_index only if there is no repetition
            A[write_index] = A[i]
            write_index += 1
    print(A[:write_index])
    return write_index


#test
print(delete_duplicates([2,3,5,5,7,11,11,11,13]))

"""
Variant 1:
WAP that takes an array and a key, and updates the array so that all occurences of the key have been removed, and the remaining
elements have been shifted left to fill the empty indices. Return the number of remaining elements. No requirements for number stored after last
valid element
This can be also done using list comprehension, just saying
"""

def removeKey(A, key):
    if not A:
        return 0
    pos = 0
    for i in range(len(A)):
        if A[i]!= key:
            A[pos] = A[i]
            pos = pos + 1
    print(A[:pos])
    return pos

def removeKeyV2(A, key):
    return len([val for val in A if val!=key] )

#testing
print(removeKey([2,1,3,3,4,5,6,3], 3))
print(removeKeyV2([2,1,3,3,4,5,6,3], 3))
print(removeKey([2,1,3,3,4,5,6,3], 2))
print(removeKey([1,1,1,1,1,1,2,1,1,1], 1))
print(removeKey([1,1,1,1,1,1,2,1,1,1], 2))
print(removeKey([1,1,1,1,1,1,1,1,1], 1))


"""
Variant 2:
WAP which takes as input a sorted Array A of integers and a positive integer m, and updates
the array so that if x appears m times in A it appears exactly min(2, m) times in A.
The update to A should be performed in one pass, and no additional storage may be allocated
Logic: remove extra occurences of elements which have count of m, and set them to min(2,m), that is repeat at most twice only

"""
def minArray(A, m):
    if not A:
        return []
    repeat = min(2, m)# either one or two
    #remember it is a sorted array
    count = 1
    pos = 1
    for i in range(1, len(A)):
        if A[i-1] != A[i]:
            if count == m:
                pos = pos - count + repeat#pull back the pos
                count = 1
            else:
                count = 1
        else:
            count = count + 1
        A[pos] = A[i]
        pos += 1

    if count == m:#if number repeated is last in series
        pos = pos - count + repeat

    return A[:pos]




print(minArray([1,2,2,3,3,3,4,4,5,6,6,6], 3))
print(minArray([1,1,2,2,2,3,3,3,4,4,4, 5, 5, 5, 6], 1))
print(minArray([1,2,2,3,3,4,4,4,5,6,6,6, 7, 7, 7, 7, 7], 3))



@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('5-05-sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
