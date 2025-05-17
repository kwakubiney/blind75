class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
            if root is None:
                return 0

            left_height = 1 + self.maxDepth(root.left)
            right_height = 1 + self.maxDepth(root.right)
            return max(left_height, right_height)