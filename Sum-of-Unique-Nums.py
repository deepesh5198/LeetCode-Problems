# Problem Description
# You are given an integer array nums. The unique elements of an array are the elements
# that appear exactly once in the array.
# Return the sum of all the unique elements of nums.

# Input: nums = [1,2,3,2]
# Output: 4
# Explanation: The unique elements are [1,3], and the sum is 4.

def sumOfUnique(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = 0
    unique = set(nums)
    for n in unique:
        if nums.count(n) == 1:
            res +=n
            
    return res
        