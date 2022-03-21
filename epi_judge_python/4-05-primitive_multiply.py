from test_framework import generic_test

# add using bitwise operations, multiply using shift-and-add
#using grade school algo
def multiply(x: int, y: int) -> int:
    # TODO - you fill in here.
    def add(a,b):
        while b:#this loop is for taking care of carry bits addition
            carry = a & b#yeah, it gives you bit place where 1 and 1 creates carry
            a, b = a ^ b, carry <<1# you are finding the carry bit and moving to one place ahead so that it can be added using XOR later
        return a
        
    running_sum = 0
    while x: # examines each bit of x. You also have to shift right on every loop, grade school math, ok!
        if x & 1:#check if the lsb is 1
            running_sum = add(running_sum, y)#adding 2^ky into the sum
        x, y, = x >> 1, y << 1 #indirectly 2^ky
    return running_sum


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('4-05-primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
