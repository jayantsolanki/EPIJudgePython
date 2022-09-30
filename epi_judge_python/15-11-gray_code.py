import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

"""
Leetcode: 89. Gray Code
https://leetcode.com/problems/gray-code/
Write out Gray Codes for n = 2, 3, 4
An n-bit gray code sequence is a sequence of 2n integers where:

    Every integer is in the inclusive range [0, 2n - 1],
    The first integer is 0,
    An integer appears no more than once in the sequence,
    The binary representation of every pair of adjacent integers differs by exactly one bit, and
    The binary representation of the first and last integers differs by exactly one bit.

the answer for n = 3 will be [0,1,3,2,6,7,5,4] # [000, 001, 011, 010, 110, 111, 101, 100], 2^n total items
Logic:
We build the series incrementally, adding a value only if it is distinct from all other currently in the series and 
    differs in exactly one place with the previous value. For last place , we have to check that it differs with first value
    in one place.

    We begin wil zero 000, next we try changing the bit at 0th position, if the new value not in series, add it
    Next we try to change the value of result[-1], at the 0th position, if value already there, we try to change the bit
    at 1st position, and add to result if not in the result already. We can backtrack of not of the ith position changes
    satisfy the differ_by_one criteria. We go on.
    Beauty of using for loop and history variable is that we pick only the valid elements one by one. This way we dont
    unnecessarily brute force
Time: O(n*2^n), since we need to pick 0 or 1 for ith position. In our backtracking algorithm, at every function call we iterate over a loop of length nn and try to find out all possible successors of the last added number in the present sequence.
Total n times. 
Space: O(2^n),  The maximum depth of the recursive function stack is 2^n (The recursion stops when the size of result list is 2^n).

"""

def gray_code_ori(num_bits: int) -> List[int]:
    def directed_gray_code(history):
        def differs_by_one_bit(x, y):
            bit_difference = x ^ y #
            return bit_difference and not (bit_difference &
                                           (bit_difference - 1))# x & (x-1) set  first 1 bit to zero, incase there is only 1 1bit 
                                           #it will return zero. so if two digit differs by 1 bit, bitt_difference will contain
                                           # only one instance of 1 bit, hence bit_difference & (bit_difference - 1) = 0

        if len(result) == 1 << num_bits:
            # Check if the first and last codes differ by one bit.
            # print(history)#history will be also of same size as that of result
            return differs_by_one_bit(result[0], result[-1])
        #we build series incrementaly 
        for i in range(num_bits):#this loop changes the bit at ith place
            previous_code = result[-1]
            candidate_next_code = previous_code ^ (1 << i)#switches the digit at ith position
            if candidate_next_code not in history:
                history.add(candidate_next_code)
                result.append(candidate_next_code)
                #now move to subsequent item in the series
                if directed_gray_code(history):#it will trigger again and again, since we need to find consecutive numbers which differs by 1 bit, if a partial series 
                    #isnt then we rollback and try with another bit place
                    return True
                del result[-1]
                history.remove(candidate_next_code)
        return False

    result = [0] # the reason we dont use set for storing result is that order of insertedr element in set is not ordered
    directed_gray_code(set([0]))#benefit of using set is that searching for item will be easy
    return result


#method 2
#recursion using mirroring
"""
Inspiration comes from small mirror imaging. The sequence 00, 01, 11, 10 is a 2-bit Gray codes. To get  n = 3,
we prepend 1 to reverse of the 2bit series.000, 001, 011, 010, 110, 111, 101, 100. (this is exactly mirror image)
See this: https://www.allaboutcircuits.com/technical-articles/gray-code-basics/#:~:text=What%20are%20Gray%20Codes%3F,submittal%20on%20Pulse%20Code%20Communication.
For example the Gray code sequence for n = 3 is [000, 001, 011, 010, 110, 111, 101, 100] (G(3)). This sequence can be obtained from the sequence [00, 01, 11, 10](say G(2)) for n = 2 as follows :

Add 0 to the (n - 1)th position (0 based indexed, the 2nd bit from the right) to the entire sequence 
of G(2). [00, 01, 11, 10] -> [000, 001, 011, 010] (G(3a)).

Reverse G(2) sequence and add 1 (1 << n - 1) to the (n - 1)th position (the 2nd bit from the right) [00, 01, 11, 10] -> 
[10, 11, 01, 00] -> [110, 111 101, 100] (G(3b)).

Concatenate G(3a) and G(3b) to get the Gray code sequence for n = 3 (G(3)) : [000, 001, 011, 010, 110, 111, 101, 100]


Time: T(n) = T(n-1) + O(2^(n-1)), O(2^n)
Space complexity: O(n), We start from n and continue our recursive function call until our base condition n = 0n=0 is reached. 
Thus, the depth of the function call stack will be O(n). The space occupied by the output result is not 
considered in the space complexity analysis. All 2^n numbers are added to the same list. At every function call, we iterate over the list, and at each iteration, we add a new number to the sequence. Thus, the size of the list result at the end of a function call is twice its size at the previous function call.


"""
#bottom -up
def gray_code_recursion2(num_bits: int) -> List[int]:
    if num_bits ==0:
        return [0]
    
    # These implicitly begin with 0 at bit_index (num_bits -1)
    gray_code_num_bits_minus_1 = gray_code_recursion2(num_bits - 1)
    # now, add a 1 at bit -index (num_bits - 1) to all entries in gray_code_num_bits_minus_1
    leading_bit_one = 1 << (num_bits - 1)
    # Process in reverse order to achieve reflection of gray_code_num_bits_minus_1
    return gray_code_num_bits_minus_1 + [
        leading_bit_one | i for i in reversed(gray_code_num_bits_minus_1)
    ]  

gray_code_recursion2(2)

#my take, simple to understand,  my favorite, top down
def gray_code(num_bits: int) -> List[int]:
    def gray_code_gen(n, result):
        if n == num_bits:
            return result
        result = result + [ x | (1 << n) for x in reversed(result)]
        return gray_code_gen(n+1, result)
    return gray_code_gen(0, [0])

gray_code(1)

#method 3, my favorite
#list compehrehension
# Time and space complexity: O(2 ^ n)
def gray_codde(num_bits: int) -> List[int]:
    results = [0]
    for i in range(num_bits):#at every ith bit, result size becomes twice, size doubles for every bit, hence Time comeplxity = 2^n
        results += [x | (1 << i) for x in reversed(results)]#here i am simply adding one to msb
    return results


def differ_by_1_bit(a, b):
    x = a ^ b
    if x == 0:
        return False
    while x & 1 == 0:
        x >>= 1
    return x == 1


@enable_executor_hook
def gray_code_wrapper(executor, num_bits):
    result = executor.run(functools.partial(gray_code, num_bits))

    expected_size = (1 << num_bits)
    if len(result) != expected_size:
        raise TestFailure('Length mismatch: expected ' + str(expected_size) +
                          ', got ' + str(len(result)))
    for i in range(1, len(result)):
        if not differ_by_1_bit(result[i - 1], result[i]):
            if result[i - 1] == result[i]:
                raise TestFailure('Two adjacent entries are equal')
            else:
                raise TestFailure(
                    'Two adjacent entries differ by more than 1 bit')

    uniq = set(result)
    if len(uniq) != len(result):
        raise TestFailure('Not all entries are distinct: found ' +
                          str(len(result) - len(uniq)) + ' duplicates')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('15-11-gray_code.py', 'gray_code.tsv',
                                       gray_code_wrapper))
