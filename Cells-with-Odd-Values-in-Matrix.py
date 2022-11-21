def oddCells(m, n, indices):
    """
    :type m: int
    :type n: int
    :type indices: List[List[int]]
    :rtype: int
    """
    count = 0
    matrix = [[0]*n for _ in range(m)]
    for i in indices:
        for j in range(n):
            matrix[i[0]][j] += 1

        for k in range(m):
            matrix[k][i[1]] += 1
                
    for row in range(m):
        for col in range(n):
            if matrix[row][col]%2 != 0:
                count +=1
    return count