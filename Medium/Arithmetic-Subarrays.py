# Problem Description:
# A sequence of numbers is called arithmetic if it consists of at least two elements, 
# and the difference between every two consecutive elements is the same. More formally, 
# a sequence s is arithmetic if and only if s[i+1] - s[i] == s[1] - s[0] for all valid i.

# For example, these are arithmetic sequences:

# 1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9
# The following sequence is not arithmetic:

# 1, 1, 2, 5, 7
# You are given an array of n integers, nums, and two arrays of m integers each, l and r, 
# representing the m range queries, where the ith query is the range [l[i], r[i]]. 
# All the arrays are 0-indexed.

# Return a list of boolean elements answer, where answer[i] is true if the subarray 
# nums[l[i]], nums[l[i]+1], ... , nums[r[i]] can be rearranged to form an arithmetic sequence, 
# and false otherwise.

# EXAMPLE:
# Input: nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]
# Output: [true,false,true]
# Explanation:
# In the 0th query, the subarray is [4,6,5]. This can be rearranged as [6,5,4], 
# which is an arithmetic sequence.
# In the 1st query, the subarray is [4,6,5,9]. 
# This cannot be rearranged as an arithmetic sequence.
# In the 2nd query, the subarray is [5,9,3,7]. This can be rearranged as [3,5,7,9], 
# which is an arithmetic sequence.

from __future__ import annotations
from typing import List

def checkArithmeticSubarrays(nums: List[int], l: List[int], r: List[int]) -> List[bool]:
    # a stack to store list
    stack = []

    # a flag to be stored in stack
    flag = True

    # take i, j values from each
    # l and r
    for i,j in zip(l,r):
        # get the array and sort it
        sub_arr = sorted(nums[i: j+1], reverse=True)

        # get index values till len(sub_array)-2
        for k in range(len(sub_arr)-1):
            # if k = 0
            # calculate the difference
            if k == 0:
                diff = abs(sub_arr[k] - sub_arr[k+1])

            # else compare the difference with new difference
            elif diff == abs(sub_arr[k] - sub_arr[k+1]):
                continue

            # if difference is not equal set the flag as False
            else:
                flag = False
            
        # append the flag to stack
        stack.append(flag)
        
        # again set the flag as True
        if not flag:
            flag = True
            
    # return the stack of booleans
    return stack