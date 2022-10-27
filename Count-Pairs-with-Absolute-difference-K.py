#Problem Description:

# Input: nums = [1,2,2,1], k = 1
# Output: 4
# Explanation: The pairs with an absolute difference of 1 are:
# - [1*,2*,2,1]
# - [1*,2,2*,1]
# - [1,2*,2,1*]
# - [1,2,2*,1*]

def countKdifference2(nums, k):
    count = 0
    for i in range(len(nums) -1):
        for j in range(i+1 , len(nums), 1):
            if abs(nums[i] - nums[j]) == k:
                count+=1
                print(i,j)
            else:
                continue
    return count
print(countKdifference2(nums = [3,2,1,5,4], k = 2))
        
