class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.inspect(root.left, root.right)

    def inspect(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return self.inspect(left.left, right.right) and self.inspect(left.right, right.left)