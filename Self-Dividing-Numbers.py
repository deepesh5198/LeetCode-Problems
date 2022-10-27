# Problem Description:
# A self-dividing number is a number that is divisible by every digit it contains.
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# A self-dividing number is not allowed to contain the digit zero.

# Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].

# EXAMPLE:
# Input: left = 1, right = 22
# Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]

def selfDividingNumbers(left, right):
    """
    :type left: int
    :type right: int
    :rtype: List[int]
    """
    result = []
    for i in range(left, right+1):
        str_num = str(i)
        if len(str_num) == 1:
            result.append(i)
        else:   
            for d in str_num:
                flag = True
                if int(d) != 0:
                    if i%int(d) == 0:
                        flag = True and flag
                        
                    else:
                        flag = not(flag)
                        break
                else:
                    flag = not(flag)  
                    break
                    
            if flag:
                result.append(i)
                
    return result

print(selfDividingNumbers(left = 1, right = 22))