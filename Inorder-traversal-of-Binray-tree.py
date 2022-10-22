# Problem Description: Given the root of a binary tree, return the 
# inorder traversal of its nodes' values.

#EXAMPLE
#       1
#        \
#         2
#        /
#       3

# Input: root = [1,null,2,3]
# Output: [1,3,2]


def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        else:
            stack = []
            result = []
            while stack or root:
                if root:
                    stack.append(root)
                    root = root.left
                    
                else:
                    root = stack.pop()
                    result.append(root.val)
                    root = root.right
            return result