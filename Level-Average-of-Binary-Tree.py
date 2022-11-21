# Problem Description:
# Given the root of a binary tree, return the average value 
# of the nodes on each level in the form of an array. Answers
# within 10-5 of the actual answer will be accepted.

class TreeNode:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = TreeNode(15)
root.left.right = TreeNode(7)

def levelOrder(root):
    if not root:
        return

    else:
        currentlevel = []
        result = []
        currentlevel.append(root)
        lefttoright = True
        while len(currentlevel) != 0:
            levelresult = []
            nextlevel = []

            while len(currentlevel) != 0:
                node = currentlevel.pop()
                levelresult.append(node.val)
            
                if lefttoright:
                    if node.left:
                        nextlevel.append(node.left)

                    if node.right:
                        nextlevel.append(node.right)

                else:
                    if node.right:
                        nextlevel.append(node.right)

                    if node.left:
                        nextlevel.append(node.left)

            currentlevel = nextlevel
            lefttoright = not(lefttoright)
            result.append(levelresult)

    return result
    
def averageOfLevels(root):
    """
    :type root: TreeNode
    :rtype: List[float]
    """
    level_list = levelOrder(root)
    print(level_list)
    output = []
    
    for level in level_list:
        output.append(float(sum(level)) / float(len(level)))
        
    return output

print(averageOfLevels(root))

