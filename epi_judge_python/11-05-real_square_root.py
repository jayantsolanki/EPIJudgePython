from test_framework import generic_test
import math

"""
Write an algo which takes a floating point value and returns its floating point value square root
Time: O(log(x/s)), where s is the tolerance
"""


def square_root_v1(x: float) -> float:

    # Decides the search range according to x's value relative to 1.0.
    left, right = (x, 1.0) if x < 1.0 else (1.0, x) #(x, 1.0) since square root of a fractional >= that number but less than 1

    # Keeps searching as long as left != right.
    while not math.isclose(left, right): # math.isclose(2,2.00000001) is false, math.isclose(2,2.000000001) is true
        mid = 0.5 * (left + right)
        mid_squared = mid * mid
        if mid_squared > x:
            right = mid #this is work since it is floating point, we deal with decimals, would not work in integer
        else:
            left = mid
    return left


# square_root(23)
#another take, more or less same as above, but easier to understand
def square_root_v2(x: float) -> float:

    # Decides the search range according to x's value relative to 1.0.
    left, right = (x, 1.0) if x < 1.0 else (1.0, x)#if x is < 1 then its square root will be always < 1
    
    # Keeps searching as long as left != right.
    while not math.isclose(left, right): # math.isclose(2,2.00000001) is false, math.isclose(2,2.000000001) is true
        mid = 0.5 * (left + right)
        mid_squared = mid * mid
        #if (mid * mid) <= x and (mid_tolerance * mid_tolerance) > x:
        if math.isclose((mid * mid), x) :
            return mid
        elif mid_squared > x:
            right = mid#this is work since it is floating point, we deal with decimals, would not work in integer
        else:
            left = mid
    return left
square_root_v2(23)

#practice: 06AUG2023
def square_root(x: float) -> float:

    # Decides the search range according to x's value relative to 1.0.
    left, right = (x, 1.0) if x < 1.0 else (1.0, x) #(x, 1.0) since square root of a fractional >= that number but less than 1
    # Keeps searching as long as left != right.
    if math.isclose(1.0, x):
        return x
    mid = 0
    while not math.isclose(left, right): # math.isclose(2,2.00000001) is false, math.isclose(2,2.000000001) is true
        mid = 0.5 * (left + right)
        mid_squared = mid * mid
        if math.isclose(mid_squared, x) and mid_squared < x:
            return mid
        elif mid_squared > x:
            right = mid#this is work since it is floating point, we deal with decimals, would not work in integer
        else:
            left = mid
    return right#or mid # left


#variant 1
"""
Given two positive floating point numbers x and y, calculate x/y within tolerance e if the division operation cannot be used.
Addition multiplication acceptable
Logic: You figure out the value for right, take the mid and multiply by y, if the value greater than x then 
right = mid else left =  mid
#not considering the sign
"""
import sys
def division(x: float, y: float):
    # left, right = 0, x
    if x < 1.0 and y < 1.0:
        if x > y:#0.30/0.25
            left, right = 1, sys.float_info.max
        else:#0.25/0.30
            left, right = x, 1
    elif y < 1.0:
        left, right = 1, sys.float_info.max#this may cause overflow
    else:#either x < 1.0 or x > y, or x < y, but y always > 1.0
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
