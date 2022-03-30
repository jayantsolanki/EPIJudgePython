from typing import List

from test_framework import generic_test

"""
Write a function that takes as input an nxn 2d array , and roates the array by 90 degree clockwise
time: O(n^2), space O(1)
Logic:
first insight is that we can perform the rotation  in place, in a layer-by-layer fashion
Program works its way into the center of the array from the outermost layers, performing
exchanges within a layer using the four-way swap

Note that unary complement operator ~ implemented by the special method __invert__ is unrelated to the not operator, which logically negates the value returned by __bool__
~ is the bitwise complement operator in python which essentially calculates -x - 1
So, identify each postitions to be exchanges, one on the left of equation will take the value of other, so
example, 1 will take 4th element, 2 will take 1st element, 3 will take 2nd element, 4th will take 3rd element in outer layer
"""
def rotate_matrix(square_matrix: List[List[int]]) -> None:
    matrix_size = len(square_matrix) - 1
    for i in range(len(square_matrix) // 2):#go until half of it, since in the second loop you are capturing other half too
        for j in range(i, matrix_size - i):
            # Perform a 4-way exchange. Note that A[~i] for i in [0, len(A) - 1]
            # is A[-(i + 1)].
        #in every inner loop iteration change postition of 1st, last, then second, second last, then third, third last, so on
        #outer loop changes the position of 1st verses last, second verses second last
            (square_matrix[i][j], square_matrix[j][~i],  square_matrix[~i][~j], 
            square_matrix[~j][i])= (square_matrix[~j][i], 
                                    square_matrix[i][j], 
                                    square_matrix[j][~i], 
                                    square_matrix[~i][~j])
            # print(i,j, square_matrix)

# rotate_matrix_simple([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

#variant 1
"""
Implement an algorithm  to reflect array A, assum it is nxn 2d array. , about the 
horizontal axis. Repeat same reflection along y-axis, the diagonal from top-left to bottom-right
and diagonal top-right to bottom-left
"""

def mirror_matrix_horizontally(square_matrix):

    matrix_size = len(square_matrix)
    


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('5-19-matrix_rotation.py',
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
