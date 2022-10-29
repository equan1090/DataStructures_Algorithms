# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        order = self.inorder(root, [])
        for i in range(1, len(order)):
            if order[i] <= order[i-1]:
                return False
        return True
        
    def inorder(self, root, order):
        if not root:
            return order
        
        self.inorder(root.left, order)
        order.append(root.val)
        self.inorder(root.right, order)
        return order