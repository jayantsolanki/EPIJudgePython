"""
Write a program which takes a input as an array of digits encoding a non negative 
decimal integer D, an return D + 1, example [1, 3, 0] -> [1, 3, 1],
[9,9,9] -> [1,0,0,0] etc 
"""
from typing import List

from test_framework import generic_test


#brute force
#time complexity O(n)
def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):# like a school level addition, move the carry to next element
        # if A[i] != 10:
        #     break
        # A[i] = 0
        # A[i - 1] += 1
        # or
        if A[i]==10:
            A[i] = 0
            A[i-1] = A[i-1] + 1
        else:
            break
    if A[0] == 10:
        # there is a carry out, so we need one more digit to store the result.
        # A slick way to do this is to append a 0 at the end of the array
        # and update the first entry to 1
        A[0] = 1
        A.append(0)

    return A
#testing brute force algo
plus_one([1, 3, 0])
plus_one([1, 2, 3])
plus_one([9, 8, 9])
plus_one([9, 9, 9])

#variant
"""
WAP which takes as input two strings s and t of bits encoding binary numbers Bs and Bt, respectively, and returns a new string of bits representing Bs + Bt
"""

def plus_bits(Bs, Bt):
    if len(Bs) > len(Bt):
        Bt = '0'*(len(Bs) - len(Bt)) + Bt
    elif len(Bs) < len(Bt):
        Bs = '0'*(len(Bt) - len(Bs)) + Bs
    C = 0
    S = ""
    for i in reversed(range(0, len(Bs))):
        S = str(int(Bs[i]) ^ int(Bt[i]) ^ C) + S
        C = (int(Bs[i]) & C) |  (int(Bt[i]) & C) | (int(Bt[i]) & int(Bs[i]))

    if C:# adding this in the end
        S = '1' + S
    return (S)

plus_bits("1010", "0010")
plus_bits("1000000000000000000000", "0010")
plus_bits("1010100", "0010")
plus_bits("10", "0010")

#shortcut
def plus_bits2(Bs, Bt):
    return bin(int(Bs,2) + int(Bt,2))[2:]

plus_bits2("10", "0010")
plus_bits2("1010100", "0010")



print()

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('5-02-int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
