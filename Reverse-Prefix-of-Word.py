# Problem Description
# Input: word = "abcdefd", ch = "d"
# Output: "dcbaefd"
# Explanation: The first occurrence of "d" is at index 3. 
# Reverse the part of word from 0 to 3 (inclusive),
# the resulting string is "dcbaefd".

def reversePrefix(word, ch):
    """
    :type word: str
    :type ch: str
    :rtype: str
    """
    if ch in word:
        # initialize an empty string
        res = ""
        # find the index of the ch
        j = word.index(ch)
        # append reverse substring of word
        # (from j to 0th index) to res
        res += word[j::-1]

        # then append other half substring of word
        # as it is to the res
        res += word[j+1:]

        # return res
        return res

    else:
        # if ch not in word, return the word
        return word

print(reversePrefix(word = "abcdefd", ch = "d"))

