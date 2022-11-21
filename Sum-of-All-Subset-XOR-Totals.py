# Problem Description:
# Example 1:

# Input: nums = [1,3]
# Output: 6
# Explanation: The 4 subsets of [1,3] are:
# - The empty subset has an XOR total of 0.
# - [1] has an XOR total of 1.
# - [3] has an XOR total of 3.
# - [1,3] has an XOR total of 1 XOR 3 = 2.

#   0 + 1 + 3 + 2 = 6

def subsetXORSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    def binary(x):
        x = [bit for bit in bin(x)[1:] if bit != 'b']
        bit_count = len(x)
        if bit_count != 5:
            x = ['0']*(5-bit_count) + x
        return x

    def xor(x, y):
        res = []
        for i,j in zip(x,y):
            if i==j:
                res.append('0')

            else:
                res.append('1')

        return res
    
    # making powerset
    x = len(nums)
    powerset = []
    masks = [1 << i for i in range(x)]
    total = 0
    for i in range(1 << x):
        powerset.append([j for mask, j in zip(masks, nums) if i & mask])
    
    # finding sum of all subset XOR totals
    for subset in powerset:
        if len(subset) == 1:
            total += subset[0]

        else:
            result = ['0']*5
            for n in subset:
                result = xor(result, binary(n))

            total += int("".join(result), base=2)
            
    return total