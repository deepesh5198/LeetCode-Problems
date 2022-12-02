# Problem description:
# Given a string s, you can transform every letter individually to be lowercase 
# or uppercase to create another string.

# Return a list of all possible strings we could create. Return the output in any order.

# EXAMPLE:
# Input: s = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]

def letterCasePermutation(s):
    res = [""]

    # for every character in s
    for c in s:
        # empty list
        t=[]

        # if c is alpha
        if c.isalpha():
            # then to each string in result list
            # concate the upper and lower case of the character c
            for r in res:   
                t.append(r+c.upper())
                t.append(r+c.lower())

        # if c is a number
        else:
            # then concate that number to
            # each of the strings in result list
            for r in res:
                t.append(r+c)

        # update res as t
        res = t
        
    return res