# Problem Statement:
# A binary tree's maximum depth is the number of nodes along the
# longest path from the root node down to the farthest leaf node.

def maxDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0 
    
    else:
        return max(self.maxDepth(root.left),\
                self.maxDepth(root.right)) + 1