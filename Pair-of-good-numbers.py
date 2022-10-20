#Problem Description:
# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.


# Example:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

def num_of_pairs(count):
    """
    Utility function to calculate pair count.
    :count: int
    
    """
    if count == 1:
        return 0

    elif count == 2:
        return 1

    else:
        return  num_of_pairs(count - 1) + (count-1)
        
def numIdenticalPairs(nums):
    
    """
    :type nums: List[int]
    :rtype: int
    """
    pair_count = 0
    
    for num in set(nums):
        if nums.count(num) <=1:
            continue
        else:
            pair_count += num_of_pairs(nums.count(num))

    return pair_count

print(numIdenticalPairs([1,2,1,3,1,3]))