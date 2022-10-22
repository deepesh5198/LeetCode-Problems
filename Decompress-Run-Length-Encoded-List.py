# Problem Description
# We are given a list nums of integers representing a list compressed with run-length encoding.
# Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).
# For each such pair, there are freq elements with value val concatenated in a sublist.
# Concatenate all the sublists from left to right to generate the decompressed list.

# Return the decompressed list.

# EXAMPLE:
# Input: nums = [1,2,3,4]
# Output: [2,4,4,4]
# Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
# The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
# At the end the concatenation [2] + [4,4,4] is [2,4,4,4].
    

def decompress(nums):
    result = []
    
    while nums:
        pair = nums[:2]
        freq = pair[0]
        value = pair[1]
        result = result + [value]*freq
        nums = nums[2:]
    return result

print(decompress([1,2,3,4]))