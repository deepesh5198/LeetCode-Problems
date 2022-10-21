def numberSmallerThan(nums):
    result = []
    for number in nums:
        result.append(len([num for num in nums if num < number]))
    return result

def numberSmallerThan(nums):
    result = []
    for number in nums:
        # result.append(nums.count(<number))
        pass
    return result


# print(numberSmallerThan([8,1,2,2,3]))
nums = [8,1,2,2,3]

nums.count()