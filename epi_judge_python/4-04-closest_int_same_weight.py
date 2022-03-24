from test_framework import generic_test
import sys

# the correct approach is to swap two rightmost bits which differs
#O(1)
def closest_int_same_bit_count(x: int) -> int:
    # TODO - you fill in here.
    if x in (0, sys.maxsize):#0, 1111111111111111
        return "Can not be found"
    lowestsetBit = x & ~(x-1) #remember this technique always
    lowestunSetbit = ~x & (x+1) #remember this technique always
    if lowestunSetbit > lowestsetBit: # for cases like x = 7
        x |= lowestunSetbit
        x ^= lowestunSetbit>>1
    else:
        x ^= lowestsetBit
        x |= lowestsetBit>>1
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('4-04-closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
