# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):

       
        def recurse(node):
            if not node: return 0
            left, right = recurse(node.left), recurse(node.right)
            self.result = max(self.result, left+right)
            return 1 + max(left, right)

        self.result = 0
        recurse(root)
        return self.result