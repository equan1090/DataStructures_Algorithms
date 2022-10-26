# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        
        return abs(l - r) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
        
    def dfs(self, root):
        if not root:
            return 0
        
        return 1 + max(self.dfs(root.left), self.dfs(root.right))