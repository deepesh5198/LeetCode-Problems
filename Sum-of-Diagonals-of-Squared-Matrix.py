# Problem Description:
# Given a square matrix mat, return the sum of the matrix diagonals.

# Only include the sum of all the elements on the primary diagonal
# and all the elements on the secondary diagonal that are not part 
# of the primary diagonal.

# EXAMPLE:
# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]
# Output: 25
# Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# Notice that element mat[1][1] = 5 is counted only once.


def diagonalSum(mat):
    """
    :type mat: List[List[int]]
    :rtype: int
    """
    length = len(mat[0])
    if length == 1:
        return mat[0][0]

    sum_of_primary = 0
    sum_of_secondary = 0

    for i in range(length):
        sum_of_primary += mat[i][i]

    for i,j in zip(range(length), reversed(range(length))):
        if not i==j:
            sum_of_secondary += mat[i][j]

    return sum_of_primary + sum_of_secondary

print(diagonalSum(mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]))