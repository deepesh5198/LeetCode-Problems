# Problem: Flip the image

#EXAMPLE:
# Input: image = [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

def fliptheimage(image):
    pass
    # return vector]
    return [list(reversed([0 if i==1 else 1 for i in vector])) for vector in image]

print(fliptheimage([[1,1,0],[1,0,1],[0,0,0]]))