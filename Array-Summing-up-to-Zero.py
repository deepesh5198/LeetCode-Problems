# Given an integer n, return any array containing n unique
# integers such that they add up to 0.

# EXAMPLE:
# Input: n = 5
# Output: [-7,-1,1,3,4]
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

def sumZero(n):
    """
    :type n: int
    :rtype: List[int]
    """
    res = []
    if n == 1:
        return [0]
    
    if n%2 == 0:
        for i in range(1,(n//2) +1):
            res.append(-i)
            res.append(i)
        
    elif n%2 !=0:
        res.append(0)
        for i in range(1,(n//2) +1):
            res.append(-i)
            res.append(i)
    return res