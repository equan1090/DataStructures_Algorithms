class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        left = self._isBalanced(root.left)
        right = self._isBalanced(root.right)

        return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def _isBalanced(self, root):
        if root is None:
            return 0
        return 1 + max(self._isBalanced(root.left), self._isBalanced(root.right))
