# A valid parentheses string is either empty "", "(" + A + ")", or A + B,
# where A and B are valid parentheses strings, and + represents string concatenation.

# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string s is primitive if it is nonempty, and there does not
# exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

# Given a valid parentheses string s, consider its primitive decomposition:
# s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

# Return s after removing the outermost parentheses of every 
# primitive string in the primitive decomposition of s.

#EXAMPLE:
# Input: s = "(()())(())"
# Output: "()()()"
# Explanation: 
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

result = []
def removeParanthases(s:str):
    s = [i for i in s]
    print(s)
    result = []
    while s:
        if s[0] == "(":
            if s[1] == "(":
                s.pop(0)
                result.append("(")
                s.pop(0)
                
            else:
                result.append("()")
                s.pop(0)
                s.pop(0)
                
        elif s[0] == ")":
            if s[1] == ")":
                s.pop(0)
                result.append(")")
                s.pop(0)
                
            else:
                result.append(")(")
                s.pop(0)
                s.pop(0)

    return "".join(result)
print(removeParanthases("()()"))