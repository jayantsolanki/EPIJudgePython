"""
WAP that multiply two arbitrary precsion integers
for example, [1,9,3,7,0,7,7,2,1] * [-7,6,1,8,3,8,2,5,7,2,8,7] = [-1,4,7,5,7,3,9,5,2,5,8,9,6,7,4,1,2,9,2,7]
Hint: use grade school mutliplication, one at a time
time complexity: O(nm)
"""
from typing import List

from test_framework import generic_test


def multiply(num1, num2):
    # TODO - you fill in here.
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0], = abs(num1[0]), abs(num2[0])

    result = [0] *(len(num1) + len(num2)) #atmost m+n, can be m+n-1 too, but m+n is safe bet
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10
            # print(f'i: {i}, j: {j}, sum: {i+j+1}, array: {result}')

    #remove the leading zeroes.
    result = result[next((i for i , x in enumerate(result)#enumerate gives you index too
                        if x != 0), len(result)):] or [0]
    """
    next(iterator[, default])

    Return the next item from the iterator. If default is given and the iterator
    is exhausted, it is returned instead of raising StopIteration.
    hence if all are zero, then it will be returned as [len(result):] which is [], [] or [0] becomes [0]
    """

    return [sign * result[0]] + result[1:]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('5-03-int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
