from test_framework import generic_test
import math

def is_palindrome_number(x: int) -> bool:
    # TODO - you fill in here.
    if x <= 0:#only for positives
        return x == 0
    num_digits = math.floor(math.log10(x)) + 1 # get the number of digits#this is crucial
    msd_mask = 10**(num_digits-1)#-1 since 1 is also part of digit, for 5 digit number 10000
    for i in range(num_digits // 2): # half the range, you have to check till the middle itself
        if x // msd_mask != x % 10: # get the most significant digits, it is always x/msd^n-1, 10000/1000, n = 5
            return False
        x %= msd_mask # removes the most significant digit of x, example 32345%10000 = 2345
        x //= 10 # remove the least significant digit of x, example 32345/10 = 3234
        msd_mask //= 100# why hundred, because you are removing lsd and msd, that means two zeros
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('4-09-is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
