def islandPerimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    def top_left_corner(i,j, peri):
        down = grid[i+1][j]
        right = grid[i][j+1]
        if (down) and (right):
            peri += 2

        elif (down ==1) or (right):
            peri += 3

        else:
            peri += 4
        return peri


    def top_right_corner(i,j,peri):
        left = grid[i][j-1]
        down = grid[i+1][j]
        if (down) and (left):
            peri += 2

        elif (down) or (left):
            peri += 3

        else:
            peri += 4

        return peri

    def bottom_left_corner(i, j, peri):
        up = grid[i-1][j]
        right = grid[i][j+1]
        if (up) and (right):
            peri += 2

        elif (up) or (right):
            peri += 3

        else:
            peri += 4

        return peri

    def bottom_right_corner(i,j,peri):
        up = grid[i-1][j]
        left = grid[i][j-1]
        if (up) and (left):
            peri += 2

        elif (up) or (left):
            peri += 3

        else:
            peri += 4

        return peri

    def left_edge(i,j,peri):
        up = grid[i-1][j]
        right = grid[i][j+1]
        down = grid[i+1][j]

        if ((up) and (down) and (right)):
            peri += 1

        elif (not(up) and (down) and (right)):
            peri += 2

        elif ((up) and not(down) and (right)):
            peri += 2

        elif ((up) and (down) and not(right)):
            peri += 2

        elif (not(up) and (down) and not(right)):
            peri += 3

        elif ((up) and not(down) and not(right)):
            peri += 3

        elif (not(up) and not(down) and (right)):
            peri += 3

        else:
            peri += 4

        return peri


    def top_edge(i,j,peri):
        right = grid[i][j+1]
        left = grid[i][j-1]
        down = grid[i+1][j]

        if ((left ) and (right) and (down)):
            peri += 1

        elif (not(left) and (right) and (down)):
            peri += 2

        elif ((left) and not(right) and (down)):
            peri += 2

        elif ((left ) and (right) and not(down)):
            peri += 2

        elif (not(left) and (right) and not(down)):
            peri += 3

        elif ((left ) and not(right) and not(down)):
            peri += 3

        elif (not(left ) and not(right) and (down)):
            peri += 3
        else:
            peri += 4

        return peri

    def right_edge(i,j,peri):
        up = grid[i-1][j]
        left = grid[i][j-1]
        down = grid[i+1][j]

        if ((up) and (down) and (left)):
            peri += 1

        elif (not(up) and (down) and (left)):
            peri += 2

        elif ((up) and not(down) and (left)):
            peri += 2

        elif ((up) and (down) and not(left)):
            peri += 2

        elif (not(up) and (down) and not(left)):
            peri += 3

        elif ((up) and not(down) and not(left)):
            peri += 3

        elif (not(up) and not(down) and (left)):
            peri += 3

        else:
            peri += 4

        return peri

    def bottom_edge(i,j,peri):
        up = grid[i-1][j]
        right = grid[i][j+1]
        left = grid[i][j-1]

        if ((left ) and (right) and (up)):
            peri += 1

        elif (not(left) and (right) and (up)):
            peri += 2

        elif ((left) and not(right) and (up)):
            peri += 2

        elif ((left ) and (right) and not(up)):
            peri += 2

        elif (not(left) and (right) and not(up)):
            peri += 3

        elif ((left ) and not(right) and not(up)):
            peri += 3

        elif (not(left ) and not(right) and (up)):
            peri += 3

        else:
            peri += 4

        return peri

    def in_the_middle(i,j,peri):
        up = grid[i-1][j]
        right = grid[i][j+1]
        left = grid[i][j-1]
        down = grid[i+1][j]

        if ((left ) and (right) and (up)) and (down):
            peri +=0

        elif (not(left) and (right) and (up)) and (down):
            peri += 1

        elif ((left) and not(right) and (up)) and (down):
            peri += 1

        elif ((left ) and (right) and not(up)) and (down):
            peri += 1

        elif ((left ) and (right) and (up)) and not(down):
            peri += 1

        elif (not(left) and not(right) and (up)) and (down):
            peri += 2

        elif ((left) and (right) and not(up)) and not(down):
            peri += 2

        elif (not(left) and (right) and not(up)) and (down):
            peri += 2

        elif ((left) and not(right) and (up)) and not(down):
            peri += 2

        elif ((left) and not(right) and not(up)) and (down):
            peri += 2

        elif (not(left) and (right) and (up)) and not(down):
            peri += 2

        elif ((left ) and not(right) and not(up)) and not(down):
            peri += 3

        elif (not(left ) and (right) and not(up)) and not(down):
            peri += 3

        elif (not(left ) and not(right) and (up)) and not(down):
            peri += 3

        elif (not(left ) and not(right) and not(up)) and (down):
            peri += 3

        else:
            peri += 4

        return peri

    peri = 0
    rows = len(grid)
    columns = len(grid[0])

    if rows == 1:
        if columns == 1:
            peri += 4
        else:
            i = 0
            for j in range(columns):
                if grid[i][j]:
                    # left corner
                    if j==0:
                        right = grid[i][j+1]
                        if right:
                            peri += 3

                        else:
                            peri +=4
                    # right corner
                    elif j == columns -1:
                        left = grid[i][j-1]
                        if left:
                            peri += 3

                        else:
                            peri += 4
                    # middle
                    elif 0 < j < columns:
                        left = grid[i][j-1]
                        right = grid[i][j+1]
                        if left and right:
                            peri += 2

                        elif left or right:
                            peri += 3

                        else:
                            peri += 4
                    else:
                        continue
                else:
                    continue
    elif columns == 1:
        j = 0
        for i in range(rows):
            if grid[i][j]:
                # top corner
                if i == 0:
                    down = grid[i+1][j]
                    if down:
                        peri += 3

                    else:
                        peri += 4

                # bottom corner
                elif i == rows - 1:
                    up = grid[i-1][j]
                    if up:
                        peri += 3

                    else:
                        peri += 4

                # middle
                elif 0 < i < rows:
                    up = grid[i-1][j]
                    down = grid[i+1][j]
                    if up and down:
                        peri += 2

                    elif up or down:
                        peri += 3

                    else:
                        peri += 4

                else:
                    continue
            else:
                continue

    else:
        for i in range(rows):
            for j in range(columns):
                if grid[i][j]:
                    # Case 1: Top-Left Corner
                    if i == 0 and j == 0:
                        peri = top_left_corner(i=i, j=j, peri=peri)

                    # Case 2: Top-Right Corner
                    elif (i == 0) and (j == columns-1):
                        peri = top_right_corner(i=i, j=j, peri=peri)

                    # Case 3: Bottom-Left corner 
                    elif (i == rows - 1) and (j == 0):
                        peri = bottom_left_corner(i=i, j=j, peri=peri)

                    # Case 4: Bottom-Right corner
                    elif (i == rows - 1) and (j ==(columns-1)):
                        peri = bottom_right_corner(i=i, j=j, peri= peri)

                    # Case 5: Left Edge
                    elif (0 < i < rows-1) and (j == 0):
                        peri = left_edge(i=i, j=j, peri=peri)

                    # Case 6: Top edge
                    elif (i == 0) and (0 < j < columns - 1):
                        peri = top_edge(i=i, j=j, peri=peri)

                    # Case 7: Right edge
                    elif (0 < i < rows-1) and (j == columns - 1):
                        peri = right_edge(i=i, j=j, peri=peri)

                    # Case 8: Bottom Edge
                    elif (i == rows - 1) and (0 < j < columns - 1):
                        peri = bottom_edge(i=i, j=j, peri=peri)

                    # Case 9: In the middle
                    elif (0 < i < rows - 1) and (0 < j < columns - 1):
                        peri = in_the_middle(i=i, j=j, peri=peri)

                else:
                    continue
            else:
                continue
    return peri


grid = [[0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [0,0,0,0]]

print(islandPerimeter(grid))