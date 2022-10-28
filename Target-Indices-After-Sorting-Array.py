# Problem Description

# Input: nums = [1,2,5,2,3], target = 2
# Output: [1,2]
# Explanation: After sorting, nums is [1,2*,2*,3,5].
# The indices where nums[i] == 2 are 1 and 2.


def targetIndices(nums, target): # The slow version
    # sort the array
    nums = sorted(nums)
    # initialize empty list to store indexes
    result = []
    
    # initialize i at 0
    i = 0
    
    # iterate till i != length of array
    # and i <= target
    while i != len(nums) and nums[i] <= target:
        if nums[i] == target:
            result.append(i)
        i+=1
    return result



def targetIndices2(nums, target): # the fast version
    """
    This method is gives less time complexity
    """
    # initialize empty list
    # for storing indexes
    result = []
    
    # sort the array
    nums.sort()
    
    # count target in sorted array
    count_of_target = nums.count(target)
    
    # if count of target is not 0
    if count_of_target != 0:
        
        # store the first index of target
        # in sorted array
        first_index = nums.index(target)
     
    # if count of target is 0
    # target doesn't exist in array   
    if count_of_target == 0:
        # simply return an empty list
        return []
    
    # if count of target is 1
    if count_of_target == 1:
        # just append the first index to the result
        # and return
        result.append(first_index)
        return result
    
    # else when count of target > 1
    else:
        # run the loop from first_index to the first_index + count of target
        # for example: [1,2,3,4,4,4,4,4,5,6], target = 4
        # count_of_target = 5, first_index = 3
        # so run the loop from index 3 to 7 (5+3 = 8 but range excludes 8th index) 
        for index in range(first_index, count_of_target + first_index):
            # append the indexes in result
            result.append(index)
        return result
print(targetIndices2(nums = [53,8,12,80,99,6,39,15,64,31,17,12,98,79,6,69,99,67,93,30,76,9,3,77,45,77], target = 99)) 