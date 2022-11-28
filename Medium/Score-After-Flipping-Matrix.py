# Problem Description
# You are given an m x n binary matrix grid.

# A move consists of choosing any row or column and toggling each value in that 
# row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

# Every row of the matrix is interpreted as a binary number, and the score of 
# the matrix is the sum of these numbers.

# Return the highest possible score after making any number of moves 
# (including zero moves).

# EXAMPLE:
# Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# Output: 39
# Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
def matrixScore(grid) -> int:
    R, C = len(grid), len(grid[0])
    ans = 0

    for c in range(C):
        col = 0

        for r in range(R):
            col += grid[r][c]^grid[r][0]

        ans+= max(col, R-col)*2**(C-1-c)
    return ans