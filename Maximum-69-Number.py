# Problem Description
# You are given a positive integer num consisting only of digits 6 and 9.

# Return the maximum number you can get by changing at most one digit
# (6 becomes 9, and 9 becomes 6).

# EXAMPLE:
# Input: num = 9669
# Output: 9969
# Explanation: 
# Changing the first digit results in 6669.
# Changing the second digit results in 9969.
# Changing the third digit results in 9699.
# Changing the fourth digit results in 9666.
# The maximum number is 9969.
 
def maximum69Number (num):
    """
    :type num: int
    :rtype: int
    """
    res = []
    if num in (9, 99, 999, 9999):
        return num
    for i in [1000, 100, 10, 1]:
        if i != 1:
            print(i)
            if ((num//i)%10) == 0:
                continue
                
            elif ((num//i)%10) == 6:
                res.append(num + 3*i)
                
            else:
                res.append(num - 3*i)

        else:
            if num%10 == 6:
                res.append(num + 3)

            else:
                res.append(num - 3)

    return res

print(maximum69Number(9969))
