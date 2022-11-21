# Problem Description:
# You are given an integer array nums (0-indexed). In one operation, 
# you can choose an element of the array and increment it by 1.

# For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].
# Return the minimum number of operations needed to make nums strictly increasing.

# An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1.
# An array of length 1 is trivially strictly increasing.

# EXAMPLE:
# Input: nums = [1,1,1]
# Output: 3
# Explanation: You can do the following operations:
# 1) Increment nums[2], so nums becomes [1,1,2].
# 2) Increment nums[1], so nums becomes [1,2,2].
# 3) Increment nums[2], so nums becomes [1,2,3].

def minOperations(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    operations = 0
    length = len(nums)
    if length == 1:
        return 0

    for i in range(length - 1):
        if nums[i+1] > nums[i]:
            continue
        else:
            op = (nums[i] - nums[i+1]) + 1
            nums[i+1] += op
            operations += op
            
    return operations

print(minOperations([1,5,2,4,1]))