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
        spiral_ordering.extend([col[size-offset - 1] for col in square_matrix[offset:size-offset-1][:]])#col elements
        spiral_ordering.extend(square_matrix[size-offset - 1][size-offset-1:offset:-1])#row elements reversed
        spiral_ordering.extend([col[offset] for col in square_matrix[size-offset-1:offset:-1][:]]) #col elements reversed
        
    for offset in range((len(square_matrix)+1) // 2): # + one needed, for n = 1
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
        if offset == d - offset - 1:
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
    k = 0
    l = 0
 
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
        if (k < m):
 
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




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('5-18-spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
