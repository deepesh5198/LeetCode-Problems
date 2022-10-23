# Problem Description:
# You own a Goal Parser that can interpret a string command.
# The command consists of an alphabet of "G", "()" and/or "(al)"
# in some order. The Goal Parser will interpret "G" as the string
# "G", "()" as the string "o", and "(al)" as the string "al". The
# interpreted strings are then concatenated in the original order.

# Given the string command, return the Goal Parser's interpretation of command.

#EXAMPLE:
# Input: command = "G()(al)"
# Output: "Goal"
# Explanation: The Goal Parser interprets the command as follows:
# G -> G
# () -> o
# (al) -> al
# The final concatenated result is "Goal".

def goalParser(command):
    # make a queue of characters in command
    queue = [l for l in command]
    
    # initiate an empty list
    goal = []

    # run this loop till the queue gets empty
    while len(queue)!=0:
        # pop the element at index 0 from queue
        char = queue.pop(0)
        
        # check if the char is "G"
        if char == "G":
            #append it to goal 
            goal.append("G")

        # else check if the char is "("
        elif char == "(":
            
            # if char is "("
            # check if the next element in queue
            # is ")"
            if queue[0] == ")":
                # if true 
                # append "o" to goal
                goal.append("o")
                # and at index 0 from queue
                queue.pop(0)
                
            # if next element is not ")"
            elif queue[0] != ")":
                # pop at index 0 from queue
                queue.pop(0)
                
                # append "al" to goal
                goal.append("al")
                
                # pop at index 0 twice
                queue.pop(0)
                queue.pop(0)

    # join the goal list to make a word
    return "".join(goal)
print(goalParser("G()()()()(al)")) 