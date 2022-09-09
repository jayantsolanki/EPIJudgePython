from typing import List
import math
from test_framework import generic_test

#a 2-d array can be written as row-wise or columnwise. In this problem we write spiral clockwise
#wap which takes nxn 2d array and returns the spiral ordering
#time: O(n^2)
"""
here is the uniform way of adding the boundaries, add the first n-1 elements in first row, then n-1  
elements of last column, then n-1 elements of last row(in reversed) then n-1 elements of first column
in reversed. After this we are left with n-2 x n-2 matrix, hence process goes on
Odd n will have corner case of a center element, else even n will be a center matrix
Above becomes an iterative process of getting elements in nxn, (n-2)x(n-2), (n-4)x(n-4)m,,,,2d arrays
#divide and Conquer
"""
def matrix_in_spiral_order_original(square_matrix: List[List[int]]) -> List[int]:
    def matrix_layer_in_clockwise(offset):
        if offset == len(square_matrix) - offset - 1:
            # square_matrix has odd dimension, and we are at the center of the
            # matrix square_matrix.
            spiral_ordering.append(square_matrix[offset][offset])
            return

        spiral_ordering.extend(square_matrix[offset][offset:-1 - offset])
        spiral_ordering.extend(list(zip(*square_matrix))[-1 - offset][offset:-1 - offset])
        spiral_ordering.extend(square_matrix[-1 - offset][-1 - offset:offset:-1])#store in reversed
        spiral_ordering.extend(list(zip(*square_matrix))[offset][-1 - offset:offset:-1])#store in reversed

    spiral_ordering: List[int] = []
    for offset in range((len(square_matrix) + 1) // 2):
        matrix_layer_in_clockwise(offset)
    return spiral_ordering

#easy for my weak mind lol
#time: O(n^2)
def matrix_in_spiral_order(square_matrix):
    offset = 0
    size = len(square_matrix)
    spiral_ordering = []
    def matrix_layer_in_clockwise(offset, size):
        if (size - offset - 1) == offset: #checking if only one element left
            spiral_ordering.append(square_matrix[offset][offset])#should be append, since we getting only element, not subarray
            return
               
        spiral_ordering.extend(square_matrix[offset][offset:size-offset-1])#row elements
        spiral_ordering.extend([col[size-offset - 1] for col in square_matrix[offset:size-offset-1][:]])#col elements, [:] not needed
        spiral_ordering.extend(square_matrix[size-offset - 1][size-offset-1:offset:-1])#row elements reversed
        spiral_ordering.extend([col[offset] for col in square_matrix[size-offset-1:offset:-1][:]]) #col elements reversed
        
    for offset in range((len(square_matrix)+1) // 2): # + one needed, for n = 1 -> (1+1)//2
    # for offset in range(math.ceil(len(square_matrix) / 2)): # + one needed, for n = 1
        matrix_layer_in_clockwise(offset, size)

    return spiral_ordering
    
# matrix_in_spiral_order([[1,2,3],[4,5,6],[7,8,9]])
# matrix_in_spiral_order([[1,2,3,4],[5,6, 7,8],[9,10,11,12], [13,14,15,16,17]])
# matrix_in_spiral_order([[1,2,3,4,5],[6, 7,8,9,10],[11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25]])


#variant 1
"""
generate dxd array given its spiral, [1,2,3,4,....d^2], if d =3, result = [[1,2,3],[4,5,6],[7,8,9]]
https://www.geeksforgeeks.org/form-a-spiral-matrix-from-the-given-array/
Approach: This problem is just the reverse of this problem “Print a given matrix in spiral form“. The approach to do so is: 

Traverse the given array and pick each element one by one.
Fill each of this element in the spiral matrix order.
Spiral matrix order is maintained with the help of 4 loops – left, right, top, and bottom.
Each loop prints its corresponding row/column in the spiral matrix.
"""
def spiral_to_matrix(spiral):
    d = int(math.sqrt(len(spiral)))
    mat= [[0 for i in range(d)] for j in range(d)];
    index = 0
    for offset in range((d+1) // 2):
        if offset == d - offset - 1: #odd sized
            mat[offset][offset] = spiral[index]
            break

        # print top row
        for i in range(offset, d-offset-1):
            mat[offset][i] = spiral[index]
            index += 1

        # print right column
        for i in range(offset, d-offset-1):
            mat[i][d-1-offset] = spiral[index]
            index += 1

        #print bottom row
        for i in range(d-1-offset, offset, -1):
            mat[d-1-offset][i] = spiral[index]
            index += 1

        # print left column
        for i in range(d-1-offset, offset, -1):
            mat[i][offset] = spiral[index]
            index += 1
    return mat

spiral_to_matrix([ 1, 2, 3, 4, 5, 6,
                7, 8, 9, 10, 11, 12,
                13, 14, 15, 16, 17, 18 ])
spiral_to_matrix([1,2,3,4])
spiral_to_matrix([1,2,3,4,5,6,7,8,9])
spiral_to_matrix([ 1, 2, 3, 4, 5, 6,
                7, 8, 9, 10, 11, 12,
                13, 14, 15, 16, 17, 18,
                19,20,21,22,23,24,25 ])

#variant 3# not working
"""
WAP to enumerate the first n pairs of integers (a,b) in spiral order.
Example (0,0) (1,0) (1,-1) (0,-1) (-1,-1) (-1,0) (-1,1) (0,1) (1,1) (2,1) 
Logic: may be use cos and sin, and add one after 8 repeats lets see
"""
def pair_spirals(n):
    #imagine it as a square of diagonal 2x2^0.5, whose diagonal increased by 2 after every 8 repeats  (at every 360 degree, 45 increment)
    #1.414*costheta, 1.414*sintheta, for x and y
    result = [(0,0)]
    if n == 1:
        return result
    pairs = {
        1: (1,0),
        2: (1,-1),
        3: (0,-1),
        4: (-1, -1),
        5: (-1, 0),
        6: (-1, 1),
        7: (0, 1),
        0: (1, 1),
    }
    for i in range(1,n):
        if i - 8 > 0: 
            result.append((result[i-1][0]+ pairs[i%8][0], result[i-1][1]+ pairs[i%8][1]))
            print(i%8)
            # result.append((pairs[i%8][0], pairs[i%8][1]))
        else:
            result.append((pairs[i%8][0], pairs[i%8][1]))
    return result

pair_spirals(11)

#variant 4
"""
write a program to compute spiral of mxn array
"""
#easy for my weak mind lol
#time: O(m*n)
#https://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/
def matrix_in_spiral_order_mn(A):
    m = len(A)    
    n = len(A[0]) 
    spiral_ordering = []
    k = 0 #for controlling row offset
    l = 0 #for controlling column offset
 
    ''' k - starting row index
        m - ending row index
        l - starting column index
        n - ending column index
        i - iterator 
    '''
 
    while (k < m and l < n):
 
        # append the first row from
        # the remaining rows
        for i in range(l, n):
            spiral_ordering.append(A[k][i])
 
        k += 1
 
        # append the last column from
        # the remaining columns
        for i in range(k, m):
            spiral_ordering.append(A[i][n - 1])
 
        n -= 1
 
        # append the last row from
        # the remaining rows
        if (k < m): #make sure there is  not a single row array left
 
            for i in range(n - 1, (l - 1), -1):
                spiral_ordering.append(A[m - 1][i])
 
            m -= 1
 
        # append the first column from
        # the remaining columns
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                spiral_ordering.append(A[i][l])
 
            l += 1


    return spiral_ordering

matrix_in_spiral_order_mn([[1,2,3,4],[5,6, 7,8]])
matrix_in_spiral_order_mn([[1,2]])
matrix_in_spiral_order_mn([[1], [2]])
matrix_in_spiral_order_mn([[1,2,3,4],[5,6, 7,8], [9,10,11,12]])
matrix_in_spiral_order_mn([[1,2,3,4],[5,6, 7,8], [9,10,11,12], [13,14,15,16]])
matrix_in_spiral_order_mn([[1,2,3], [4,5,6]])
matrix_in_spiral_order_mn([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
matrix_in_spiral_order_mn([[1,2,3],[4,5,6],[7,8,9]])
matrix_in_spiral_order_mn([[1,2,3,4,5],[6, 7,8,9,10],[11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25]])

#variant 5 and 6
"""
Compute the kth element in the spiral order for an mxn 2d array A in O(R) time
https://stackoverflow.com/questions/54774747/compute-the-kth-element-in-spiral-order-for-an-m-x-n-2d-array-a-in-o1-time
"""
def find_kth_element(A, m, n, k):
    if (k > m*n or k < 1):
        return -1
    if (m < 1 or n < 1):
        return -1
    if(m == 1):#Total elements formula not applicable in one-dimensional array
        return A[0][k-1]
    if(n == 1):
        return A[k-1][0]
    ring = 1
    mod_m = m 
    mod_n = n
    if(k == m*n):
        if m%2!=0 and n%2!=0:
            return A[m//2][n//2]
    while True:
        Total_elements = 2*m + 2*n -8*(ring) + 4 #in that ring, use book notes to derive this formula, max elements that ring can have
        # Total_elements = 2*mod_m + 2*mod_n - 4 #in that ring, use book notes to derive this formula
        # print(Total_elements)
        if k <= Total_elements:
            offset = k
            #check in first row
            if offset <= mod_n:
                x = ring - 1
                y = ring - 1 + offset -1
            #check in last column
            elif offset <= (mod_n + mod_m - 1):
                x = ring - 1 + offset - mod_n
                y = n - ring
            #check in last row
            elif offset <= (mod_n + mod_m - 1 + mod_n - 1):
                x = m - ring
                y = ring-1 + mod_n - 1 - (offset - (mod_n + mod_m - 1))
            #check in first column
            elif offset <= (mod_n + mod_m - 1 + mod_n - 1 + mod_m-1):
                x = ring - 1 + mod_m - 1 - (offset - (mod_n + mod_m-1 + mod_n - 1))
                y = ring - 1
            # print(x, y)
            return A[x][y]
        else:
            mod_m = m - ring*2
            mod_n = n - ring*2
            ring = ring + 1
            k = k - Total_elements
            # print(mod_m, mod_n)

        if(mod_m < 1 or mod_n < 1):
            break

find_kth_element([[1,2,3,4]], 1, 4, 3)
find_kth_element([[1], [2], [3], [4]], 4, 1, 3)
find_kth_element([[1,2,3,4], [5,6,7,8]], 2, 4, 8)
find_kth_element([[1,2,3,4], [5,6,7,8], [9, 10, 11, 12], [13,14,15,16]], 4, 4, 13)
find_kth_element([[1,2,3,4], [5,6,7,8], [9, 10, 11, 12], [13,14,15,16], [17,18,19,20]], 5, 4, 20)
find_kth_element([[1,2,3,4], [5,6,7,8], [9, 10, 11, 12], [13,14,15,16], [17,18,19,20]], 5, 4, 20)
find_kth_element([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]], 3, 5, 2)
find_kth_element([[1,2,3], [4,5,6], [7,8,9]], 3, 3, 9)
find_kth_element([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25]], 5, 5, 25)


# Variant 5 and 6
"""
Compute the kth element in the spiral order for an mxn 2d array A in O(R) time
https://stackoverflow.com/questions/54774747/compute-the-kth-element-in-spiral-order-for-an-m-x-n-2d-array-a-in-o1-time
"""
# def kth_element_spiral(A, m, n, k):#k here starts with 0
#     # first_ring_max = 2 * (m-1) + 2 * (n - 1)
#     first_ring_max = 2*m + 2*n - 4

#     ring, ring_start_elements = None, None

#     if (k < first_ring_max):
#         ring = 0
#         ring_start_elements = 0
#     else:
#         ring = int(math.floor((-(m + n) + math.sqrt((m+n)**2 - 4*k)) /(-4)))
#         #arithmatic sum to find out how many elements covers before this ring started
#         ring_start_elements = int((ring * (first_ring_max + 2 * (m-(1 + 2*(ring - 1))) + 2 * (n-(1 + 2*(ring - 1))))) / 2)

#     offset = k - ring_start_elements

#     width = (m - ring*2) - 1
#     height = (n - ring*2) - 1

#     if (offset <= width): # top
#         x = ring + offset 
#         y = ring
#         return A[x][y]
#     elif (offset <= width + height): # right
#         x = m - ring - 1
#         y = ring + (offset - width)
#         print("I ran")
#         return A[x][y]
#     elif (offset <= width + height + width): # bottom
#         x = width - (offset - width - height)
#         y = n - ring - 1
#         return A[x][y]
#     else: # left
#         x = ring
#         y = height - (offset - width - height - width)
#         return A[x][y]
"""
T1 = 2m + 2n - 4
Tr = 2m + 2n -8r + 4 #r here is the ring
Sr = (T1 + Tr)r/2 #sum of progression till ring r
Solving:
Sr = r(2m+2n-4+2m+2n-8r+4)/2
Sr = r(4m +4n -8r)/2
Sr = -4r^2 + (2m +2n)r #this is quadratic equation analogous to ax^2 + bx + c
Since Sr is lower bound of k, lets solve it with respect to r and k
-4r^2 + (2m +2n)r <= k
-4r^2 + (2m +2n)r - k <= 0
r = floor((-(m + n) + sqrt((m+n)^22 - 4*k)) /(-4))
"""
def kth_element_spiral(A, m, n, k):#k here starts with 1
    """
    inputs: A: array, m: rows, n: columns, k: position
    output: Array element returned for position k
    """
    if k==0:
        return(-1,-1)

    first_ring_max = 2*m + 2*n - 4
    ring, ring_start_elements = None, None #ring: rings elapsed to reach position k
    if (k < first_ring_max):
        ring = 0
        ring_start_elements = 0
    else:
        ring = int(math.floor((-(m + n) + math.sqrt((m+n)**2 - 4*k)) /(-4)))
        #arithmetic sum to find out how many elements covered in ring, ring-1 , .. 0
        ring_start_elements = int(-4*(ring**2) + 2*ring*(m+n))
    offset = k - ring_start_elements#elements remaining to check for in the current ring, because k is upper boundary

    #rows left in current ring, logic: after every ring top and bottom rows removed
    mod_m = (m - ring*2)
    # columns left in current ring, logic: after every ring left and right rows removed
    mod_n = (n - ring*2)

    if (offset <= mod_n): # top row in the current ring
        x = ring
        y = ring + offset - 1
    elif (offset <= mod_n + mod_m - 1): # rightmost column in the current ring
        x = ring + (offset - mod_n)
        y = n - 1 - ring
    elif (offset <= mod_n + mod_m - 1 + mod_n - 1): # bottom row in the current ring
        x = m - 1 - ring
        y = ring + mod_n - 1 - (offset - (mod_n + mod_m - 1))
    elif offset <= mod_n + mod_m - 1 + mod_n - 1 + mod_m-1: # leftmost column in the current ring
        x = ring + mod_m - 1 - (offset - (mod_n + mod_m-1 + mod_n - 1))
        y = ring
    else:
        return(-1, -1)#not found
    return A[x][y]    

kth_element_spiral([[1,2,3,4]], 1, 4, 3)
kth_element_spiral([[1], [2], [3], [4]], 4, 1, 3)
kth_element_spiral([[1,2,3,4], [5,6,7,8]], 2, 4, 8)
kth_element_spiral([[1,2,3,4], [5,6,7,8], [9, 10, 11, 12], [13,14,15,16]], 4, 4, 13)
kth_element_spiral([[1,2,3,4], [5,6,7,8], [9, 10, 11, 12], [13,14,15,16], [17,18,19,20]], 5, 4, 16)
kth_element_spiral([[1,2,3,4], [5,6,7,8], [9, 10, 11, 12], [13,14,15,16], [17,18,19,20]], 5, 4, 20)
kth_element_spiral([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]], 3, 5, 2)
kth_element_spiral([[1,2,3], [4,5,6], [7,8,9]], 3, 3,8)
kth_element_spiral([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25]], 5, 5, 25)

for i in range(1,10):
    print(i, kth_element_spiral([[1,2,3], [4,5,6], [7,8,9]],3, 3, i))
for i in range(1,9):
    print(i, kth_element_spiral([[1,2,3,4], [5,6,7,8]],2, 4, i))
for i in range(1,5):
    print(i, kth_element_spiral([[1], [2], [3], [4]], 4, 1, i))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('5-18-spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
