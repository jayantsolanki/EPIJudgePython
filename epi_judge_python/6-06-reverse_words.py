from audioop import reverse
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# reverse all words in a sentence, alice like bob becomes bob like alice
# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
#logic: difficult to solve in one pass, needs two passes
# in first pass, just reverse the whole array
#in second pass, identify each word , and its word boundary, then reverse them
#basically reverse th3e whole srting first, then reverse indiviual words
# time : O(n), space O(1)
def reverse_words_original(s):
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


# practice 22MAY2022
def reverse_words(s):

    def reverse_string(start, finish, s):
        while start < finish:
            #exchange characters
            s[start], s[finish] = s[finish], s[start]
            start, finish = start + 1, finish - 1
    reverse_string(0, len(s) - 1, s)#first reverse the string
    start = 0
    finish = 0
    while True:
        #now reverse the word by word
        finish = start #move the tracker finish to start position, start will change after space is encountered
        #search the blank
        while finish < len(s):
            if s[finish] == ' ':
                break
            finish = finish + 1
        if finish == len(s):#first check why the while loop broke, is it the end of string
            reverse_string(start, finish - 1, s)
            break
        reverse_string(start, finish - 1, s)
        start  = finish + 1
    # reverse_string(start, finish - 1, s)

@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('6-06-reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
