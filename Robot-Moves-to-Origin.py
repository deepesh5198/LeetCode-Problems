# Problem Description:
# Input: moves = "UD"
# Output: true
# Explanation: The robot moves up once, and then down once.
# All moves have the same magnitude, so it ended up at the
# origin where it started. Therefore, we return true.

# Solution: You come back to the same point if
# (Number of steps forward = Number of steps backward) and (Number of steps right = Number of steps left)
# 
def robotMoves(moves):
    if (moves.count("R") == moves.count("L"))\
        and (moves.count("D") == moves.count("U")):
        return True
    else:
        return False

print(robotMoves("RRDD"))
