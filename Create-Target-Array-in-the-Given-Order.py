# Problem Description
# Given two arrays of integers nums and index. Your task is to create target array under the following rules:
# Initially target array is empty.
# From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
# Repeat the previous step until there are no elements to read in nums and index.
# Return the target array.

# It is guaranteed that the insertion operations will be valid.

#EXAMPLE:
# Input: nums = [1,2,3,4,0], index = [0,1,2,3,0]
# Output: [0,1,2,3,4]
# Explanation:
# nums       index     target
# 1            0        [1]
# 2            1        [1,2]
# 3            2        [1,2,3]
# 4            3        [1,2,3,4]
# 0            0        [0,1,2,3,4]

def createTargetArray(nums, index):
    if len(index) == 1:
        return nums
    
    else:    
        result = []
        for val, i in zip(nums, index):
            result.insert(i, val)
        return result
print(createTargetArray(nums = [1,2,3,4,0], index = [0,1,2,3,0]))
    
    