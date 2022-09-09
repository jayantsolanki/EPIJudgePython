from test_framework import generic_test
from test_framework.test_failure import TestFailure

"""
Implement runlength encoding and decoding scheme. Assume the string to be decoded is a valid encoding.
Time : O(n)
"""
#my implementation
def decoding(s: str) -> str:
    # TODO - you fill in here.
    result = []
    count = 0
    for chr in s:
        if chr.isdigit():
            count = count * 10 + int(chr)#number can be more than single digit hence multiplying by 10
        else:
            result.append(chr * count)
            count = 0 
    return "".join(result)

# decoding("3e4f2e")

#assuming there are only alphabets present, no numbers
#my implementation
def encoding(s: str) -> str:
    result = []
    prev_char = None
    count = 0
    for chr in s:
        if prev_char is None:
            count = 1
            prev_char = chr
        elif chr != prev_char:
            result.append(str(count) + prev_char)
            count = 1
            prev_char = chr
        else:
            count += 1
    result.append(str(count) + prev_char) # for the last character
    return "".join(result) 
# encoding("eeeffffee")

def decoding_ori(s: str) -> str:

    count, result = 0, []
    for c in s:
        if c.isdigit():
            count = count * 10 + int(c)
        else:  # c is a letter of alphabet.
            result.append(c * count)  # Appends count copies of c to result.
            count = 0
    return ''.join(result)


def encoding_ori(s: str) -> str:

    result, count = [], 1
    for i in range(1, len(s) + 1):
        if i == len(s) or s[i] != s[i - 1]:
            # Found new character so write the count of previous character.
            result.append(str(count) + s[i - 1])
            count = 1
        else:  # s[i] == s[i - 1].
            count += 1
    return ''.join(result)


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('6-11-run_length_compression.py',
                                       'run_length_compression.tsv',
                                       rle_tester))
