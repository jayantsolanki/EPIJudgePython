from test_framework import generic_test

#check book for notes
"""
Define the snakestring of s to be the left-right top-to-bottom sequence in which characters appear when s is written in sinusoidal fashion. For example, the snakestring string for "Hello-World!" is "e-lHloWrdlo!", - is the space.
Write a program which takes as input a string s and retums the snakestring of s.
O(n)time
"""
def snake_string(s: str) -> str:

    result = []
    # Outputs the first row, i.e., s[1], s[5], s[9], ...
    for i in range(1, len(s), 4):
        result.append(s[i])
    # Outputs the second row, i.e., s[0], s[2], s[4], ...
    for i in range(0, len(s), 2):
        result.append(s[i])
    # Outputs the third row, i.e., s[3], s[7], s[11], ...
    for i in range(3, len(s), 4):
        result.append(s[i])
    return ''.join(result)

snake_string("Hello World")


# Python solution uses slicing with right steps.
def snake_string_pythonic(s):
    return s[1::4] + s[::2] + s[3::4]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('6-10-snake_string.py', 'snake_string.tsv',
                                       snake_string))
