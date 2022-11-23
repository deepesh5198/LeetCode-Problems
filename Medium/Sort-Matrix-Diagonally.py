# A matrix diagonal is a diagonal line of cells starting from some 
# cell in either the topmost row or leftmost column and going in the 
# bottom-right direction until reaching the matrix's end. For example, 
# the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, 
# includes cells mat[2][0], mat[3][1], and mat[4][2].

# Given an m x n matrix mat of integers, sort each matrix diagonal 
# in ascending order and return the resulting matrix.

# EXAMPLE:
# Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
# Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

from pprint import pprint
from collections import defaultdict
def diagonalSort(mat):
    """
    :type mat: List[List[int]]
    :rtype: List[List[int]]
    """
    # store m and n
    m = len(mat)
    n = len(mat[0])

    # create mapping
    # using defaultdict(list) ## it creates a dict of lists
    mapping = defaultdict(list)

    # go through each element and store
    # them in diag_index in mapping respectively
    for i in range(m):
        for j in range(n):
            # calculate diag_index
            diag_index = i-j
            # element at mat[i][j]
            el = mat[i][j]

            # append to list at
            # diag_index
            mapping[diag_index].append(el)

    # sort each lists(diagonals) in mapping
    # in descending order
    for key in mapping:
        mapping[key].sort(reverse=True)

    # again put the elements back in
    # matrix by popping from each diagonal_lists
    # in mapping
    for i in range(m):
        for j in range(n):
            # calculate diagonal index to pop from
            diag_index = i-j
            # pop the element from the diag_index
            el = mapping[diag_index].pop()

            # put the element at [i][j]th location
            mat[i][j] = el
        
    # return the matrix
    return mat

print(diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))
