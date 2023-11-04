import functools
from test_framework import generic_test

"""
Given two string s (keyword string) and t (the text to be searched in), find the first occurrence of s in t.
Sliding window problem
"""

#brute force O(n^2)

def rabin_karp_brute(t: str, s: str) -> int:

    for i in range(len(t)):
        match = True
        local_index = i
        for j in range(len(s)):
            #also check whether you are nearing end of t
            if local_index == len(t) or s[j] != t[local_index]:
                match = False
                break
            else:#if character matches
                local_index += 1
        if match:#returns first occurence of match
            return i
    return -1

# time O(m + n)
# https://riptutorial.com/algorithm/example/24653/introduction-to-rabin-karp-algorithm
#my formula has MSB starting with 0, instead of m - 1 power
def rabin_karp(t: str, s: str) -> int:    
    pattern_len = len(s)
    if pattern_len > len(t):
        return -1
    prime_num = 11 #i am taking 11 instead of 10 or 26
    Ts_hash = sum([ ord(s[i]) * (prime_num ** i) for i in range(pattern_len)])
    Tt_hash = sum([ ord(t[i]) * (prime_num ** i) for i in range(pattern_len)])

    for i in range(pattern_len, len(t) + 1):#need to run at least one time
        # Checks the two substrings are actually equal or not, to protect
        # against hash collision.
        if Ts_hash == Tt_hash and t[i - pattern_len:i] == s:
            # print("i ran")
            return i - pattern_len
        elif i < len(t): #protection against index error
            #now calculate rolling hash
            first_char = ord(t[i - pattern_len])
            Tt_hash = (Tt_hash - first_char) // prime_num + (ord(t[i]) * prime_num ** (pattern_len - 1))
            # (Tt_hash - first_char) // prime_num because Tt_hash = a + b*prime + c * prime**2 + d * prime ** 3 ..., 
            # hence for rolling, we need to remove a first
            #then divide by prime the remaining, so as to reduce the power, 
            # New hash = (b + c * prime + d * prime ** 2) + e * prime **3
    return -1

# rabin_karp("FOOBAR", "BAR")
# rabin_karp("FOOBARWIDGET", "WIDGETS")

def rabin_karp_ori(t: str, s: str) -> int:

    if len(s) > len(t):
        return -1  # s is not a substring of t.

    base = 26
    # Hash codes for the substring of t and s.
    t_hash = functools.reduce(lambda h, c: h * base + ord(c), t[:len(s)], 0)
    s_hash = functools.reduce(lambda h, c: h * base + ord(c), s, 0)
    power_s = base**max(len(s) - 1, 0)  # base^|s-1|.

    for i in range(len(s), len(t)):
        # Checks the two substrings are actually equal or not, to protect
        # against hash collision.
        if t_hash == s_hash and t[i - len(s):i] == s:
            return i - len(s)  # Found a match.

        # Uses rolling hash to compute the hash code.
        t_hash -= ord(t[i - len(s)]) * power_s
        t_hash = t_hash * base + ord(t[i])

    # Tries to match s and t[-len(s):].
    if t_hash == s_hash and t[-len(s):] == s:
        return len(t) - len(s)
    return -1  # s is not a substring of t.



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('6-12-substring_match.py',
                                       'substring_match.tsv', rabin_karp))
