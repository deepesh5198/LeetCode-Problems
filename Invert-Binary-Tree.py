#Problem Description:
# Given the root of a binary tree, invert the tree, and return its root.

# Example:
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if not root:
            return 
        
    else:
        queue = []
        queue.append(root)
        
        while queue:
            node = queue.pop(0)
            
            temp = node.left
            node.left = node.right
            node.right = temp
            
            if node.left:
                queue.append(node.left)
                
            if node.right:
                queue.append(node.right)
                
    return root
    
    
    