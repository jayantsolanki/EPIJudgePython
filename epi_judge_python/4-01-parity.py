from test_framework import generic_test

#https://www.topcoder.com/thrive/articles/A%20bit%20of%20fun:%20fun%20with%20bits

# O(n)
def parity(x: int) -> int:
    is_parity = 0
    while x:
        is_parity ^= x & 1 #get the last bit value and XOR it with is_parity
        x >>= 1
    return is_parity

def parity_logn(x: int) -> int:
    # TODO - you fill in here.
    x = x ^ x >> 32 
    x = x ^ x >> 16 # only last 16 digits important
    x = x ^ x >> 8 # only last 8 digits important
    x = x ^ x >> 4
    x = x ^ x >> 2
    x = x ^ x >> 1
    return x & 1 # extracting the last digit, which contains the answer

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
print(modulo(77, 8))
print(modulo(77, 2))
print(modulo(5, 2))

"""
Test if x is a power of 2, i.e., evaluates to true for x = 1,2,4,8, false for other values
logic, parity should be only 1, count should be only 1 for all the bits
use this theory, x & (x-1), drops the lowest bit, if that is one, than the final value should be zero, O(1), will only run once if it was in a for loop, 
since after first iteration the value will become zero.
"""
def checkPower(x):
    return bool((((x & (x-1)) == 0) and x)) #extra and makes sure that it is not 
    #marking zero as power of two

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
logic: subtract 1 from x and or(|) it with x, O(1), subtracting 1 turns all zero before the rightmost 1 to 1
"""
def rightProp(x):
    return (x | (x-1))

"""
right propogate the rightmost set bit , example, turn 01010000 to 01011111
logic: get the lowestsetbit, subtract 1 from it, now OR it with x
"""
def rightProp_2(x):
    lowestsetbit = x & ~(x-1)
    return x | (lowestsetbit - 1)

print("Check rightmost set bit propogate")
print(rightProp(8))
print(rightProp_2(8))
print(rightProp(16))
print(rightProp_2(16))

if __name__ == '__main__':
    exit(generic_test.generic_test_main('4-01-parity.py', 'parity.tsv', parity))
