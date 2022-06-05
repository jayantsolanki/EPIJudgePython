from test_framework import generic_test
import collections

"""
Design an algo which takes text from an anon letter and text from a magazine and determines if it is possible to write the 
anon letter using text from magazine. Each character in anon letter must have count lesses or equal to its corresponding 
counting in magazine
Logic:
    Make single pass over the letter, creating the character count in a hashtable.
    Now, make a pass over the magazine, if processing the character c, reduce its count in hashmap by one, remove it from hastable if count becomes zero
    If hash table get empty during the pass, return True
    If hash table remains there after end of pass, return False

Note: Check the pythonic solution
Time: Worstcase O(m + n), m and n are size of letter and magazine
Space: O(L), L is total unique characters in Letter
"""
def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:

    # Compute the frequencies for all chars in letter_text.
    char_frequency_for_letter = collections.Counter(letter_text)

    # Checks if characters in magazine_text can cover characters in
    # char_frequency_for_letter.
    for c in magazine_text:
        if c in char_frequency_for_letter:
            char_frequency_for_letter[c] -= 1
            if char_frequency_for_letter[c] == 0:
                del char_frequency_for_letter[c]
                if not char_frequency_for_letter:
                    # All characters for letter_text are matched.
                    return True

    # Empty char_frequency_for_letter means every char in letter_text can be
    # covered by a character in magazine_text.
    return not char_frequency_for_letter

# Pythonic solution that exploits collections.Counter. Note that the
# subtraction only keeps keys with positive counts.
def is_letter_constructible_from_magazine_pythonic(letter_text: str,
                                                   magazine_text: str) -> bool:
    # you can actually add or subtract two or more counters, check page 174
    return (not collections.Counter(letter_text) -
            collections.Counter(magazine_text))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
        '12-02-is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
