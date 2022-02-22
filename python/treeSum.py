'''
Write a function, tree_sum, that takes in the root of a binary tree that contains number values.
The function should return the total sum of all values in the tree.
'''


'''Depth First Recursive'''


def tree_sum(root):
    if root is None:
        return 0

    return root.val + tree_sum(root.left) + tree_sum(root.right)


'''Depth First Iterative'''
# def tree_sum(root):
#   if root is None:
#     return 0

#   sum = 0
#   stack = [root]
#   while stack:
#     current = stack.pop()
#     sum += current.val
#     if current.left:
#       stack.append(current.left)
#     if current.right:
#       stack.append(current.right)
#   return sum


'''Breadth First Approach'''
# from collections import deque
# def tree_sum(root):
#   if root is None:
#     return 0
#   sum = 0
#   queue = deque([root])
#   while queue:
#     current = queue.popleft()
#     sum += current.val
#     if current.left:
#       queue.append(current.left)
#     if current.right:
#       queue.append(current.right)
#   return sum
