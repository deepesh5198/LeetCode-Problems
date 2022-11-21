# Problem Description:
# You are given a string s of even length. Split this string into
#  two halves of equal lengths, and let a be the first half and b be the second half.

# Two strings are alike if they have the same number of vowels
# ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). 
# Notice that s contains uppercase and lowercase letters.

# Return true if a and b are alike. Otherwise, return false.

# Example:
# Input: s = "book"
# Output: true
# Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

def halvesAreAlike(self, s):
    """
    :type s: str
    :rtype: bool
    """

    l = len(s)
    a = s[:l//2]
    b = s[l//2:]
    left = 0
    right= 0
    vowels = "aeiouAEIOU"
    for v in set(a):
        if v in vowels:
            left += a.count(v)

    for v in set(b):
        if v in vowels:
            right += b.count(v)
            
    return (left == right)