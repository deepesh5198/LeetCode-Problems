# Problem Description:
# Given the root of a binary tree, return the same tree where every subtree 
# (of the given tree) not containing a 1 has been removed.

# A subtree of a node node is node plus every node that is a descendant of node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(0)
root.right = TreeNode(0)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)

def pruneTree(root):
    if not root:
        return

    else:
        root.left = pruneTree(root.left)
        root.right = pruneTree(root.right)

        if root.val == 1:
            return root

        elif root.val == 0:
            if root.left or root.right:
                return root

            else:
                return None

pruneTree(root)