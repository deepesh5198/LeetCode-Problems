# Problem Description: Given an nums "nums". We define a running sum of
# an nums as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of "nums".


#EXAMPLE:

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

def runningSumOfArray(nums):

    for i,val in enumerate(nums):
        if i ==0:
            continue
        else:
            nums[i] = val + nums[i-1]
            
    return nums
    
print(runningSumOfArray([1,2,3,4]))