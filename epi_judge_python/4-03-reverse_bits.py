from test_framework import generic_test
import math
"""
Write a program that takes a 64bit unsigned integer and retuns the 64bit unsigned integer consisting of bits 
in reverse order.
"""

def reverse_bits(x: int) -> int:
    # TODO - you fill in here.
    bit_size = 64 # creating this for 64bit number reverse
    y = 0
    position = bit_size - 1
    while position >= 0:#start with LSB, push it to MSB
        y |=(x & 1) << position #extract digit and push it to left
        x >>= 1#kick out LSB
        position -= 1
    return y

def reverse_bits2(x: int) -> int:# i think this one should be correct, even though it is failing the trials
    # TODO - you fill in here.
    #bit_size = 64 # creating this for 64bit number reverse
    y = 0
    position = math.floor(math.log(x, 2))#may be use this
    while position >= 0:#start with LSB, push it to MSB
        y |=(x & 1) << position
        x >>= 1#kick out LSB
        position -= 1
    return y


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('4-03-reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
    # exit(
    #     generic_test.generic_test_main('4-03-reverse_bits.py', 'reverse_bits.tsv',
    #                                    reverse_bits))
