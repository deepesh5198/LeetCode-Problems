# Problem Description:
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Approach: straight forward Stack approach

def isValid(s: str) -> bool:
    stack = []

    for c in s:
        if not stack:
            stack.append(c)

        elif c == ")" and stack[-1] == "(":
            stack.pop()
        
        elif c == "}" and stack[-1] == "{":
            stack.pop()

        elif c == "]" and stack[-1] == "[":
            stack.pop()

        else:
            stack.append(c)

    if not stack:
        return True

    else:
        return False