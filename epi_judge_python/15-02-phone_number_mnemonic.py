import itertools
from typing import List

from test_framework import generic_test, test_utils

"""
Leetcode: 17 https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Compute all  mnemonics for a phone number
Write a program which takes as input a phone number, specified as string of digits, and returns all possible characters sequences that corresponds to the phone number. 
Note: Imagine the digit to characters mapping in phone keypad. Each number will have upto 4 characters mapped
Time: Since loop give rise to 4 recursion, hence T(n) = 4T(n - 1) = O(4^n), so 3 digits number will have at most 4^2 combinations
    or anagrams
"""

# The mapping from digit to corresponding characters.
MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')


def phone_mnemonic_ori(phone_number: str) -> List[str]:
    def phone_mnemonic_helper(digit: int) -> None:
        if digit == len(phone_number):
            # All digits are processed, so add partial_mnemonic to mnemonics.
            # (We add a copy since subsequent calls modify partial_mnemonic.)
            mnemonics.append(''.join(partial_mnemonic))
        else:
            # Try all possible characters for this digit.
            for c in MAPPING[int(phone_number[digit])]:
                partial_mnemonic[digit] = c
                phone_mnemonic_helper(digit + 1)

    mnemonics: List[str] = []
    partial_mnemonic = ['0'] * len(phone_number)
    phone_mnemonic_helper(0)#index 0 passed
    return mnemonics

#my take
def phone_mnemonic(phone_number: str) -> List[str]:
    mnemonics: List[str] = []
    def phone_mnemonic_helper(numbers, partial_mnemonic) -> None:
        if len(numbers) == 0:
            mnemonics.append(partial_mnemonic)
        else:
            char = numbers[0]
            for c in MAPPING[int(char)]:
                phone_mnemonic_helper(numbers[1:], partial_mnemonic + c)
    phone_mnemonic_helper(phone_number, "")
    return mnemonics

# phone_mnemonic("23")

# Pythonic solution
def phone_mnemonic_pythonic(phone_number: str) -> List[str]:
    return [
        ''.join(mnemonic)
        for mnemonic in itertools.product(*(MAPPING[int(digit)]
                                            for digit in phone_number))
    ]


def phone_mnemonic_pythonic_another(phone_number: str) -> List[str]:
    table = {
        '0': '0',
        '1': '1',
        '2': 'ABC',
        '3': 'DEF',
        '4': 'GHI',
        '5': 'JKL',
        '6': 'MNO',
        '7': 'PQRS',
        '8': 'TUV',
        '9': 'WXYZ'
    }
    return [
        a + b for a in table.get(phone_number[:1], '')
        for b in phone_mnemonic_pythonic_another(phone_number[1:]) or ['']
    ]

#variant 1
"""without recursion
https://leetcode.com/problems/letter-combinations-of-a-phone-number/solution/884976
Logic:
    iterative DFS solution
    You create a empty stack. This stack will temporarily store the intermediate mneumonics and also the full mneumonics
    Length of the those intermediates will determine if further building is required or not
    Keep popping the items and append new characters to those untill desired length reached
    Simplest example: "2", stack will be filled with ['a', 'b', 'c']
    Why it is DFS, because it always start from left side of the tree, if you imagine the tree. It keeps on adding until
    it reaches the leaf(first valid anagram), then pops it, move to sibling and build it
"""
def phone_mnemonic_var(phone_number: str) -> List[str]:
    num_to_letters = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')
    stack = []
    answer = []
    num_length = len(phone_number)
    
    stack.append("")
    
    while len(stack) > 0:
        current = stack.pop()
        
        if len(current) == num_length:#stop building it further once decided length reached
            answer.append(current)
        else:
            current_num_index = len(current)
            num_letters = num_to_letters[int(phone_number[current_num_index])]
            for letter in num_letters:
                stack.append(current + letter)
                
    return answer

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            '15-02-phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
