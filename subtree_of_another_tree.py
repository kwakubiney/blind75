class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        isSameTreeForRoot = self.isSameTree(root, subRoot)
        if isSameTreeForRoot:
            return True
        isSameTreeForRootLeft = self.isSameTree(root.left, subRoot)
        isSameTreeForRootRight = self.isSameTree(root.right, subRoot)
        return isSameTreeForRootLeft or isSameTreeForRootRight

    def isSameTree(self, root, subroot):
        if not root and not subroot:
            return True
        if not root or not subroot:
            return False
        if root.val != subroot.val:
            return False
        return self.isSameTree(root.left, subroot.left) and self.isSameTree(root.right, subroot.right)