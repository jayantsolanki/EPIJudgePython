from test_framework import generic_test

#advantage of using 2^k is that it can be computed efficiently using shifting
# Advantage of using 2^k is that it can be computed efficiently using shifting. You basically find the 2^k value that makes y x 2^k just 
# less than x then add that 2^k value to the quotient. Repeat above step by lowering the power by shifting right.
#Time O(n)
def divide(x: int, y: int) -> int:
    result, power = 0, 32 # start with largest power and keep going down
    y_power = y << power # y*2^k, 2^k is the factor
    while x >= y:#stop when y > x, that means x became remainder now
        while y_power > x:
            y_power >>=1#keep on dividing by 2
            power -= 1
        
        result += 1 << power
        x -= y_power# essentially divison is the process of keep on subtracting until you start getting negative
    return result







if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('4-06-primitive_divide.py',
                                       'primitive_divide.tsv', divide))
