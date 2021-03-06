from functools import cache, lru_cache
from test_framework import generic_test

"""
Leetcode 72. Edit Distance
https://leetcode.com/problems/edit-distance/
Write a program that takes two strings and computes the minimum number of edits needed to transform the first string
to second string. Edits are remove, replace, insert
Logic:
    Similar to longest common subsequence, here we do the above three operations and find the min

Time and Space: O(mn)
"""
def levenshtein_distance_ori(A: str, B: str) -> int:
    @lru_cache(None)
    def compute_distance_between_prefixes(A_idx, B_idx):
        if A_idx < 0:
            # A is empty so add all of B's characters.
            return B_idx + 1
        elif B_idx < 0:
            # B is empty so delete all of A's characters.
            return A_idx + 1

        if A[A_idx] == B[B_idx]:
            return compute_distance_between_prefixes(A_idx - 1, B_idx - 1)

        substitute_last = compute_distance_between_prefixes(
            A_idx - 1, B_idx - 1)
        add_last = compute_distance_between_prefixes(A_idx, B_idx - 1)
        delete_last = compute_distance_between_prefixes(A_idx - 1, B_idx)
        return 1 + min(substitute_last, add_last, delete_last)

    return compute_distance_between_prefixes(len(A) - 1, len(B) - 1)

#my fav
#top down approach, similar to approach in longest common subsequence
def levenshtein_distance_mem(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    @cache
    def dp(i, j):
        if i == m and j == n:#this is the target
            return 0
        elif i == m:# unexpected end, that means rest of the characters needs to be added from word2
            return n - j #important
        elif j == n:# unexpected end, that means rest of the characters needs to be removed from word 1
            return m - i # #important
        else:
            if word1[i] == word2[j]:
                return dp(i + 1, j + 1)
            else:
                return min(dp(i + 1, j), dp(i + 1, j + 1), dp(i, j + 1)) + 1 #delete, replace and insert, respectively
    return dp(0, 0)


#bottom up, my way
# O(mn) for time and space
def levenshtein_distance_iter(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    cache = [[0] * (n+1) for _ in range(m + 1)] #contains emty string clause too
    #setting base cases, that is number of changes needs for converting empty strings to other word
    
    for i in range(m+1):#first column
        cache[i][0] = i
    for j in range(n+1): #top row
        cache[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]: # if same characters, also why i - 1 and j - 1, since starting from 1
                cache[i][j] = cache[i - 1][j - 1] #no changes required, hence copy changes from last character
            else:
                cache[i][j] = 1 +min(cache[i - 1][j], cache[i - 1][j - 1], cache[i][j - 1]) # delete, replace, insert
    
    return cache[m][n]

#variant 1
"""
Compute distance in O(min(m,n)) space and O(mn) time"""
#bottom up, improved space O(min(m, n))
def levenshtein_distance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    #making sure n is the smallest one, hence word2 too
    if m < n:
        word1, word2 = word2, word1
        m, n = n, m

    cache = [0] * (n + 1)
   
    for i in range(m + 1):
        temp_row = cache[:]
        for j in range(n + 1):
            # print(i, j, m, n, len(cache))
            if i == 0: #important
                cache[j] = j  # Need to insert `j` chars to become word2[:j]
            elif j == 0:
                cache[j] = i  # Need to delete `i` chars to become ""
            elif word1[i - 1] == word2[j - 1]: # if same characters, also why i - 1 and j - 1, since index starting from 1
                cache[j] = temp_row[j - 1]
            else:
                cache[j] = 1 + min(temp_row[j], temp_row[j - 1], cache[j - 1])
    return cache[-1]
    
#varian2
"""
Leetcode: 1143. Longest Common Subsequence
https://leetcode.com/problems/longest-common-subsequence/
Find Longest Common Subsequence
"""
#topdown
def longestCommonSubsequence_cached(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2) 
    @cache
    def dp(i, j):
        if i == m or j == n:
            return 0

        elif text1[i] == text2[j]:
            return dp(i+1, j+1) + 1
        else:
            return max(dp(i + 1, j), dp(i, j + 1))
    return dp(0, 0)

longestCommonSubsequence_cached("Carthorse", "Orchestra")
#bottom up
def longestCommonSubsequence_b2(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2) 
    cache = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                cache[i][j] = 1 + cache[i - 1][j - 1]
            else:
                cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])
    print(cache)
    return cache[m][n]
