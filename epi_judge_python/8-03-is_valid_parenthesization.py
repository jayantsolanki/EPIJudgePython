from test_framework import generic_test

#leetcode 20 https://leetcode.com/problems/valid-parentheses/
# write a program that tests if a string made up of '(', ')'. '[', ']', '{', '}' is well formed
#example: "([]){()}" is  well formed expression
#logic: starting from left, every time we see a left type of string, we store it in stack
# and when we see a right form of string, we match it with stack and take it out
#time complexity is O(n) since for each character we perform O(1) operations

def is_well_formed_original(s: str) -> bool:

    left_chars, lookup = [], {'(': ')', '{': '}', '[': ']'}#excellent
    for c in s:
        if c in lookup:#only take left types  of brackets, squares, curlies
            left_chars.append(c)
        elif not left_chars or lookup[left_chars.pop()] != c: # if list is empty or doesnt match with one popped up
            # Unmatched right char or mismatched chars.
            return False
    return not left_chars # return true if empty
#simple
def is_well_formed(s: str) -> bool:

    left_chars, lookup = [], {'(': ')', '{': '}', '[': ']'}#excellent
    for c in s:
        if c in lookup:#only take left types  of brackets, squares, curlies
            left_chars.append(c)
        elif not left_chars:# if list is empty, and character is some other or right ones
            # Unmatched right char or mismatched chars.
            return False
        elif lookup[left_chars.pop()] != c: # if list is not empty and doesnt match with one popped up
            # Unmatched right char or mismatched chars.
            return False
    return not left_chars # return true if empty list

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('8-03-is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
