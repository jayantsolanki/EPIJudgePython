from test_framework import generic_test
#https://www.topcoder.com/thrive/articles/A%20bit%20of%20fun:%20fun%20with%20bits

# Write a program to count the number of 1s in the n bits
def count_bits_old(x: int) -> int:
    # TODO - you fill in here.
    count = 0
    while x:
        count += x & 1
        x >>= 1 
    return count

def count_bits(x: int) -> int: #faster since it only goes until number of 1s bit present
    # TODO - you fill in here.
    count = 0
    while x:
        count += 1
        x = x & (x-1)
    return count




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                       count_bits))
