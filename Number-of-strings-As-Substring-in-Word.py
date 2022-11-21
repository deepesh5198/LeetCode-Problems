# Problem Description:
# Given an array of strings patterns and a string word, return the
# number of strings in patterns that exist as a substring in word.

# A substring is a contiguous sequence of characters within a string.

# EXAMPLE:
# Input: patterns = ["a","abc","bc","d"], word = "abc"
# Output: 3
# Explanation:
# - "a" appears as a substring in "abc".
# - "abc" appears as a substring in "abc".
# - "bc" appears as a substring in "abc".
# - "d" does not appear as a substring in "abc".
# 3 of the strings in patterns appear as a substring in word.

def numOfStrings(patterns, word):
    count = 0
    word_len = len(word)
    for p in patterns:
        res = []
        z = len(p)
        for i in range(word_len):
            res.append(word[i:z+i])

        if p in res:
            count +=1
    return count

print(numOfStrings(patterns = ["a", "ab", "bc", "abc", "d"], word = "abc"))