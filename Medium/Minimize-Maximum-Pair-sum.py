# Problem Description:
# The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum 
# is the largest pair sum in a list of pairs.

# For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair 
# sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.
# Given an array nums of even length n, pair up the elements of nums into 
# n / 2 pairs such that:

# Each element of nums is in exactly one pair, and
# The maximum pair sum is minimized.
# Return the minimized maximum pair sum after optimally pairing up the elements.

# EXAMPLE:
# Input: nums = [3,5,2,3]
# Output: 7
# Explanation: The elements can be paired up into pairs (3,3) and (5,2).
# The maximum pair sum is max(3+3, 5+2) = max(6, 7) = 7.

def minPairSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # sort the nums array
    nums.sort()

    # initialize i at 0
    i = 0

    # initialize j at last index
    j = len(nums)-1

    # initialize m at 0
    m = 0
    
    # while i is not > j
    while i <= j:
        # compare with old m value
        # replace it with the max value
        m = max(m, nums[i] + nums[j])

        # increament i
        i +=1

        # decreament j
        j -=1
        
    return m