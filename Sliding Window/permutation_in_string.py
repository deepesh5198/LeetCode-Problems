# Problem Description:
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

# Example:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Approach: Counter + Sliding window

from collections import Counter
def checkInclusion(s1: str, s2: str) -> bool:
    s1_map = Counter(s1)

    win_size = len(s1)

    for i in range(len(s2)):
        try:
            s2_map = Counter(s2[i:i+win_size])
            if s1_map == s2_map:
                return True
            else:
                continue
        except:
            return False