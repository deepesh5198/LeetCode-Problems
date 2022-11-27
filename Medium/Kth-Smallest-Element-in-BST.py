# Problem Description:
# Find the kth Smallest element in the Binary Search Tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(3)
root.left = TreeNode(1)
root.left.right = TreeNode(2)
root.right = TreeNode(4)

def kthSmallest(root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    # empty list
    result = []

    # fill the result list
    # with nodes in the BST
    # by level order traversal
    if not root:
        return

    else:
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            result.append(node.val)
            
            if node.left:
                queue.append(node.left)
                
            if node.right:
                queue.append(node.right)
                
    # sort the result list in ascending order
    result.sort()

    # return the k-1th element
    return result[k-1]

print(kthSmallest(root=root, k=1))