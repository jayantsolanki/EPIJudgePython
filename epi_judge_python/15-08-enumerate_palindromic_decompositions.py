from typing import List

from test_framework import generic_test

"""
Leetcode: https://leetcode.com/problems/palindrome-partitioning/
131. Palindrome Partitioning

Compute all the palindromic decomposition of a given string. For example, for string = "aab"
there can be many ways it can be decomposed, all decomposition are [['a', 'a', 'b'], ['a', 'ab'], ['aa', 'b'], ['aab']] but,
only [["a","a","b"],["aa","b"]] are palindromic decompositions.

example = "abc"
For n size string there are n-1 slots to choose from for partition boundary
for string of size n = 3, there are 3-1 slots to put partition, we can have partition/decomposition (|) at a|bc or ab|c, 
here we are putting only | at a time = total ways=  2c1 = 2
for string of size n =3, we have partition/decomposition (|) at a|b|c, here we are putting only 2 at a time, total = 2c2 = 1
for string of size n =3, we have partition/decomposition (|) at abc, here we are putting only 0 at a time 2c0 = 1
Total ways to parition = 2c1 + 2c2 + 2c0 or 2c0 + 2c1 + 2c2 = 2^2
Generalizing for n size string = (n-1)C0 + (n-1)C1 + (n-1)C2 + ... (n-1)C(n-1) = 2^(n-1) ways to partition

Logic:
    First thing is that you should know how to decompose a string correctly, below code (decompositions) does that.
        In order to decompose, you should start with index 0, then keep on increasing the index in a for loop, variable is 'end'
        Store the substring formed using text[start:end+1]
        Inside the loop, call the backtrack method by passing the substring array and the end + 1. Repeat
        Base case: when start reaches length of text, stop and append the result
        Use this image for visualization: blob:https://leetcode.com/cf16d90c-d054-48cd-95a5-59cb637e6ef1

    So during each substring genreation, check if that is palindrome, if not, backtrack to top.
Time: See this: https://leetcode.com/problems/palindrome-partitioning/solution/1195630
Since decomposisiton forms a n-ary tree, hence O(n*2^n), reference: https://leetcode.com/problems/palindrome-partitioning/Figures/131/time_complexity.png

https://stackoverflow.com/questions/24591616/whats-the-time-complexity-of-this-algorithm-for-palindrome-partitioning
Should be O(n*2^n). You are basically trying out every possible partition out there. For a string with length n, you will have 2^(n - 1) ways to partition it. This is because, a partition is equivalent of putting a "|" in b/t two chars. There are n - 1 such slots to place a "|". There are only two choice for each slot - placing a "|" or not placing a "|". Thus 2^(n - 1) ways to place "|"s.



there could be 2^{N} possible substrings in the worst case. For each substring, it takes O(N) time to generate substring and determine if it a palindrome or not. This gives us time complexity as O(n*2^n).


For a string of size N the recursive method will recur for substrings of size N-1, N-2, N-3 and so on. This can be written as,

T(N) = T(N-1) + T(N-2) + ... + T(1)T(N)=T(N−1)+T(N−2)+...+T(1).

Similarly, T(N - 1) can be written as,

T(N - 1) = T(N-2) + T(N-3) + ... + T(1)T(N−1)=T(N−2)+T(N−3)+...+T(1)

Subtracting the above 2 expressions and solving the expression, we get,

T(N) = 2T(N-1)T(N)=2T(N−1)

The time complexity of above recurrence relation is given by,

T(N) = O(2^N)
Additionally, to check if a substring is a palindrome or not we must iterate O(N/2) times within each recursive call
So overall: O(N*2^N)
Space: O(2^n)
"""
def decompositions(text: str) -> List[List[str]]:
    result = []
    def backdoor(start, curr):
        if start == n:
            result.append(curr[:])
            return
        for end in range(start, n):
            curr.append(text[start:end + 1])
            backdoor(end+1, curr)
            curr.pop()
    n = len(text)
    backdoor(0, [])
    return result

decompositions("abcd")

#my take
#helper
def is_palindromic(s: str) -> bool:
    return all([s[i] == s[~i] for i in range(len(s)//2)])

def palindrome_decompositions_with_array_curr(text: str) -> List[List[str]]:
    result = []
    def backdoor(start, curr):
        if start == n:
            result.append(curr[:])
            return
        for i in range(start, n):
            substring = text[start:i + 1]
            if substring == substring[::-1]:#checking if it is a palindrome, interestingly this seems faster, then below
            # if is_palindromic(substring):
                curr.append(substring)
                backdoor(i+1, curr)
                curr.pop()
    n = len(text)
    backdoor(0, [])
    return result

#not using array in this (curr), a bit faster, so no need for using pop
def palindrome_decompositions(text: str) -> List[List[str]]:
    result = []
    def backdoor(start, curr):
        if start == n:
            result.append(curr[:])
            return
        for i in range(start, n):
            substring = text[start:i + 1]
            if substring == substring[::-1]:#checking if it is a palindrome, interestingly this seems faster, then below
            # if is_palindromic(substring):
                # curr.append(substring)
                backdoor(i+1, curr + [substring])
                # curr.pop()
    n = len(text)
    backdoor(0, [])
    return result
# palindrome_decompositions("aab")

#from book


def palindrome_decompositions_ori(text: str) -> List[List[str]]:
    def directed_palindrome_decompositions(offset, partial_partition):
        if offset == len(text):
            result.append(partial_partition.copy())
            return

        for i in range(offset + 1, len(text) + 1):
            prefix = text[offset:i]
            if prefix == prefix[::-1]:
                directed_palindrome_decompositions(
                    i, partial_partition + [prefix])

    result: List[List[str]] = []
    directed_palindrome_decompositions(offset=0, partial_partition=[])
    return result


# Pythonic solution uses bottom-up construction.
def palindrome_decompositions_pythonic(text: str) -> List[List[str]]:
    return ([[text[:i]] + right
             for i in range(1,
                            len(text) + 1) if text[:i] == text[:i][::-1]
             for right in palindrome_decompositions_pythonic(text[i:])]
            or [[]])

def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            '15-08-enumerate_palindromic_decompositions.py',
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))
