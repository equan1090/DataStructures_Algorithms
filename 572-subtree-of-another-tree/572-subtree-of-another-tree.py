# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        
        if subRoot is None:
            return True
        if root is None:
            return False
        
        if self.sameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
        
    def sameTree(self, root, subroot):
        if not root and not subroot:
            return True
        
        if not root or not subroot:
            return False
        
        if root.val != subroot.val:
            return False
        
        return self.sameTree(root.left, subroot.left) and self.sameTree(root.right, subroot.right)