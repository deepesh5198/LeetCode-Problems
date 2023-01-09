# Problem Description:
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

# Approach: Stack
def evalRPN(tokens) -> int:
    stack = []

    for c in tokens:
        if not stack:
            stack.append(c)

        elif c in "+-*/":
            b = stack.pop()
            a = stack.pop()
            stack.append(str(int(eval(a+c+b))))

        else:
            stack.append(c)

    ans = stack.pop()
    return int(eval(ans))