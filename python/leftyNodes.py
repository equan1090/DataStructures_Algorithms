'''
Write a function, lefty_nodes, that takes in the root of a binary tree.
The function should return a list containing the left-most value on every level of the tree.
The list must be ordered in a top-down fashion where the root is the first item.
'''


def lefty_nodes(root):
    return _lefty_nodes(root, 0, [])


def _lefty_nodes(root, level, res):
    if root is None:
        return []

    if len(res) == level:
        res.append(root.val)

    _lefty_nodes(root.left, level + 1, res)
    _lefty_nodes(root.right, level + 1, res)

    return res
