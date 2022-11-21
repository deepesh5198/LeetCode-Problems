# Problem Statement:
# Given a string s, return true if s is a good string, or false otherwise.
# A string s is good if all the characters that appear in s have the same
# number of occurrences (i.e., the same frequency).

# EXAMPLE:
# Input: s = "abacbc"
# Output: true
# Explanation: The characters that appear 
# in s are 'a', 'b', and 'c'. All characters occur 2 times in s.


def areOccurrencesEqual(self, s):
    """
    :type s: str
    :rtype: bool
    """
    count = s.count(s[0])
    char_set = set(s[1:])
    res = True
    for c in char_set:
        if s.count(c) == count:
            continue
        else:
            res = False
            break
            
    return res
        

