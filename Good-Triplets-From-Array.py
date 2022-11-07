#Problem Description:
# Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

# A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

# 0 <= i < j < k < arr.length
# |arr[i] - arr[j]| <= a
# |arr[j] - arr[k]| <= b
# |arr[i] - arr[k]| <= c
# Where |x| denotes the absolute value of x.

# Return the number of good triplets.

# EXAMPLE:

# Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
# Output: 4
# Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].

def countGoodTriplets(self, arr, a, b, c):
    """
    :type arr: List[int]
    :type a: int
    :type b: int
    :type c: int
    :rtype: int
    """
    count = 0
    # for any array values of i, j, k range between:
    # i(min) = 0 to i(max) = len(array)-2
    # j(min) = 1 to j(max) = len(array)-1
    # k(min) = 2 to k(max) = len(array)
    
    for i in range(0, len(arr) - 2):
        for j in range(1, len(arr) -1):
            if i < j:
                for k in range(2, len(arr)):
                    if i< k and j < k:
                        if (abs(arr[i] - arr[j]) <= a)\
                            and(abs(arr[j] - arr[k]) <= b)\
                            and(abs(arr[i] - arr[k]) <= c):
                            count +=1
                    else:
                        continue
            else:
                continue
    return count