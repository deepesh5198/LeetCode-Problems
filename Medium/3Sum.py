# Problem Desciption
# Given an integer array nums, return all the triplets [nums[i], nums[j], 
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of 
# the triplets does not matter.

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    # sort the array
    nums.sort()

    for i, a in enumerate(nums):
        # avoiding duplicates
        if i > 0 and nums[i - 1] == a:
            continue

        l, r = i+1 , len(nums) - 1

        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1

            elif threeSum < 0:
                l += 1

            else:
                res.append([a, nums[l], nums[r]])
                # [-2,-2,0,0,2,2]
                l += 1

                # increase value of left pointer
                # unless nums[l] != nums[l-1]
                while nums[l] == nums[l-1] and l < r:
                    l += 1
    return res