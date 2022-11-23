# Problem Description
# A parentheses string is valid if and only if:

# It is the empty string,
# It can be written as AB (A concatenated with B), where A and B are 
# valid strings, or It can be written as (A), where A is a valid string.
# You are given a parentheses string s. In one move, you can insert a 
# parenthesis at any position of the string.

# For example, if s = "()))", you can insert an opening parenthesis 
# to be "(()))" or a closing parenthesis to be "())))".
# Return the minimum number of moves required to make s valid.

# EXAMPLE:
# Input: s = "())"
# Output: 1

def minAddToMakeValid(s):
    """
    :type s: str
    :rtype: int
    """
    # initialize an empty stack
    stack = []

    # go through each parantheses in s
    for p in s:
        # if stack is empty append the paranthesis to stack
        if not stack:
            stack.append(p)
        
        # else if top of stack is "("
        # and current paranthesis is ")"
        # pop the from stack
        elif stack[-1] == "(" and p == ")":
            stack.pop()

        # else append to stack
        else:
            stack.append(p)
            
    # return the length of stack
    return len(stack)

    