from test_framework import generic_test

#uses recursion
def power(x: float, y: int) -> float:
    # TODO - you fill in here.
    result, power = 1.0, y
    if y < 0: # this is used for negative powers
        power, x = -power, 1.0/x
    while power: #if zero then return result = 1
        if power & 1: #checking if the last digit of power is 1
            result *= x
        x, power = x * x, power >> 1 # dividing the power by 2
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('4-07-power_x_y.py', 'power_x_y.tsv',
                                        power))
