# Problem Description:
# Given an n-ary tree, return the level order traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order traversal, 
# each group of children is separated by the null value (See examples).

# EXAMPLE:
# Input: root = [1,null,3,2,4,null,5,6]
# Output: [[1],[3,2,4],[5,6]]

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def levelOrder(root):
    """
    :type root: Node
    :rtype: List[List[int]]
    """
    # initialize an empty list
    res = []
    if not root:
        return
    
    else:
        # append the root value in the result list
        res.append([root.val])

        # initiate an empty queue
        queue = []

        # append the children list of root
        # into the queue
        queue.append(root.children)
        
        # run the while loop till the queue gets empty
        while queue:
            # level result
            level_res = []

            # next level
            next_level = []
            
            # pop children list from queue
            children = queue.pop(0)
            
            # go through each node in chilren list
            for n in children:

                # append node value to level result list
                level_res.append(n.val)

                # if node has children
                if n.children:
                    # if next_level list is empty then
                    # assign node's children list as next_level 
                    if not next_level:
                        next_level = n.children

                    # if next_level list is not empty then
                    # extend next_level
                    else:
                        next_level.extend(n.children)
                
            # extend the queue with next_level list        
            queue.append(next_level)
            if level_res:
                res.append(level_res)
            else:
                return res
    return res