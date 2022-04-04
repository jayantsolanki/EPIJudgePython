import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
#logic: difficult to solve in one pass, needs two passes
# in first pass, just reverse the whole array
#in second pass, identify each word , and its word boundary, then reverse them
# time : O(n), space O(1)
def reverse_words(s):
    def reverse_range(s, start, finish):# main work function for reversing
        while start < finish:
            s[start], s[finish] = s[finish], s[start]
            start, finish = start + 1, finish - 1

    # First, reverse the whole string.
    reverse_range(s, 0, len(s) - 1)

    start = 0
    while True:
        finish = start
        while finish < len(s) and s[finish] != ' ':#identify word boundary
            finish += 1
        if finish == len(s):
            break
        # Reverses each word in the string.
        reverse_range(s, start, finish - 1)
        start = finish + 1
    # Reverses the last word. because it has no space to end with
    reverse_range(s, start, len(s) - 1)


# Pythonic solution, doesn't reverse in-place, may be used with strings, just strings
def reverse_words_pythonic(s):
    return ' '.join(reversed(s.split(' ')))



@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('6-06-reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
