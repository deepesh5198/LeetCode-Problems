# Problem Description:
# You are given a string s formed by digits and '#'.
# We want to map s to English lowercase characters as follows:

# Characters ('a' to 'i') are represented by ('1' to '9') respectively.
# Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
# Return the string formed after mapping.

# The test cases are generated so that a unique mapping will always exist.


# EXAMPLE:
# Input: s = "10#11#12"
# Output: "jkab"
# Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

def freqAlphabets(s):
    """
    :type s: str
    :rtype: str
    """
    pass

    res = ""
    i = 0
    l = len(s)
    while i < l:
        if i == l-1:
            res += chr(int(s[i])+96)
            return res

        elif (i < l-2) and s[i+2] == '#':
            res += chr(int(s[i:i+2])+96)
            i += 3

        else:
            res += chr(int(s[i])+96)
            i += 1
    return res

print(freqAlphabets(s = "10#22#12#"))