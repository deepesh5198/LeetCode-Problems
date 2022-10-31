# Problem Description:

# You are given a string allowed consisting of distinct characters and an array
# of strings words. A string is consistent if all characters in the string appear
# in the string allowed.

# Return the number of consistent strings in the array words.

# EXAMPLE:
# Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
# Output: 2
# Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

def countConsistentStrings(allowed, words):
    allowed = set(allowed)
    count = 0
    for word in words:
        if not(set(word) - allowed):
            count +=1
            
    return count
print(countConsistentStrings(allowed = "ab", words = ["ad","bd","aaab","baa","badab"]))