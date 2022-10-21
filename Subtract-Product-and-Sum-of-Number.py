#Problem Description:
#Given an integer number n, return the difference between
# the product of its digits and the sum of its digits.

#EXAMPLE:
# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15

def subtractProductandSum(n:int):
    num_str = str(n)
    product = "*".join(num for num in num_str)
    sum = "+".join(num for num in num_str)
    
    return eval(product) - eval(sum)

print(subtractProductandSum(234))