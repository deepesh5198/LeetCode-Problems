# Problem Description:
# Given a m x n grid with 0s and 1s, where, 
# 0 means water, 
# and 1 means island
# We are required to return the Area of the largest island.

# SOLUTION: Use DFS

from typing import List

def maxAreaOfIsland(grid: List[List[int]]) -> int:
    # get the number of rows and columns in the grid
    rows, cols = len(grid), len(grid[0])
    
    # create an empty set to keep the visited cells
    visited = set()
    
    # defining a dfs function
    def dfs(r, c):
        # base case
        if ((r<0 or r>= rows) or (c<0 or c>=cols) or
            (grid[r][c] == 0) or ((r, c) in visited)):
            return 0
        # add the (r, c) pair (cell) in the visited set 
        visited.add((r,c))
        
        return (1 + 
                dfs(r+1, c) +
                dfs(r-1, c) +
                dfs(r, c+1) +
                dfs(r, c-1)
                )
    
    area = 0
    # traverse the whole grid
    for r in range(rows):
        for c in range(cols):
            area = max(area, dfs(r,c))
            
    return area