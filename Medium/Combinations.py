# Problem Description:
# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# You may return the answer in any order.

# EXAMPLE:
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

def combineV1(n, k):
    res = []
    stack = [(1,[])]

    while stack:
        start, combo = stack.pop()
        if len(combo) == k:
            res.append(combo)

        else:
            for i in range(start, n+1):
                newCombo = combo+[i]
                stack.append((i+1, newCombo))

    return res

print(combineV1(n=4, k=3))

def combineV2(n, k):
    res = []

    def recurse(start, combo):
        if len(combo) == k:
            res.append(combo[:])

        else:
            for i in range(start, n+1):
                combo.append(i)
                recurse(i+1, combo)

                combo.pop()
            return res

    return recurse(1, [])

print(combineV2(n=4, k=2))