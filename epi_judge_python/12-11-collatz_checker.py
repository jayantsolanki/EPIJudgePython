from typing import Set

from test_framework import generic_test

"""
Test collatz conjecture for first n positive integers
    1 - if a number is odd then update it with a value calculated by multiply by three and add one
    2 - if even; update it with its half
    Keep doing 1 or 2 until 1 is reached
Logic:
    1 - reuse computation by storing all the numbers that have covergence to 1
    2 - skip even numbers, since they are immediately halved and result number must have been checked before
    3 - if every number until k has been tested,  we can stop the loop as soon as we reach a number
        less than or equal to k. We do not need to store the number < k in the hash table
    4 - Check for inifnite loop if smae number encountered, then exit
Time: at least proportional to n
"""
def test_collatz_conjecture(n: int) -> bool:

    # Stores odd numbers already tested to converge to 1.
    verified_numbers: Set[int] = set()

    # Starts from 3, hypothesis holds trivially for 1.
    for i in range(3, n + 1):
        sequence: Set[int] = set()#used for checking if infinite loop is going
        test_i = i
        while test_i >= i:
            if test_i in sequence:
                # We previously encountered test_i, so the Collatz sequence has
                # fallen into a loop. This disproves the hypothesis, so we
                # short-circuit, returning False.
                return False
            sequence.add(test_i)

            if test_i % 2:  # Odd number.
                if test_i in verified_numbers:
                    break  # test_i has already been verified to converge to 1.
                verified_numbers.add(test_i)
                test_i = 3 * test_i + 1  # Multiply by 3 and add 1.
            else:
                test_i //= 2  # Even number, halve it.
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('12-11-collatz_checker.py',
                                       'collatz_checker.tsv',
                                       test_collatz_conjecture))
