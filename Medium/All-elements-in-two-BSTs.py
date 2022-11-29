# Problem Descripiton
# Given two binary search trees root1 and root2, return a list containing all the
# integers from both trees sorted in ascending order.

# EXAMPLE:
# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getAllElements(root1, root2):
    # empty list to store node values
    list_of_nodes = []
    
    def inorderTraverse(root):
        if not root:
            return list_of_nodes
        else:
            inorderTraverse(root.left)
            list_of_nodes.append(root.val)
            inorderTraverse(root.right)
            
    inorderTraverse(root1)
    inorderTraverse(root2)
    
    list_of_nodes.sort()
    
    return list_of_nodes