from test_framework import generic_test

"""
Write a program that returns nth integer in the look-and-say problem
In this problem, series start with 1, then subsequent numbers are literally derived
by describing the previous number in the series, in terms of consecutive digits.
Read of the digits in previous entry,count them in group of same type. Next number genreated by looking at previous
[1, 11, 21, 1211, 111221, 312211, so on], second item 11 is pronunced as one 1; similarly
21 -> two 1s etc
Logic: we compute the nth item by iteratively applying the above rule n-1 times
Time: O(n2^n); since each successive item can have twice as much as digit compared to previous
Hence, you have to go through n iteration, then in each iteration, expect twice the digits 
"""
def look_and_say_original(n: int) -> str:
    def next_number(s):
        result, i = [], 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                i += 1
                count += 1
            result.append(str(count) + s[i])
            i += 1
        return ''.join(result)#returning the array as a string

    s = '1'
    for _ in range(1, n):# 1 to n - 1, we already included zero
        s = next_number(s)
    return s

# practice 22MAY2022

def look_and_say(n: int) -> str:
    def next_number(word):
        i = 0
        result = []#counts the number of each unique digit
        while i < len(word):
            count = 1
            while i+1 < len(word) and word[i] == word[i + 1]:
                i = i + 1
                count += 1
            result.append(str(count) + word[i])
            i = i + 1
        return "".join(result)
    
    s = '1'
    for _ in range(1, n):
        s = next_number(s)
    return s


look_and_say(7)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('6-07-look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
