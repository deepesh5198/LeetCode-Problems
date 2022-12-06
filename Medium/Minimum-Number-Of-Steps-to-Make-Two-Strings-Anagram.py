# Problem Description:
# Input: s = "leetcode", t = "practice"
# Output: 5
# Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters 
# to make t anagram of s.
import collections

def minSteps(s: str, t: str) -> int:
    S = collections.Counter(s)
    T = collections.Counter(t)

    return sum((S-T).values())


