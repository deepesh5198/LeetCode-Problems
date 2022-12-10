class FindElements:
    def __init__(self, root):
        self.nodes = set()
        if not root:
            return

        root.val = 0
        self.nodes.add(0)
        
        def uncontaminate(root):
            if not root:
                return

            if root.left:
                root.left.val = 2*root.val + 1
                self.nodes.add(root.left.val)
                uncontaminate(root.left)
            
            if root.right:
                root.right.val = 2*root.val + 2
                self.nodes.add(root.right.val)
                uncontaminate(root.right)

        uncontaminate(root)

    def find(self, target: int) -> bool:
        if target in self.nodes:
            return True

        else:
            return False