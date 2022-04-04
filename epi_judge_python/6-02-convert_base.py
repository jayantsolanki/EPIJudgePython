import functools
import string

from test_framework import generic_test

# string.hexdigits   = '0123456789abcdefABCDEF'
#return string value of a string number in a particular base with a targetted base
# example 615 base 7 in base 13 is 1A7
# time complexity: O(n(1 + log(b1) base b2)), where n is length of given string
# resoning: first, we perform n multiply-and-adds to get decimal number from given string
# then we prform log(x) base b2 multiply and adds to get result. 
# The value x is upper bounded by b1^n and log(b1^n) base b2 = nlog(b1) base b2
def convert_base_original(num_as_string: str, b1: int, b2: int) -> str:
    def construct_from_base(num_as_int, base):
        return ('' if num_as_int == 0 else
                construct_from_base(num_as_int // base, base) +
                string.hexdigits[num_as_int % base].upper())

    is_negative = num_as_string[0] == '-'
    #first converting into decimal format
    num_as_int = functools.reduce(
        lambda x, c: x * b1 + string.hexdigits.index(c.lower()),
        num_as_string[is_negative:], 0)
    return ('-' if is_negative else '') + ('0' if num_as_int == 0 else
                                           construct_from_base(num_as_int, b2))

#for my simple mind
def convert_base(num_as_string: str, b1: int, b2: int) -> str:

    def construct_from_base(num_as_int, base):#extract last digit and work up
        if num_as_int == 0:
            return ""
        else:
            return construct_from_base(num_as_int // base, base) + string.hexdigits[num_as_int % base].upper()

    is_negative = num_as_string[0] == '-'
    #first converting into decimal format
    num_as_int = 0
    for digit in num_as_string[num_as_string[0] in '-+':]:
        num_as_int = num_as_int*b1 + string.hexdigits.index(digit.lower())# had to use this, since ord('A) = 65, ord('9') = 57

    return ('-' if is_negative else '') + ('0' if num_as_int == 0 else
                                           construct_from_base(num_as_int, b2))


convert_base("615", 7, 13)
convert_base("1111", 2, 10)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('6-02-convert_base.py', 'convert_base.tsv',
                                       convert_base))
