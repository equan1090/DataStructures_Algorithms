# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        self.traverse(root, 0, values)
        return values
        
    def traverse(self, root, level, values):
        if root is None:
            return
        
        if len(values) == level:
            values.append(root.val)
        
        self.traverse(root.right, level + 1, values)
        self.traverse(root.left, level + 1, values)