from test_framework import generic_test


def swap_bits(x, i, j):
    # TODO - you fill in here.
    # extract the ith and jth bits and check if they differ, if they differ, the only swap them
    if ((x >> i) & 1) != ((x >> j) & 1): # move the ith and jth bit to right and fetch their value, anding with 1, gives out the last binary bit (rightmost)
        # i-th and j-th bits differs, we will swap them by flipping their values
        # use XOR to select the bits to flip, x^ 1 = 0, whn x = 1 and 1 when x = 0
        bit_mask = (1 << i) | (1 << j) # creating bitmask
        x ^= bit_mask # xor used here to flip the digit, 0 ^ 1 = 1, 1^ 1 = 0
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('4-02-swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
