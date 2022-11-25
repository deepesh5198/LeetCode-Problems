# Given an array of distinct integers candidates and
# a target integer target, return a list of all unique 
# combinations of candidates where the chosen numbers sum 
# to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited 
# number of times. Two combinations are unique if the frequency 
# of at least one of the chosen numbers is different.

# EXAMPLE:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.


def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    ans = []
    l = len(candidates)
    
    # using backtracking
    def backtrack(current, current_sum, index):

        # base case 1
        if current_sum > target:
            return
        
        # base case 2
        if current_sum == target:
            ans.append(current)
            return
        
        # recursion case
        else:
            for i in range(index, l):
                backtrack(
                    current + [candidates[i]],
                    current_sum + candidates[i],
                    i
                )
    backtrack([],0,0)
    return ans