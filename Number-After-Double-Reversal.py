# Problem Description:
# Reversing an integer means to reverse all its digits.

# For example, reversing 2021 gives 1202. 
# Reversing 12300 gives 321 as the leading zeros are not retained.
# Given an integer num, reverse num to get reversed1,
# then reverse reversed1 to get reversed2.
# Return true if reversed2 equals num. Otherwise return false.

# EXAMPLE:
# Input: num = 526
# Output: true
# Explanation: Reverse num to get 625, then reverse 625 to get 526, which equals num.

def isSameAfterReversals(self, num):
    """
    :type num: int
    :rtype: bool
    """
    num_str = str(num)
    num_str = str(int(num_str[::-1]))
    num_str = num_str[::-1]

    return int(num_str) == num