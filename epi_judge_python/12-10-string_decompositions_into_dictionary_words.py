import collections
from typing import List

from test_framework import generic_test

"""
Write aprogram which takes as input a string (sentence) and an array of string (words) and returns the starting indices 
of substrings of the sentence string which are the concaternation of all the strings in the words array. 
Each string must appear only once, their ordering is immaterial. All strings in words have equal length.
They may have duplicates.
Logic:
    Since the words size are fixed, we can directly check n size strings iteratively to see if they are in words as a prefix, if not we can discard them and move ahead with remainder of the strings left.
    Strategy:
        Create a function which receives the index to start searching from. It will have a for loop starting with that index
        and goes until the start + total length of the words array(total character count), step size is the length of each word.
        Maintain a counter which trackes the word if found and cross checks with a sepearate word counter to see 
        how many are needed. Return fales if counter exceeds or step size character doesnt match
Time: for each substring check we need to run loop untill size of words(total character) O(mN), m is length of word arrayand N is 
each word size. Also we scan each character in sentence of size n, so total Time is O(nmN)

"""
def find_all_substrings_original(s: str, words: List[str]) -> List[int]:
    def match_all_words_in_dict(start):
        curr_string_to_freq = collections.Counter()
        for i in range(start, start + len(words) * unit_size, unit_size):
            curr_word = s[i:i + unit_size]
            it = word_to_freq[curr_word]#since words can be repeated, get the count so as to make sure that limit is reached
            if it == 0:
                return False
            curr_string_to_freq[curr_word] += 1
            if curr_string_to_freq[curr_word] > it:
                # curr_word occurs too many times for a match to be possible.
                return False
        return True

    word_to_freq = collections.Counter(words)
    unit_size = len(words[0])
    return [
        i for i in range(len(s) - unit_size * len(words) + 1)
        if match_all_words_in_dict(i)
    ]

# find_all_substrings('amanaplanacanal', ['can', 'apl', 'ana'])
# find_all_substrings('amanaplanacanalanacanapl', ['can', 'apl', 'ana'])

#practice:

def find_all_substrings(s: str, words: List[str]) -> List[int]:
    result = []
    def find_substring_index(start):
        current_word_count = collections.Counter()
        #go until the size of the total words array (as in total characters, step size each word length)
        for index in range(start, start + len(words) * word_length, word_length):
            word = s[index:index+word_length]
            needed_count = word_counter[word]#counter returns zero if that word didnt exist in the word_counter
            # if needed_count == 0: #this is not needed
            #     return False
            current_word_count[word] += 1 
            if current_word_count[word] > needed_count:
                return False #either the word doesnt exist given array or it exceeded the total required count
        return True  

    word_counter = collections.Counter(words)   
    word_length = len(words[-1])
    # for index in range(0, len(s)):#this will work, but not important
    for index in range(0, len(s) - word_length * len(words) + 1):
        if find_substring_index(index):
            result.append(index)
    
    return result
# find_all_substrings('amanaplanacanal', ['can', 'apl', 'ana'])
# find_all_substrings('amanaplanacanalanacanapl', ['can', 'apl', 'ana'])

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            '12-10-string_decompositions_into_dictionary_words.py',
            'string_decompositions_into_dictionary_words.tsv',
            find_all_substrings))
