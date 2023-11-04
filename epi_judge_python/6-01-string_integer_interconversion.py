from test_framework import generic_test
from test_framework.test_failure import TestFailure

"""
Implement an integer to string conversion function, and a string to integer conversison function, 
For example, if the input to the first function is the integer 314, it should retum the string "31.4" and 
if the input to the second function is the string "314" it should return the integer 314.
"""
#not supposed to use int and str
#   logic: extract each digit using %10 and /10 then
#   Use ord and chr
# approach is to add each extracted digit to the end, and then reverse it
def int_to_string(x: int) -> str:

    is_negative = False
    if x < 0:
        x, is_negative = -x, True

    s = []
    while True: #cant use x here, it will fail for x == 0
        s.append(chr(ord('0') + x % 10))#get ord value than add the number then convert to character
        x //= 10
        if x == 0:
            break

    # Adds the negative sign back if is_negative
    return ('-' if is_negative else '') + ''.join(reversed(s))

# start from left, extract the character, multiply the partial by 10  for each succeeding character
def string_to_int_simple(s: str) -> int:
    running_sum = 0
    sign = 1
    for digit in s:
        if digit == '-':
            sign = -1
        elif digit == '+':
            sign = 1
        else:
            running_sum = running_sum*10 + ord(digit) - ord('0')
    return sign*running_sum

    # return (-1 if s[0] == '-' else 1) * functools.reduce(
    #     lambda running_sum, c: running_sum * 10 + string.digits.index(c),s[s[0] in '-+':], 0)
    # return (-1 if s[0] == '-' else 1) * functools.reduce(
    #     lambda running_sum, c: running_sum * 10 +  ord(c) - ord('0'),s[s[0] in '-+':], 0)

def string_to_int(s: str) -> int:
    running_sum = 0
    sign = -1 if s[0] == '-' else 1
    for digit in s[s[0] in '-+':]:
        running_sum = running_sum*10 + ord(digit) - ord('0')
    return sign*running_sum

    # return (-1 if s[0] == '-' else 1) * functools.reduce(
    #     lambda running_sum, c: running_sum * 10 + string.digits.index(c),s[s[0] in '-+':], 0)
    # return (-1 if s[0] == '-' else 1) * functools.reduce(
    #     lambda running_sum, c: running_sum * 10 +  ord(c) - ord('0'),s[s[0] in '-+':], 0)

string_to_int('1234')
# int_to_string(1234)


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('6-01-string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
