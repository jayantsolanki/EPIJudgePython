from test_framework import generic_test


def reverse(x: int) -> int:
    # TODO - you fill in here.
    result, x_remaining = 0, abs(x)
    while x_remaining:
        result = result * 10 + x_remaining % 10
        x_remaining //=10
    return -result if x < 0 else result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('4-08-reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
