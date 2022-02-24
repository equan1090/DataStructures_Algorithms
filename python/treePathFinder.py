'''
tree path finder
Write a function, path_finder, that takes in the root of a binary tree and a target value. The function should return an array representing a path to the target value. If the target value is not found in the tree, then return None.

You may assume that the tree contains unique values.
'''
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None


def path_finder(root, target):
    result = _path_finder(root, target)

    if result:
        return result[::-1]

    return None


def _path_finder(root, target):

    if root is None:
        return None

    if root.val == target:
        return [root.val]

    leftPath = _path_finder(root.left, target)
    if leftPath:
        leftPath.append(root.val)
        return leftPath

    rightPath = _path_finder(root.right, target)
    if rightPath:
        rightPath.append(root.val)
        return rightPath

    return None
