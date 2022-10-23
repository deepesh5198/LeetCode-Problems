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

def decToBinary(num1,num2):
    """
        a utility function to convert
        decimal number to a 4 bit binary
        vector
        :param num: int
        
    """
    bin1 = [d for d in bin(num1).replace('b','')]
    bin2 = [d for d in bin(num2).replace('b','')]
    print(bin1, bin2)
    
    if max(num1, num2) == num1:
        while len(bin2) != len(bin1):
            bin2.insert(0,'0')
        return bin1, bin2    
        
    elif max(num1 , num2) == num2:
        while len(bin1) != len(bin2):
            bin1.insert(0,'0')
        return bin1, bin2
        
    else:
        return bin1, bin2
        

def hammingDistance(x,y):
    """
        function to calculate hamming distance
        between two numbers
        :type x: int
        :type y: int
        :rtype: int
    """
    x,y = decToBinary(x,y)
    
    if max(x,y) == x:
        while len(y) != len(x):
            y.insert(0,'0')
            
    else:
        while len(x) != len(y):
            x.insert(0,'0')
    print(x, y)
    
    hamming_distance = 0
    for i,j in zip(x,y):
        if i != j:
            hamming_distance +=1
            
    return hamming_distance

print(hammingDistance(3,5))
       
     
    