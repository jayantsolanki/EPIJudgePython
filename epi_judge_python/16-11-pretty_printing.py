from functools import cache
import typing
from typing import List
from test_framework import generic_test

 ###################### Discarded #############################
"""
The pretty printing problem
Given text that is  a string of words separated by single blanks, decompose the text into lines such 
that no word is split across lines and the messiness of the decomposition is minimized. 
Each lines hold no more than a specified number of characters.
Messiness of a single with b blank characters is b**2. Total messiness is sum of messines of each line.
Logic:
    You focus on last word and the last line. Start from there, and start minimizing the messiness value.
    In the optimum placement of the first i words, the last line consists of some subset of words ending in the ith word.
    Furthermore, since the first i words are assumed to be optimally placed, the placement of words on the lines
    prior to the last one must be optimum. Therefore, we can write a recursive formula for the minimum messines, M(i),
    when placing the first i words. Specifically M(i) = min(f(i, j) + M(j - 1)), where f(i, j) is the messiness of a
    single line consisting of words j to i inclusive. 
Time complexity: O(nL), where L is length of line, n is words array size
Space: O(n)
"""
def minimum_messiness(words: List[str], line_length: int) -> int:

    num_remaining_blanks = line_length - len(words[0])
    # min_messiness[i] is the minimum messiness when placing words[0:i + 1].
    min_messiness = ([num_remaining_blanks**2] +
                     [typing.cast(int, float('inf'))] * (len(words) - 1))
    for i in range(1, len(words)):
        num_remaining_blanks = line_length - len(words[i])#initial blanks spaces
        min_messiness[i] = min_messiness[i - 1] + num_remaining_blanks**2 #cumulative sum
        # Try adding words[i - 1], words[i - 2], ...
        for j in reversed(range(i)):#trying to minimize the messiness by adding more words to that line i
            num_remaining_blanks -= len(words[j]) + 1
            if num_remaining_blanks < 0:
                # Not enough space to add more words.
                break
            first_j_messiness = 0 if j - 1 < 0 else min_messiness[j - 1] #edge case for index j == 0
            current_line_messiness = num_remaining_blanks**2
            min_messiness[i] = min(min_messiness[i],
                                   first_j_messiness + current_line_messiness)
    return min_messiness[-1]



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('16-11-pretty_printing.py',
                                       'pretty_printing.tsv',
                                       minimum_messiness))
