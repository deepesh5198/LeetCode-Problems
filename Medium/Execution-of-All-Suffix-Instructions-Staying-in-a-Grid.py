# There is an n x n grid, with the top-left cell at (0, 0) and the 
# bottom-right cell at (n - 1, n - 1). You are given the integer n 
# and an integer array startPos where startPos = [startrow, startcol] 
# indicates that a robot is initially at cell (startrow, startcol).

# You are also given a 0-indexed string s of length m where s[i] is 
# the ith instruction for the robot: 'L' (move left), 'R' (move right), 
# 'U' (move up), and 'D' (move down).

# The robot can begin executing from any ith instruction in s. 
# It executes the instructions one by one towards the end of s 
# but it stops if either of these conditions is met:

# The next instruction will move the robot off the grid.
# There are no more instructions left to execute.
# Return an array answer of length m where answer[i] is the number 
# of instructions the robot can execute if the robot begins executing 
# from the ith instruction in s.

# EXAMPLE:
# Input: n = 3, startPos = [0,1], s = "RRDDLU"
# Output: [1,5,4,3,1,0]
# Explanation: Starting from startPos and beginning execution from the ith instruction:
# - 0th: "RRDDLU". Only one instruction "R" can be executed before it moves off the grid.
# - 1st:  "RDDLU". All five instructions can be executed while it stays in the grid and ends at (1, 1).
# - 2nd:   "DDLU". All four instructions can be executed while it stays in the grid and ends at (1, 0).
# - 3rd:    "DLU". All three instructions can be executed while it stays in the grid and ends at (0, 0).
# - 4th:     "LU". Only one instruction "L" can be executed before it moves off the grid.
# - 5th:      "U". If moving up, it would move off the grid.

def executeInstructions(n, startPos, s):
    """
    :type n: int
    :type startPos: List[int]
    :type s: str
    :rtype: List[int]
    """
    res = []
    l = len(s)
    for i in range(l):
        count = 0
        pos = startPos.copy()
        j = i
        for move in s[j:]:
            if move == 'R':
                pos[1] += 1
                if 0 <= pos[0] <= n-1 and 0 <= pos[1] <= n-1:
                    count +=1
                    j += 1
                else:
                    res.append(count)
                    break

            elif move == 'L':
                pos[1] -=1
                if 0 <= pos[0] <= n-1 and 0 <= pos[1] <= n-1:
                    count += 1
                    j += 1
                else:
                    res.append(count)
                    break

            elif move == 'U':
                pos[0] -= 1
                if 0 <= pos[0] <= n-1 and 0 <= pos[1] <= n-1:
                    count += 1
                    j += 1
                else:
                    res.append(count)
                    break

            else:
                pos[0] += 1
                if 0 <= pos[0] <= n-1 and 0 <= pos[1] <= n-1:
                    count += 1
                    j += 1
                else:
                    res.append(count)
                    break
            
        else:
            res.append(count)

    return res

print(executeInstructions(n = 1, startPos = [0,0], s = "LRUD"))