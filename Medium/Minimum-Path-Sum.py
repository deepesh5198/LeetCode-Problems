# USING Dynamic Programming

def minPathSum(grid) -> int:
    if not grid:
        return 0
    
    # get number rows and cols
    rows, cols = len(grid), len(grid[0])

    # row traverse
    for i in range(1, rows):
        # store the sum of prev and current cell
        # in current cell
        grid[i][0] = grid[i-1][0] + grid[i][0]
    
    # col traverse
    for j in range(1,cols):
        # store the sum of prev and current cell
        # in current cell
        grid[0][j] = grid[0][j-1] + grid[0][j]
        
    # traverse the grid
    for i in range(1, rows):
        for j in range(1, cols):
            # store the sum of 
            # min(grid[i-1][j], grid[i][j-1]) and value in current cell
            # in the current cell
            grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
    
    # return the value at previous cell
    return grid[-1][-1]


# grid = [[1,3,1],[1,5,1],[4,2,1]]

# rows = len(grid)
# cols = len(grid[0])
# min_sum = 0
# visited = set()

# def dfs(r, c, min_sum):
#     if ((r >= rows) or (c >= cols) or
#         ((r,c) in visited)):
#         return 0

#     if r == c:
#         return grid[r][c]

#     visited.add((r, c))
#     min_sum = min( min_sum, 0 + dfs(r+1, c, min_sum) + dfs(r, c+1, min_sum))
    

# for r in range(len(grid)):
#     for c in range(len(grid[0])):
#         dfs(r, c, min_sum)
# print(min_sum)
