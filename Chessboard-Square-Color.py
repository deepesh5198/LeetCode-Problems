# Problem Description:
# You are given coordinates, a string that represents the coordinates
# of a square of the chessboard. Below is a chessboard for your reference.

# Return true if the square is white, and false if the square is black.

# The coordinate will always represent a valid chessboard square.
# The coordinate will always have the letter first, and the number second.

# EXAMPLE:
# Input: coordinates = "a1"
# Output: false
# Explanation: From the chessboard above, the square with coordinates "a1" is black, so return false.

def squareIsWhiteV1(self, coordinates):
    """
    :type coordinates: str
    :rtype: bool
    """
    chessboard = {  0: {'1':False,
                        '2':True,
                        '3':False,
                        '4':True,
                        '5':False, 
                        '6':True, 
                        '7':False, 
                        '8':True},
                    1: {'1':True,
                        '2':False,
                        '3':True,
                        '4':False, 
                        '5':True, 
                        '6':False, 
                        '7':True,
                        '8':False}
                    }
    if ord(coordinates[0])%2!=0:
        return chessboard[0][coordinates[1]]
    
    else:
        return chessboard[1][coordinates[1]]

# Alternate Solution
def squareIsWhiteV2(self, coordinates):
    """
    :type coordinates: str
    :rtype: bool
    """
    if ord(coordinates[0])%2!=0:
        if int(coordinates[1])%2==0:
            return True
        else:
            return False
    
    else:
        if int(coordinates[1])%2==0:
            return False
        else:
            return True