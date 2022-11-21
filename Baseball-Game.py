def calPoints(ops):
    """
    :type operations: List[str]
    :rtype: int
    """
    stack = []
    for c in ops:
        if c == "+":
            stack.append(stack[-1] + stack[-2])
        elif c == "D":
            stack.append(stack[-1]*2)
        elif c == "C":
            stack.pop(-1)

        else:
            stack.append(int(c))

    return sum(stack)

print(calPoints(["5","-2","4","C","D","9","+","+"]))
