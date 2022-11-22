# Problem Description
# You are given the root node of a binary search tree (BST) and a 
# value to insert into the tree. Return the root node of the BST 
# after the insertion. It is guaranteed that the new value does not 
# exist in the original BST.

# Notice that there may exist multiple valid ways for the insertion, 
# as long as the tree remains a BST after insertion. You can return 
# any of them.

# EXAMPLE:
# Input: root = [4,2,7,1,3], val = 5
# Output: [4,2,7,1,3,5]
# Explanation: Another accepted tree is:

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

def insertIntoBST(root, val):
    """
    :type root: TreeNode
    :type val: int
    :rtype: TreeNode
    """
    if not root:
        root = TreeNode(val)
        return root
    
    else:
        if val < root.val:
            if not root.left:
                node = TreeNode(val)
                root.left = node
                
            else:
                insertIntoBST(root.left, val)
                
        else:
            if not root.right:
                node = TreeNode(val)
                root.right = node
                
            else:
                insertIntoBST(root.right, val)
                
    return root

root1 = insertIntoBST(root, 5)

print(root1.right.left.val)