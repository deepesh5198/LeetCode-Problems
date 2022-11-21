# Problem Description:
# Given an array of strings words, return the words that
# can be typed using letters of the alphabet on only one
# row of American keyboard like the image below.

# In the American keyboard:
# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".

# EXAMPLE:
# Input: words = ["Hello","Alaska","Dad","Peace"]
# Output: ["Alaska","Dad"]

def findWords(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    row1 = set("qwertyuiop")
    row2 = set("asdfghjkl")
    row3 = set("zxcvbnm")
    res = []
    
    for word in words:
        char_set = set(word.lower())
        if char_set.issubset(row1) or char_set.issubset(row2) or char_set.issubset(row3):
            res.append(word)


    return res

print(findWords(words = ["Hello","Alaska","Dad","Peace"]))