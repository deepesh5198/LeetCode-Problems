def dailyTemperatures(temperatures):
    # create an empty stack
    stack = []
    # create a result array of 0s
    res = [0]*len(temperatures)

    # iterate through temperatures list
    for i, t in enumerate(temperatures):
        # go through stack 
        # if top of stack's [1] position
        # is less than curr temperature
        while stack and stack[-1][1] < t:
            # pop the stack's top
            p = stack.pop()
            # in result at position of popped element
            # put the distance between current and the popped element
            res[p[0]] = (i - p[0])

        # append the new temperature in the stack
        stack.append((i,t))
            
    return res