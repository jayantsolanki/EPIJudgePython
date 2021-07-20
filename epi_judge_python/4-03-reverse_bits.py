from test_framework import generic_test


def reverse_bits(x: int) -> int:
    # TODO - you fill in here.
    bit_size = 64 # creating this for 64bit number reverse
    y = 0
    position = bit_size - 1
    while position >= 0:#start with LSB, push it to MSB
        y |=(x & 1) << position
        x >>= 1#kick out LSB
        position -= 1
    return y


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('4-03-reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
