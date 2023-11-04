from typing import List

from test_framework import generic_test

# leetcode: 204,
# https://leetcode.com/problems/count-primes/?envType=list&envId=9fmel2q1
# a trial division algo has O(n^1.5), because we go through n numbers, and do n^0.5 division checks. 
# It is a classical algo we use to do in school
#improved one
# Given n, return all primes up to and including n.
# time to sieve for each p is proportional to n/p, hence O(n/2 + n/5 + n/7 + n/11  + ..) yielding below
# time: O(nloglogn), space, O(n)
def generate_primes_ori(n: int) -> List[int]:
    primes = []
    # is_prime[p] represents if P is prime or not. Initially, set each to
    # true, expecting 0 and 1. Then use sieving to eliminate nonprimes.
    is_prime = [False, False] + [True] * (n-1)# first two for 0, 1
    for p in range(2, n+1):
        if is_prime[p]:#only proceed when array at pos p is true
            primes.append(p)
            #sieve p's multiples.
            for i in range(p*2, n+1, p):#next P+P+P+P... so on, mark false for multiples of p
                is_prime[i] = False
    return primes

#ignore even numbers, and only look for p^2 for sieving, also less on storage
def generate_primes(n: int) -> int:
    primes = []
    size = (n - 3) // 2 + 1 # minusing 0, 1, and 2, and also only n-1 to be considered
    is_prime = [True] * (size)
    if n >= 2:
        primes.append(2)
    for p in range(size):# < n
        num = 2 * (p + 1) + 1 #or use 2*p + 3
        # is_prime[p] represents (2p + 3) is prime or not.
        # For example, is_prime[0] represents 3 is prime or not, is_prime[1]
        # represents 5, is_prime[2] represents 7, etc.
        # Initially set each to true. Then use sieving to eliminate nonprimes.
        if is_prime[p]:
            primes.append(num)
            # Sieving from num^2, where num^2 = (4p^2 + 12p + 9). The index in is_prime
            # is (2p^2 + 6p + 3) because is_prime[p] represents 2p + 3.
            # for i in range(num + 2 * num, n, 2 * num):
            for j in range(2 * p**2 + 6 * p + 3, size, num):
                is_prime[j] = False
    return primes
    


generate_primes(20)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('5-09-prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
  