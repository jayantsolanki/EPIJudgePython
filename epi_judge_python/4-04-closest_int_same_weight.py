from test_framework import generic_test
import sys

# Write a program which takes as input a nonnegative integer x and returns a number y which is not equal to x, 
# but has the same weight as x and their absolute different is smallest as possible.
#look into the book for O(n) approach, similar to swap bits program
# the correct approach is to swap two rightmost bits which differs
#O(1)
def closest_int_same_bit_count(x: int) -> int:
    # TODO - you fill in here.
    if x in (0, sys.maxsize):#0, 1111111111111111
        return "Can not be found"
    lowestsetBit = x & ~(x-1) #remember this technique always
    lowestunSetbit = ~x & (x+1) #remember this technique always, 
    #trick is to remember that you need to sert first 0 to 1 but adding 1 to it
    if lowestunSetbit > lowestsetBit: # for cases like x = 7, 
        #we check for unsetbit first, because if it is greater than
        #definitely there should be 1 before it
        x |= lowestunSetbit
        x ^= lowestunSetbit>>1#need this for example 0100111, 
        #unset is 1000, and set is 1, hence cant do x ^= lowestsetbit
    else:
        x ^= lowestsetBit
        x |= lowestsetBit>>1
    return x



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('4-04-closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
