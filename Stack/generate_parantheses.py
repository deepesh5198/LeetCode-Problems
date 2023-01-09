# Approach: Backtracking (Very Easy)

def generateParenthesis(n: int):
    # base case: iff nClose == nOpen == n
    # add close P: if nClose < n
    # add open P: if nClose > nOpen

    stack = []
    res = []

    def backtrack(nOpen, nClose):
        # base case
        if nOpen == nClose == n:
            res.append("".join(stack))
            return

        if nClose < n:
            stack.append("(")
            backtrack(nOpen, nClose+1)
            stack.pop()

        if nOpen < nClose:
            stack.append(")")
            backtrack(nOpen+1, nClose)
            stack.pop()

    backtrack(0,0)
    return res