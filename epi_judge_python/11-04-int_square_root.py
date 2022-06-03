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

        if mid_squared <= k:
            l = mid + 1
        else:
            r = mid - 1
    return r



#more simple
def square_root_binary(k: int) -> int:
    left, right = 0, k
    if k == 1:
        return k

    while left <= right:
        mid = left + (right - left) // 2

        #if (mid * mid == k) or (mid * mid < k and k < (mid + 1) * (mid + 1)):# you have to just find the closest digit
        if (mid * mid == k) or (mid * mid < k < (mid + 1) * (mid + 1)):# you have to just find the closest digit, above line also correct
            return mid
        elif mid * mid > k:
            right = mid - 1
        else:# mid * mid < x
            left = mid + 1
    return 0
# square_root(10)

#newton method of finding square root of a function
#see notes in the book
def square_root(k: int) -> int:
    if k == 1:
        return k
    x = k // 2 # seed or the starting guessed x
    while True:
        if x * x <= k:
            return x
        x = (x + k//x)//2

# square_root_newton(10)      


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('11-04-int_square_root.py',
                                       'int_square_root.tsv', square_root))
