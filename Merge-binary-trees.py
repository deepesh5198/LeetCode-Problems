# You are given two binary trees root1 and root2.
# Imagine that when you put one of them to cover the other,
# some nodes of the two trees are overlapped while the others
# are not. You need to merge the two trees into a new binary tree.
# The merge rule is that if two nodes overlap, then sum node values
# up as the new value of the merged node. Otherwise, the NOT null
# node will be used as the node of the new tree.

# Return the merged tree.

# Note: The merging process must start from the root nodes of both trees.

# EXAMPLE
#       1               2                   3
#      /  \            /  \                /  \ 
#     3    2          1    3      ==>     4     5 
#    /                 \    \            /  \    \
#   5                   4    7          5    4    7
#
# Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
# Output: [3,4,5,5,4,null,7]

class TreeNode:
    def __init__(self, data = None) -> None:
        self.data = data
        self.left = None
        self.right = None
        
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)

def mergeTrees(root1, root2):
    if not root1 and not root2:
        return None

    elif not root1 and root2:
        return root2
    
    elif root1 and not root2:
        return root1
    
    else:
        root = TreeNode()
        root.data = root1.data + root2.data
        
        root.left = mergeTrees(root1.left, root2.left)
        root.right = mergeTrees(root1.right, root2.right)
        
    return root

newRoot = mergeTrees(root1, root2)

def inorder(root):
    if not root:
        return
    else:
        print(root.data)
        inorder(root.left)
        
        inorder(root.right)
        
inorder(newRoot)
    
    
    
    
