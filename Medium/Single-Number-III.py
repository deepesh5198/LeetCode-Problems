# Problem statement:
# Given an integer array nums, in which exactly two elements appear 
# only once and all the other elements appear exactly twice. Find the 
# two elements that appear only once. You can return the answer in any order.

# You must write an algorithm that runs in linear runtime complexity and 
# uses only constant extra space.

# EXAMPLE:
# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]
# Explanation:  [5, 3] is also a valid answer.

def singleNumberV1(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    return [x for x in nums if nums.count(x) == 1]
# print(singleNumberV1(nums = [-1,0]))

def singleNumberV2(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    nums = sorted(nums, key=lambda x: nums.count(x))
    return nums
# print(singleNumberV2(nums = [1,2,1,3,2,5]))

def singleNumberV3(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    num_set = set(nums)
    s = sorted(num_set, key=lambda x: nums.count(x))
    return s[:2]
# print(singleNumberV3(nums = [1,2,1,3,2,5]))

# With Much less TIME COMPLEXITY
def singleNumberV4(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    stack = []
    nums.sort()
    for n in nums:
        if not stack:
            stack.append(n)
        elif stack[-1] == n:
            stack.pop()
        else:
            stack.append(n)
    return stack

print(singleNumberV4(nums = [1,2,1,3,2,5]))
