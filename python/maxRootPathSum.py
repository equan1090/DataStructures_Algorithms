# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def max_path_sum(root):
    if root is None:
        return float('-inf')

    if root.left is None and root.right is None:
        return root.val

    leftPath = max_path_sum(root.left)
    rightPath = max_path_sum(root.right)

    return root.val + max(leftPath, rightPath)
