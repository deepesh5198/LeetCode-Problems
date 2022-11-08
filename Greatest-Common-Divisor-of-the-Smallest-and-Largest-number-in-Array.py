def findGCD(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    smol = nums[0]
    large = nums[-1]
    
    gcd = float("-inf")
    if smol == large:
        return smol

    else:
        for i in range(1, smol + 1):
            if smol%i == 0 and large%i == 0:
                if gcd < i:
                    gcd = i
        return gcd

print(findGCD(nums = [2,5,6,9,10]))