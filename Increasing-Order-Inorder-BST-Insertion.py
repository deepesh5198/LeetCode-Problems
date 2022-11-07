# Problem Description:
# Input: root = [5,1,7]
# Output: [1,null,5,null,7]
 
#       5               1
#     /   \     ->       \
#    1     7              5
#                          \
#                           7

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def __init__(self):
        self.node = TreeNode()
        self.result = []
        
    def insert(self, node, data):
        if node.val == None:
            node.val = data
            
        elif not node.right:
            node.right = TreeNode(val = data)
            
        else:
            self.insert(node.right, data)
    
            
    def rec_inorder_traversal(self, root):
        if not root:
            return
        else:
            self.rec_inorder_traversal(root.left)
            self.insert(self.node, root.val)
            self.rec_inorder_traversal(root.right)
        
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.node.val = None
        self.rec_inorder_traversal(root)
        return self.node