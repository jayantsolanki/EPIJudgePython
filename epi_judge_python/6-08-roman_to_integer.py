from test_framework import generic_test
import functools
"""
Roman to Decimal
"""
#write a program which takes as input a valid roman number string s and returns its integer
"""
I = 1
V = 5
X = 10
L = 50
C = 100 (Century)
D = 500
M = 1000
Exceptions allowed:
- I can immediately precede V and X #precede means minus
- X can immediately precede L and C
- C can immediately precede D and M
Back to back exceptions not allowed, eg: IXC is invalid as is CDM
Logic: Start from right to left. If the symbol after(right) the current one is greater than it, we subtract the current symbol
It does not check that when a smaller symbol appears to the left of a larger one that it is one of the six allowed excption
(We assumed that string provided will be devoid of exceptions)
Time: O(n)
"""
def roman_to_integer_original(s: str) -> int:

    T = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    return functools.reduce(
        lambda val, i: val + (-T[s[i]] if T[s[i]] < T[s[i + 1]] else T[s[i]]),
        reversed(range(len(s) - 1)), T[s[-1]])

#for my simple mind
def roman_to_integer_simple(s: str) -> int:

    T = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    val = 0
    for i in range(len(s)-1, -1, -1):
        if i+1 < len(s) and T[s[i]] < T[s[i+1]]:# if the symbol after(right) the current one is greater than it, we subtract
            val = val - T[s[i]]
        else:
            val = val + T[s[i]]
    return val

    # return functools.reduce(
    #     lambda val, i: val + (-T[s[i]] if T[s[i]] < T[s[i + 1]] else T[s[i]]),
    #     reversed(range(len(s) - 1)), T[s[-1]])

# roman_to_integer('LIX')
# roman_to_integer_simple('LIX')

#practice 22MAY2022
def roman_to_integer(s: str) -> int:
    val = 0
    T = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }

    for i in range(len(s) - 1, -1, -1):
        if i + 1 < len(s) and T[s[i]] < T[s[i + 1]]:
            val = val - T[s[i]]
        else:
            val = val + T[s[i]]
    return val

#variant
"""
Write a program that takes as input a string of Roman number symbols and checks whether that string is valid.
Roman numbers appear in non increasing order, but with following exception as mentioned in the above problem
Logic: Look for back to back exceptions and string is always non increasing if no exception there
"""

#using regex range 0 - 4000
# https://www.geeksforgeeks.org/validating-roman-numerals-using-regular-expression/
# https://stackoverflow.com/questions/267399/how-do-you-match-only-valid-roman-numerals-with-a-regular-expression
"""
Exceptions allowed:
- I can immediately precide V and X
- X can immediately proceed L and C
- C can immediately proceeed D and M
No digit is repeated in succession more than thrice, i.e., I, X and C cannot be repeated more than 3 times.
The digits V, L and D are not repeated. The repetition of V, L and D is invalid in the formation of numbers.
M{0,4} specifies the thousands section and basically restrains it to between 0 and 4000, 0000, 1000, 2000, ... 4000
 
(CM|CD|D?C{0,3}) this is for the hundreds section and covers all the possibilities, 000, 100, 200, ... 900
 
(XC|XL|L?X{0,3}) is for the tens place and covers all the possibilities , 00, 10, 20, 30, ,,, 90
 
Finally, (IX|IV|V?I{0,3}) is the units section. 0, 1, 2, 3,4,5,6,7,8,9 , ? same as{0,1}
"""
def ValidationOfRomanNumerals(s):
    if len(s) == 0:
        return False
    # Importing regular expression
    import re
     
    # Searching the input string in expression and
    # returning the boolean value
    #regex is in non increasing pattern
    print(bool(re.search(r"^M{0,4}(CM|CD|D{0,1}C{0,3})(XC|XL|L{0,1}X{0,3})(IX|IV|V{0,1}I{0,3})$",s)))#using three exceptions

ValidationOfRomanNumerals("MCCXXXVIII")
ValidationOfRomanNumerals("MXCCXXXVIII") 
ValidationOfRomanNumerals("MMMCM") 
ValidationOfRomanNumerals("IXC")
ValidationOfRomanNumerals("XC")
ValidationOfRomanNumerals("CDM")
ValidationOfRomanNumerals("MCXCC")# correct is MCXC

# variant 2
"""
https://leetcode.com/problems/integer-to-roman/
write a program that takes as input a positive integer n and returns a shortest valid roman number in string form
Logic: create val and syb which will be use for mapping int values to roman values. after that take int values one by one and check how many of those will fit in input value, and add that amount of roman nums to result, and remove the added value from input and repeat the process until zero.
Actual range 1 - 3999
"""
def int_to_Roman(num):# this also gives the shortest one
   val = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)# rest others not in here will be repeated, like III
   # or XX or CC
   syb = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
   roman_num = ""
   for i in range(len(val)):
      count = int(num / val[i])#will be zero if num less than val[i]
      roman_num += syb[i] * count# nice
      num -= val[i] * count
    #   if num == 0:
    #       break
   return roman_num

int_to_Roman(59)
int_to_Roman(3900)
int_to_Roman(8000) # actual answer should be VIII with a dash on its top 

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('6-08-roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
