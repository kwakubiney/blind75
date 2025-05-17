class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #for every node, we care about it's left max depth and it's right max depth,
        #for that node, the max depth of it's left and right differnece will determine if it is balanced or not.
        #then from there we can do same for its left and it's right and bubble up booleans
        if not root:
            return True

        left_height = self.calculate_max_depth(root.left)
        right_height = self.calculate_max_depth(root.right)

        if abs(left_height - right_height) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def calculate_max_depth(self, root):
        if not root:
            return 0
        return 1 + max(self.calculate_max_depth(root.left), self.calculate_max_depth(root.right))