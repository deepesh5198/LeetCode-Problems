# Given an integer array nums of length n where all the integers of 
# nums are in the range [1, n] and each integer appears once or twice, 
# return an array of all the integers that appears twice.

# You must write an algorithm that runs in O(n) time and uses only 
# constant extra space.

# EXAMPLE:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]

def findDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    nums.sort()
    res = []
    l = len(nums)
    i = 0
    while i < l:
        if i < l -1:
            # print(i)
            if nums[i] == nums[i+1]:
                res.append(nums[i])
                i +=2
            else:
                i +=1
                # print(i)
        else:
            break
    return res

print(findDuplicates(nums = [4,3,2,7,8,2,3,1]))