longestCommonSubsequence_b2("Carthorse", "Orchestra")
longestCommonSubsequence_b2("abcde", "ace")

#this returns the actual subsequence
def longestCommonSubsequence_b2_seq(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2) 
    cache = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                cache[i][j] = 1 + cache[i - 1][j - 1]
            else:
                cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])
    #to generate the sequence, just follow the trace
    char_array = []
    i, j = m, n 
    while True:
            if i == 0 or j == 0:
                break
            if text1[i - 1] == text2[j - 1]:
                char_array.append(text1[i - 1])
                i , j = i - 1, j - 1
            else:
                if cache[i - 1][j] > cache[i][j - 1]:
                    i = i - 1
                else:
                    j = j - 1


    return "".join(reversed(char_array))
longestCommonSubsequence_b2_seq("Carthorse", "Orchestra")
longestCommonSubsequence_b2_seq("abcde", "ace")

#variant 3
"""
https://leetcode.com/problems/longest-palindromic-subsequence/discuss/99151/Super-simple-solution-using-reversed-string
Since it says minimum, that means longest palindrome
516. Longest Palindromic Subsequence
https://leetcode.com/problems/longest-palindromic-subsequence/
Given a string A, compute the minimum number of deletions from A  to make it the result string a palindrome
Logic:
    LCS of s and reverse(s) is the longest subsequence palindrome of s.
    What you are trying to while reversing the string is trying to find the same string in another string.
"""
def PalindromiclongestCommonSubsequence_b2_seq(text1: str) -> int:
    text2 = text1[::-1]
    m, n = len(text1), len(text2) 
    cache = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                cache[i][j] = 1 + cache[i - 1][j - 1]
            else:
                cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])
    #to generate the sequence, just follow the trace
    char_array = []
    i, j = m, n 
    while True:
            if i == 0 or j == 0:
                break
            if text1[i - 1] == text2[j - 1]:
                char_array.append(text1[i - 1])
                i , j = i - 1, j - 1
            else:
                if cache[i - 1][j] > cache[i][j - 1]:
                    i = i - 1
                else:
                    j = j - 1

    return "".join(reversed(char_array)), len(text1) - len(char_array)
PalindromiclongestCommonSubsequence_b2_seq("carthorse")
PalindromiclongestCommonSubsequence_b2_seq("abcde")

#variant 4
# Regenrate the string which is closest to given string, provided that levenshtein distance is given

# Variant 5
"""
Leetcode: 97. Interleaving String
https://leetcode.com/problems/interleaving-string/
Define a string t to be an interleaving of strings s1 and s2 if there is a way to interleave the characters of s1 and s2, 
keeping the left-to-right order of each, to obtain t.
Design an algorithm that takes as input strings s1, s2 and t, and determines if t is an inteleaving of s1 and s2
#Time and Space Complexity: O(m * n)
"""
def isInterleave(s1: str, s2: str, s3: str) -> bool:
    
    m, n, t = len(s1), len(s2), len(s3)
    
    if m + n != t:
        return False
    @cache
    def dp(i, j, res):
        if res == s3 and i == m and j == n:
            return True
        # elif i == m:
        #     return False
        # elif j == n:
        #     return False
        else:
            # ans = dp(i + 1, j, res + s1[i]) | dp(i, j + 1, res + s2[j])
            ans =  False
            if i < m and s1[i] == s3[i + j]: # added extra pruning, checking if the character at ith matches i+j in s3
                ans |= dp(i + 1, j, res + s1[i])
            if j < n and  s2[j] == s3[i + j]:
                ans |= dp(i, j + 1, res + s2[j])
            return ans
    
    return dp(0, 0, "")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('16-02-levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
