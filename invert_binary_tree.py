class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:     
        if root is None:
            return
        a = root.left
        root.left = root.right
        root.right = a
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root