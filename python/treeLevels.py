'''
Write a function, tree_levels, that takes in the root of a binary tree.
The function should return a 2-Dimensional list where each sublist represents a level of the tree.
'''


# from collections import deque

# def tree_levels(root):
#   if root is None:
#     return []

#   result = []
#   queue = deque([(root, 0)])

#   while queue:
#     current, level = queue.popleft()

#     if len(result) == level:
#       result.append([current.val])
#     else:
#       result[level].append(current.val)

#     if current.left:
#       queue.append((current.left, level + 1))

#     if current.right:
#       queue.append((current.right, level + 1))

#   return result


def tree_levels(root):
    levels = []
    _tree_levels(root, levels, 0)
    return levels


def _tree_levels(root, levels, level_num):
    if root is None:
        return

    if level_num == len(levels):
        levels.append([root.val])
    else:
        levels[level_num].append(root.val)

    _tree_levels(root.left, levels, level_num + 1)
    _tree_levels(root.right, levels, level_num + 1)
