# Problem Description:
# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# APPROACH:
# Sliding Window: using a set to store characters already seen, and removing from the set
# if seen again.
# when seen again update Left pointer
# otherwise update right pointer

def lengthOfLongestSubstring(s: str) -> int:
    l,r = 0,0
    seen = set()
    max_len = 0
    if len(s) == 1:
        return 1

    while r < len(s):
        
        if s[r] in seen:
            seen.remove(s[l])
            l += 1
            max_len = max(r-l, max_len)

        else:
            seen.add(s[r])
            r += 1
            max_len = max(r-l, max_len)

    return max_len