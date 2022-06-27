from test_framework import generic_test


#time is O(n), where n is the number of bits in numbers
"""
Find HCM or GCD
Logic: Using Euclidean Algo
    if y > x, GCD of x and y = Gcd of x, y-x and so on until y-x == 0
    GCD(156, 36) = GCD(156 - 36, 36) = GCD(156 - 36 -36 , 36) == GCD(156 % 36, 36) = GCD(36, 12) = GCD(36 %12, 12) = 12
    Since 36 % 12 == 0

"""
def gcd(x: int, y: int) -> int: #assuming x will be always less than y
    if x == 0:
        return y
    else:
        if x > y:
            return gcd(y, x)
        else:
            return gcd(y % x, x)


def gcd_book(x: int, y: int) -> int:

    if x > y:
        return gcd(y, x)
    elif x == 0:
        return y
    elif not x & 1 and not y & 1:  # x and y are even.
        return gcd(x >> 1, y >> 1) << 1
    elif not x & 1 and y & 1:  # x is even, y is odd.
        return gcd(x >> 1, y)
    elif x & 1 and not y & 1:  # x is odd, y is even.
        return gcd(x, y >> 1)
    return gcd(x, y - x)  # Both x and y are odd.


if __name__ == '__main__':
    exit(generic_test.generic_test_main('15-00-euclidean_gcd.py', 'gcd.tsv', gcd))
