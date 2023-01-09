# You are given a string s and an integer k. You can choose any character of 
# the string and change it to any other uppercase English character. 
# You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you 
# can get after performing the above operations.

# Example:
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.

#Approach: Sliding Window
def characterReplacement(self, s: str, k: int) -> int:
    max_len = 0
    # need a mapping
    lookup = {}
    
    for c in set(s):
        lookup[c] = 0
    # l and r pointers
    l,r = 0,0

    while r < len(s):
        lookup[s[r]] += 1
        while (r - l+1) - max(lookup.values()) > k:
            lookup[s[l]] -=1
            l +=1

        max_len = max(max_len, (r - l+1))
        r += 1
        
    return max_len
