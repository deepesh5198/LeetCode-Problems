# Problem Description:

# Input: n = 3
# Output: 2
# Explanation: arr = [1, 3, 5]
# First operation choose x = 2 and y = 0, this leads arr to be [2, 3, 4]
# In the second operation choose x = 2 and y = 0 again, thus arr = [3, 3, 3].

def minOperations(n):
    """
    :type n: int
    :rtype: int
    """ 
    arr = [(i*2)+1 for i in range(n)]
    i = n//2
    count = 0
    mid = arr[i]

    for n in arr:
        if n < mid:
            ops = mid - n
            count += ops/2
        elif n > mid:
            ops = n - mid
            count += ops/2
        else:
            continue
    return int(count)

print(minOperations(6))