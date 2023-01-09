# Approach: Using stack, 
# HOw?: Create a pos, speed pair Array 
# sort in desc order
# iterate through each pair
# calculate time to reacht the target
# if time for current car is less than or equal to the previous car
# do not add it to stack
# else add it to stack
# finally return the length of that stack

def carFleet(target, position, speed) -> int:

    # create a stack
    stack = []

    # put the pos, speed in pairs
    pairs = [(i,j) for i,j in zip(position, speed)]

    # sort in reverse order (Desc)
    pairs.sort(reverse = True)

    # go through each pairs
    for p, s in pairs:

        # calculate time to reach the destination
        t = (target - p)/s

        # if stack is empty add the time
        if not stack:
            stack.append(t)
            
        # elif time for curr car is less than
        # or equal to the time in stack, do not
        # append it
        elif t <= stack[-1]:
            continue
            
        # else append it
        else:
            stack.append(t)

    return len(stack)