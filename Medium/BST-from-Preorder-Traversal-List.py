# Problem Description:
# Given an array of integers preorder, which represents 
# the preorder traversal of a BST (i.e., binary search tree), 
# construct the tree and return its root.

# EXAMPLE:
# Input: preorder = [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bstFromPreorder(preorder):
    """
    :type preorder: List[int]
    :rtype: TreeNode
    """
    root = TreeNode(preorder[0])

    def insert(root, node):
        if node.val < root.val:
            if not root.left:
                root.left = node

            else:
                insert(root.left, node)

        else:
            if not root.right:
                root.right = node
            
            else:
                insert(root.right, node)

    for val in preorder[1:]:
        node = TreeNode(val)
        insert(root, node)

    return root

root = bstFromPreorder([8,5,1,7,10,12])

def preoder(root):
    if not root:
        return

    else:
        print(root.val)
        preoder(root.left)
        preoder(root.right)
preoder(root)