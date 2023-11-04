import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

"""
Write a program to remove occurrences of b and replace occurrences of a with two ds. Size is given, process till the size.
"""
# dont worry about preserving subsequent characters after a and b have been dealt with
# first we delete bs and compute the final number of valid characters of the string, valid characters also include numbers of new 
# d's inserted. Do this in one single pass.
# then we replace  each a with 2 d's iterating backwards from the end of the resulting string from first operation
# Time O(n), space constant
def replace_and_remove(size: int, s: List[str]) -> int:

    # Forward iteration: remove 'b's and count the number of 'a's.
    #write index captures the characters not b

    write_idx, a_count = 0, 0
    for i in range(size):
        if s[i] != 'b':#removing b
            s[write_idx] = s[i]
            write_idx += 1
        if s[i] == 'a': #counting each a
            a_count += 1

    # Backward iteration: replace 'a's with 'dd's starting from the end.
    cur_idx = write_idx - 1 # this points to the last valid character
    write_idx += a_count - 1# adjusting write index for new enteries of d, this is the overall adjusted length of string
    final_size = write_idx + 1 #this will be the actual length of array when all a are replaced with d, after adjusting with size
    while cur_idx >= 0:#basically you are using cur_idx to scan each character, and using write_idx to recreate new array list
        if s[cur_idx] == 'a':
            s[write_idx - 1:write_idx + 1] = ['d']*2 # or ['dd']
            write_idx -= 2
        else:
            s[write_idx] = s[cur_idx]
            write_idx -= 1
        cur_idx -= 1
    return final_size

#practice 22MAY2022
def replace_and_remove_prac1(size: int, s: List[str]) -> int:
    write_idx, curr_idx, a_count = 0, 0, 0

    for i in range(size):
        if s[i] != 'b':
            s[write_idx] = s[i]
            write_idx += 1
        if s[i] == 'a':
            a_count += 1
    curr_idx = write_idx - 1
    final_size = write_idx + a_count
    write_idx = final_size - 1

    while curr_idx >= 0:
        if s[curr_idx] == 'a':
            s[write_idx - 1: write_idx + 1] = 2 * ['d']
            write_idx -= 2
        else:
            s[write_idx] = s[curr_idx]
            write_idx -= 1
        curr_idx -= 1

    return final_size

        
        

replace_and_remove_prac1(2, ['a', 'c','d','b','b','c','a'])  
# replace_and_remove(4, ['a', 'c','d','b','b','c','a'])
# replace_and_remove(7, ['a', 'c','d','b','b','c','a'])  

#variant
"""
You have an array C of characters. The characters may be letters, digits, blanks, and punctuations. The telex-encoding of the
array C is an array T of characters in which letters, digits, and blanks appear as before, but punctuation marks 
are spelled out. For example, character '.' is replaced with DOT, ',' is replace with COMMA, and etc
Design an algo to perform telex-encoding with O(1) space
Assumption: the original array is already large enough for the telex-encodings of punctuation to fit. Hence, overwriting
subsequent characters are allowed
"""

def telex_encoding(size: int, C: List[str]):
    punctuation = {
        ',': 'COMMA',
        '?': "QUESTION MARK",
        "." : "DOT",
        "!" : "EXCLAMATION MARK"
    }

    #lets count those punctuations to be replaced and overall size the array will be inflated to
    final_size = 0
    for i in C[:size]:
        if i in punctuation: # or ['.', ',', '?', '!']
            final_size += len(punctuation[i])
        else:
            final_size += 1
    write_idx = final_size - 1
    curr_idx = size - 1
    #lets start scanning for replacement, but from right
    while curr_idx >= 0:
        if C[curr_idx] in punctuation:
            length = len(punctuation[C[curr_idx]])
            C[write_idx - (length - 1):write_idx + 1] = punctuation[C[curr_idx]]
            write_idx -= length
        else:
            C[write_idx] = C[curr_idx]
            write_idx -= 1
        curr_idx -= 1
    return (C)


def telex_encoding_prac1(size: int, C: List[str]):
    punctuation = {
        ',': 'COMMA',
        '?': "QUESTION MARK",
        "." : "DOT",
        "!" : "EXCLAMATION MARK"
    }   

    final_size = 0
    for i in range(size):
        if C[i] in punctuation:
            final_size = final_size + len(punctuation[C[i]])
        else:
            final_size += 1
    curr_idx = size - 1
    write_idx = final_size - 1
    #now going from right side
    while curr_idx >= 0:
        if C[curr_idx] in punctuation:
            length = len(punctuation[C[curr_idx]])
            #replacing
            C[write_idx - (length - 1): write_idx + 1] = punctuation[C[curr_idx]]
            write_idx -= length
        else:
            C[write_idx] = C[curr_idx]
            write_idx -= 1
        curr_idx -= 1
    return C


telex_encoding_prac1(40, ['H', 'e', 'y', '!', ' ', 'J', 'a', 'y', 'a', 'n', 't', '.', ' ', 'H', 'o', 'w', ' ', 'a', 'r', 'e', ' ', 'y', 'o', 'u', '?', ' ', 'S', 'o', ',', ' ', 'w', 'h', 'e', 'n', ' ', 'w', 'i', 'l', 'l', ' ', 'y', 'o', 'u', ' ', 'b', 'e', ' ', 'r', 'e', 'a', 'd', 'y', '?', ' ', 'T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'g', 'r', 'e', 'a', 't', '.', ' ', 'O', 'v', 'e', 'r', 'w', 'r', 'i', 't', 'i', 'n', 'g', ' ', 'i', 's', ' ', 'a', 'l', 'l', 'o', 'w', 'e', 'd', '.', ' ', 'S', 'o', ' ', 'l', 'e', 't', 's', ' ', 'd', 'o', ' ', 'i', 't'])
telex_encoding(40, ['H', 'e', 'y', "!", ' ', 'J', 'a', 'y', 'a', 'n', 't', ' ', 'H', 'o', 'w', ' ', 'a', 'r', 'e', ' ', 'y', 'o', 'u', ' ', 'S', 'o', ' ', 'w', 'h', 'e', 'n', ' ', 'w', 'i', 'l', 'l', ' ', 'y', 'o', 'u', ' ', 'b', 'e', ' ', 'r', 'e', 'a', 'd', 'y', ' ', 'T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'g', 'r', 'e', 'a', 't', ' ', 'O', 'v', 'e', 'r', 'w', 'r', 'i', 't', 'i', 'n', 'g', ' ', 'i', 's', ' ', 'a', 'l', 'l', 'o', 'w', 'e', 'd', ' ', 'S', 'o', ' ', 'l', 'e', 't', 's', ' ', 'd', 'o', ' ', 'i', 't'])

@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('6-04-replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
