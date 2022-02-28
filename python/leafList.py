'''
Write a function, leaf_list, that takes in the root of a binary tree and returns a list containing the values
of all leaf nodes in left-to-right order.
'''
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None


def leaf_list(root):
    result = []
    _leaf_list(root, result)
    return result


def _leaf_list(root, result):
    if root is None:
        return

    if not root.left and not root.right:
        result.append(root.val)

    _leaf_list(root.left, result)
    _leaf_list(root.right, result)
