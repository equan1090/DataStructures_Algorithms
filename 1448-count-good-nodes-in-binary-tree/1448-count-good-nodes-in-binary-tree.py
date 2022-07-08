# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        return self.dfs(root, root.val)
        
        
    def dfs(self, node, x):
        if node is None:
            return 0
        
        res = 1 if node.val >= x else 0
        
        x = max(node.val, x)
        res += self.dfs(node.left, x)
        res += self.dfs(node.right, x)
        return res
        
        