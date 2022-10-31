# Problem Description: Given Two Arrays of Strings, check if they are equal.

# # EXAMPLE:
# Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
# Output: true
# Explanation:
# word1 represents string "ab" + "c" -> "abc"
# word2 represents string "a" + "bc" -> "abc"
# The strings are the same, so return true.

def arrayStringsAreEqual(word1, word2):
    if "".join(word1) == "".join(word2):
        return True
    else:
        False