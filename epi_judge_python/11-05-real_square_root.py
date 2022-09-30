from numpy import Inf
from test_framework import generic_test
import math

"""
Write an algo which takes a floating point value and returns its floating point value square root
Time: O(log(x/s)), where s is the tolerance
"""


def square_root(x: float) -> float:

    # Decides the search range according to x's value relative to 1.0.
    left, right = (x, 1.0) if x < 1.0 else (1.0, x) #(x, 1.0) since square root of a fractional >= that number but less than 1

    # Keeps searching as long as left != right.
    while not math.isclose(left, right): # math.isclose(2,2.00000001) is false, math.isclose(2,2.000000001) is true
        mid = 0.5 * (left + right)
        mid_squared = mid * mid
        if mid_squared > x:
            right = mid
        else:
            left = mid
    return left


square_root(23)
#another take, more or less same as above, but easier to understand
def square_root_v2(x: float) -> float:

    # Decides the search range according to x's value relative to 1.0.
    left, right = (x, 1.0) if x < 1.0 else (1.0, x)#if x is < 1 then its sqaure root will be always < 1
    
    # Keeps searching as long as left != right.
    while not math.isclose(left, right): # math.isclose(2,2.00000001) is false, math.isclose(2,2.000000001) is true
        mid = 0.5 * (left + right)
        mid_squared = mid * mid
        #if (mid * mid) <= x and (mid_tolerance * mid_tolerance) > x:
        if math.isclose((mid * mid), x) :
            return mid
        elif mid_squared > x:
            right = mid
        else:
            left = mid
    return left
square_root_v2(23)


#variant 1
"""
Given two positive floating point numbers x and y, calculate x/y within tolerance e if the division operation cannot be used.
Addition multiplication acceptable
#not considering the sign
"""
import sys
def division(x: float, y: float):
    # left, right = 0, x
    if x < 1.0 and y < 1.0:
        if x > y:
            left, right = 1, sys.float_info.max
        else:
            left, right = x, 1
    elif y < 1.0:
        left, right = 1, sys.float_info.max#this may cause overflow
    else:
        left, right = 0, x
    # left, right = (x, 1)if x < y else (0, 1)

    while not math.isclose(left, right):
        mid = 0.5 * (left + right)
        if math.isclose(mid * y, x):
            return mid
        elif mid * y > x:
            right = mid
        else:
            left = mid
    return -1

division(7, 3)
division(100, 3)
division(0.5, 3)
division(5, 0.3)
division(0.4, 0.5)
division(0.5, 0.3)
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('11-05-real_square_root.py',
                                       'real_square_root.tsv', square_root))
