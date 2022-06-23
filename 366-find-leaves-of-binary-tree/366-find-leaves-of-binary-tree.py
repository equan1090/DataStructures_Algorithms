# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        self.dfs(root, res)
        return res
        
    def dfs(self, root, res):
        if root is None:
            return 0
        
        level = max(self.dfs(root.left, res), self.dfs(root.right, res))
        
        if len(res) == level:
            res.append([])
        res[level].append(root.val)
        
        return 1 + level