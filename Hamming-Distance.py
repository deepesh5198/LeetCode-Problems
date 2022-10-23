# Problem Description:
# The Hamming distance between two integers is the number of positions
# at which the corresponding bits are different.

# Given two integers x and y, return the Hamming distance between them.

# EXAMPLE:
# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑

def decToBinary(num):
    """
        a utility function to convert
        decimal number to a 4 bit binary
        vector
        :param num: int
        
    """
    binary = [d for d in bin(num)]
    while len(binary) != 5:
        binary.insert(binary.index('b'), '0')
    binary.remove('b')
    return binary

def hammingDistance(x,y):
    """
        function to calculate hamming distance
        between two numbers
        :type x: int
        :type y: int
        :rtype: int
    """
    x = decToBinary(x)
    y = decToBinary(y)
    
    hamming_distance = 0
    for i,j in zip(x,y):
        if i != j:
            hamming_distance +=1
            
    return hamming_distance

print(hammingDistance(1,4))
       
     
    