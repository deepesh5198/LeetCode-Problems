# Problem Description:

# Given dimension of grid, get all the unique paths for a robot
# to move from (0,0) position to (m-1, n-1) position.

# EXAMPLE:
# Input: m = 3, n = 7
# Output: 28

import math
def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    total_moves = math.factorial(m+n - 2)
    down_moves = math.factorial(m-1)
    right_moves = math.factorial(n-1)

    return total_moves/(down_moves * right_moves)