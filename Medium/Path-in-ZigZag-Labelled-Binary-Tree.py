# Problem Description:
# In an infinite binary tree where every node has two children, 
# the nodes are labelled in row order.

# In the odd numbered rows (ie., the first, third, fifth,...), 
# the labelling is left to right, while in the even numbered rows 
# (second, fourth, sixth,...), the labelling is right to left.

# Given the label of a node in this tree, return the labels in 
# the path from the root of the tree to the node with that label.

# EXAMPLE:
# Input: label = 14
# Output: [1,3,4,14]

def pathInZigZagTree(label):
    # level = -1
    # total = 0
    level, total = -1, 0

    # while level > total
    while label > total:
        # go to next level
        level += 1
        
        # increament the total
        # add the 2^level at each iteration
        total += (2 ** level)
    
    # We come out of loop with total > label
    
    # now we move back to the level
    # at which total was last smaller than label
    level -= 1

    # cur = label /2
    cur = label // 2

    # initializing a list
    # with label already in it
    res = [label]

    # move back to 0th level by decrementing level by 1
    while level > -1:
        # start = 2^level
        # end = 2^(level+1) -1
        start, end = 2 ** level, (2 **(level+1)) - 1

        # updating current by
        # start + end - cur
        cur = start + end - cur

        # append the current value to result list
        res.append(cur)

        # decrement the level (going up)
        level -= 1

        # make cur = cur/2
        cur = cur // 2

    # when level == 0
    # return the reversed result list
    return res[::-1]