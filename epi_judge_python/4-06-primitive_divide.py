from test_framework import generic_test


def divide(x: int, y: int) -> int:
    # TODO - you fill in here.
    result, power = 0, 32
    y_power = y << power # y*2^k, 2^k is the factor
    while x >= y:
        while y_power > x:
            y_power >>=1#keep on dividing by 2
            power -= 1
        
        result += 1 << power
        x -= y_power
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('4-06-primitive_divide.py',
                                       'primitive_divide.tsv', divide))
