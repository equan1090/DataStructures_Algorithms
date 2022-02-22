'''
Write a function, tree_includes, that takes in the root of a binary tree and a target value.
The function should return a boolean indicating whether or not the value is contained in the tree.
'''


def tree_includes(root, target):
    if root is None:
        return False
    if root.val == target:
        return True

    return tree_includes(root.left, target) or tree_includes(root.right, target)
