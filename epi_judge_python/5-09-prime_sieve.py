from typing import List

from test_framework import generic_test

# a trial division algo has O(n^1.5), because we go through n numbers, and do n^0.5 division checks. 
# It is a classical algo we use to do in school
#improved one
# Given n, return all primes up to and including n.
# time to sieve for each p is proportional to n/p, hence O(n/2 + n/5 + n/7 + n/11  + ..) yielding below
# time: O(nloglogn), space, O(n)
def generate_primes(n: int) -> List[int]:
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


generate_primes(20)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('5-09-prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
