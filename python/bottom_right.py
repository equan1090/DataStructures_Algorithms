# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
'''
Write a function, bottom_right_value, that takes in the root of a binary tree.
The function should return the right-most value in the bottom-most level of the tree.

You may assume that the input tree is non-empty.
'''
from collections import deque
def bottom_right_value(root):
  queue = deque([root])
  current = None
  while queue:
    current = queue.popleft()
    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)

  return current.val
