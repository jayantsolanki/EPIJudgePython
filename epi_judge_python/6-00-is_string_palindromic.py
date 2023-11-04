from test_framework import generic_test

"""
Wap that checks whether a string is palindromic or not.
Time: O(n), Space: O(1)
"""
def is_palindromic(s: str) -> bool:
    return all([s[i] == s[~i] for i in range(len(s)//2)])



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('6-00-is_string_palindromic.py',
                                       'is_string_palindromic.tsv',
                                       is_palindromic))
