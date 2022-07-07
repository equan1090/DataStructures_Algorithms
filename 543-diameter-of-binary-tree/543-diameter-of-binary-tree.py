# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def path_length(self, root: TreeNode):
        if root:
            left_path = self.path_length(root.left)
            right_path = self.path_length(root.right)
            path = left_path + right_path
            if path > self.diameter:
                self.diameter = path    
            return max(left_path, right_path)+1
        return 0
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        self.path_length(root)
        return self.diameter