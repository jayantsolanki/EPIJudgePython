from test_framework import generic_test


def parity(x: int) -> int:
    # TODO - you fill in here.
    x = x ^ x >> 32
    x = x ^ x >> 16
    x = x ^ x >> 8
    x = x ^ x >> 4
    x = x ^ x >> 2
    x = x ^ x >> 1
    return x & 1

"""
Variants
"""

def parity_k(x): # O(k), where k is the number of 1 bits in a binary digit, 101011001, k = 5
    result = 0
    while x:
        result = result ^ 1
        x = x & (x-1) # this drops the last bit with 1, so basically loop will go till k
    return result

print(parity_k(0b10001010101)) # start with 0b for binary rep
print(parity_k(0b101010101))

#variants

"""
compute x mod a power of two, that is, x mod 2^n
logic: use formula x&(2^n-1), this is masking x with 2^n - 1,  O(1)
further explanation, 2^n - 1 is the digits with all bits set to 1. So when you mask it with the target number, you get values of the remainder.
"""
def modulo(x, n):
    return (x & ((1<<n) - 1))

#testing 
print("Modulo")
print(modulo(77, 6))
print(modulo(77, 2))
print(modulo(5, 2))

"""
Test if x is a power of 2, i.e., evaluates to true for x = 1,2,4,8, false for other values
logic, parity should be only 1, count should be only 1 for all the bits
use this theory, x & (x-1), drops the lowest bit, if that is one, than the final value should be zero, O(1), will only run once if it was in a for loop, 
since after first iteration the value will become zero.
"""
def checkPower(x):
    return bool((((x & (x-1)) == 0) and x)) #extra and makes sure that it is not marking zero as power of two

#test
print("Check power")
print(checkPower(20))
print(checkPower(8))
print(checkPower(16))
print(checkPower(32))
print(checkPower(256))
print(checkPower(255))
print(checkPower(24))
print(checkPower(0))


"""
right propogate the rightmost set bit , example, turn 01010000 to 01011111
logic: subtract 1 from x and or it with x, O(1)
"""
def rightProp(x):
    return (x | (x-1))

print("Check rightmost set bit propogate")
print(rightProp(8))
print(rightProp(16))

if __name__ == '__main__':
    exit(generic_test.generic_test_main('4-01-parity.py', 'parity.tsv', parity))
