# Problem Description
# You are given an n x n 2D matrix representing an image, rotate the image 
# by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the 
# input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# EXAMPLE:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    # reverse the matrix
    matrix.reverse()
    # input: [[1,2,3], [4,5,6], [7,8,9]]
    # reversed: [[7,8,9], [4,5,6], [1,2,3]]
    
    # calculate the length of row of matrix
    l = len(matrix[0])

    # swap all elements except the diagonal elements
    # from i to l-2
    for i in range(l-1):
        # from j = i+1 to l-1
        for j in range(i+1, l):
            # swapping
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # return the matrix
    return matrix

print(rotate([[1,2,3], [4,5,6], [7,8,9]]))