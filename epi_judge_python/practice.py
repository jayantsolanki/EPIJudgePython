#practice;

#parity checker;

def parityChecker(N):
    print(123)
    N ^= N>>32
    N ^= N>>16
    N ^= N>>8
    N ^= N>>4
    N ^= N>>2
    N ^= N>>1
    return N&1

parityChecker(1010101011)
parityChecker(101010101)
# this one is log N

#another one, for log(k), where k is numbr of bits

def parityCheck(N:int)->int:# so if k is odd then the result will be 1 or else zero
    result = 0
    #N = int(N) # important 
    while N:
        result ^=1
        N = N&(N-1)
    return result
parityCheck(0b1010101011)
parityCheck(0b101010101)

#computer mod power 2
def modpow(N, m):
    return(N&((1<<m)-1))

modpow(34, 3)

#swap digits

def swapDig(N, a, b):
    #check if the ath and bth bits are not same
    if(1 & (N>>a) != 1 & (N>>b)):
        #go ahead
        createMask = (1<<a) | (1<<b)
        return N ^ createMask
    return N

print(swapDig(16, 4, 0)) # bitmask = 10001, so 10000 XOR 10001 = 00001 = 1
print(swapDig(16, 4, 1))# bitmask = 10010, so 10000 XOR 10010 = 00010 = 2
print(swapDig(16, 4, 3))# bitmask = 11000
print(swapDig(16, 4, 4))# bitmask = 10000


#reverse bits # nt gonna work, mask is necessary
def reverse_bits(x): #changed algo
    y = 0
    position = 0
    while x:
        y |=(x & 1) 
        
        # y |=(x & 1) << position
        x >>= 1
        # if x:
        y <<=1
        # position += 1
    return y
    

print(reverse_bits(2))
print(reverse_bits(4))
print(reverse_bits(16))
print(reverse_bits(255))
print(reverse_bits(10))
print(reverse_bits(5))


#dutch flag problem
def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A)
    while equal<larger:
        if A[equal] < pivot:
            A[equal], A[smaller] = A[smaller], A[equal]
            smaller += 1
            equal += 1
        elif(A[equal] == pivot):
            equal += 1
        else:
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]
            
    return A

#testing

dutch_flag_partition(2, [5,7,3,6,3,2,0,1,9])


# count bits

def count_bits(x):
    sum = 0
    while x:
        sum=sum + (x&1)
        x >>=1
    return sum
