from test_framework import generic_test

# Given a non-negative integer x, compute and return the square root of x.
# Value should largest integer whose square root is less than equal to k
#use binary search O(logk)
#alternative Newton's method for Square root
# https://www.youtube.com/watch?v=cOmAk82cr9M&ab_channel=MichelvanBiezen
def square_root_v2(k: int) -> int:
    l, r = 0, k

    while l <= r:
        mid = l + (r -l) // 2
        mid_squared = mid * mid

        if mid_squared <= k:#approaching the upper limit
            l = mid + 1
        else:
            r = mid - 1
    return r



#more simple
def square_root(k: int) -> int:
    left, right = 0, k
    if k == 1:
        return k

    while left <= right:
        mid = left + (right - left) // 2

        #if (mid * mid == k) or (mid * mid < k and k < (mid + 1) * (mid + 1)):# you have to just find the closest digit
        #if (mid * mid == k) or (mid * mid < k < (mid + 1) * (mid + 1)):# you have to just find the closest digit, above line also correct
        if (mid * mid == k):
            return mid
        elif (mid * mid < k < (mid + 1) * (mid + 1)):#square is less than or equal to
            return mid
        elif ((mid -1) * (mid - 1) < k < (mid) * (mid)):#square is less than or equal to
            return mid - 1
        elif mid * mid > k:
            right = mid - 1
        else:# mid * mid < x
            left = mid + 1
    return 0
# square_root(10)

#newton method of finding square root of a function
#see notes in the book https://postimg.cc/XB48ww5X
"""
Logic:
    We start with a number larger than square root of k, hence k//2, then keep on decreasing it using Newton method
    Once the new x  is reached, check if its square is less then k, if yes, then return that x.
"""
# Time: O(logk)
def square_root_(k: int) -> int:
    if k == 1:
        return k
    x = k // 2 # seed or the starting guessed x, start with a larger number, whose square root is definitely greater than k
    while True:
        if x * x <= k:
            return x
        x = (x + k//x)//2 #see eq 3 in notes

# square_root_newton(10)      


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('11-04-int_square_root.py',
                                       'int_square_root.tsv', square_root))
