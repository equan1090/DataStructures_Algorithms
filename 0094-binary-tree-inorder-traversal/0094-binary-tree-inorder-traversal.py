# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # L N R
        return self._inorder(root, [])
    def _inorder(self, node, res):
        if not node:
            return []
        
        self._inorder(node.left, res)
        res.append(node.val)
        self._inorder(node.right, res)
        return res