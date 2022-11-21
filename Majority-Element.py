# Problem Description:
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than
# ⌊n / 2⌋ times. You may assume that the majority element always
# exists in the array.

# EXAMPLE:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    l = len(nums)
    res = set(nums[:l//2]).intersection(set(nums[l//2:]))
    
    if res:
        return res.pop()
    else:
        return nums[-1]