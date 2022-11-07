# Problem Description:
# You are given a 0-indexed string s that has lowercase English letters
# in its even indices and digits in its odd indices.

# Input: s = "a1c1e1"
# Output: "abcdef"

def replaceDigits(s):
    """
    :type s: str
    :rtype: str
    """
    result = []
    
    for char in s:
        if char.isalpha():
            result.append(char)
            
        else:
            index = ord(result[-1])
            result.append(chr(index + int(char)))
            
    return "".join(result)

print(replaceDigits(s = "a1b2c3d4e"))
# output: 'abbdcfdhe' 