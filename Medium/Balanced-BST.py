# Problem Description:
# given a root of BST convert it into a Balanced Binary Search Tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def balanceBST(root):

    # initialize an empty list to strore
    # node values in Inorder pattern
    arr = []
    def inorderTraversal(root):
        if not root:
            return []
        
        else:
            inorderTraversal(root.left)
            arr.append(root.val)
            inorderTraversal(root.right)
        
        return arr
            
    # this function takes each element in Inorder
    # travesed list, and reconstructs a binary tree
    def balanced(left, right, items_list):
        """
        :param left: low index in items_list
        :param right: high index in items_list
        """
        # if low index is greater than
        # high index return None
        if left > right:
            return None
        
        # else
        else:
            # create a new root node
            root = TreeNode()

            # calculate the mid element of
            # the items list
            mid = (left+right)//2

            # set root node value as items list mid element
            root.val = items_list[mid]

            # set root's left node from the left half of items list
            root.left = balanced(left, mid-1, items_list)
            # set root's right node from the right half of items list
            root.right = balanced(mid+1, right, items_list)
            
        # return root
        return root
    
    # create items list
    # its the list of items in inorder traversal pattern
    items_list = inorderTraversal(root)

    # return the balanced binary search tree
    return balanced(0, len(items_list) -1, items_list)
        