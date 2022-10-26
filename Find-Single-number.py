# Problem Description:
# Given a non-empty array of integers nums, every element
# appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

#EXAMPLE:
# Input: nums = [4,1,2,1,2]
# Output: 4
def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in set(nums):
        if nums.count(i) == 1:
            return i
        else:
            continue
        
print(singleNumber(nums=[4,1,2,1,2]))