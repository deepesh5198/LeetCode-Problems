# Problem Description:
# Given a string s, sort it in decreasing order based on the frequency of the characters. 
# The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them

# EXAMPLE:
# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.


def frequencySort(s):
    # make a set of chars in string
    char_set = set(s)

    # create a dictionary
    d = {}

    # go over each char in in character set
    for c in char_set:
        # map the character with its
        # count in the dictionary
        d[c] = s.count(c)

    # make list of (strings of char of length equal to the count)
    # e.g: if count of 'e' = 4, then list will contain 'e'*4 (i.e., 'eeee')
    items = [c*d[c] for c in d.keys()]

    # sort the above list according to their lengths
    # in decending order
    res = sorted(
        items, 
        key=lambda x: len(x),
        reverse=True
        )
    
    # join the res list and return
    return "".join(res)

print(frequencySort("tree"))