# Problem Description:

# Input: arr = [1,4,2,5,3]
# Output: 58
# Explanation: The odd-length subarrays of arr and their sums are:
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15
# If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

def sumOfOddArrays(arr):
    length = len(arr) + 1
    total = sum(arr)
    for odd_num in range(3, length, 2):
        for i in range(length - odd_num):
            total += sum(arr[i:odd_num + i])
                
    return total
    
print(sumOfOddArrays([1,4,2,5,3,5]))