# Problem Description:
# Given the root node of a binary search tree and two integers "low" and "high",
# return the sum of values of all nodes with a value in the inclusive range [low, high].


#EXAMPLE:
# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
root = TreeNode(val=10)
root.left = TreeNode(val=5)
root.right = TreeNode(val=15)
root.left.left = TreeNode(val=3)
root.left.right = TreeNode(val=7)
root.right.right = TreeNode(val=18)

def rangeRoot(root, low, high):
    """
    a utility recursive function to give a BST with 
    only nodes in given range "low" and "high"
    
    """
    if not root:
        return
    else:
        root.left = rangeRoot(root.left, low, high)
        root.right = rangeRoot(root.right, low, high)
        
        if low <= root.val <= high:
            return root
        
        elif root.val < low:
            return root.right
        
        elif root.val > high:
            return root.left
        
        
def rangeSum(root):
    """
    Main function to calculate sum of 
    nodes in range
    
    """
    if not root:
        return 0 
    else:
        return root.val + rangeSum(root.left) + rangeSum(root.right)
    
root = rangeRoot(root, 7, 15)   
print(rangeSum(root))


