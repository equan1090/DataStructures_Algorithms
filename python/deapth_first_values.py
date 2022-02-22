'''
Write a function, depth_first_values, that takes in the root of a binary tree.
The function should return a list containing all values of the tree in depth-first order.
'''


# Iterative approach
# def depth_first_values(root):
#     if not root:
#         return []

#     stack = [root]
#     values = []

#     while stack:
#         node = stack.pop()
#         values.append(node.val)
#         if node.right:
#             stack.append(node.right)
#         if node.left:
#             stack.append(node.left)
#     return values


# Recursive Approach


def depth_first_values(root):
    result = []
    helper(root, result)
    return result


def helper(node, result):
    if node is None:
        return result
    result.append(node.val)

    helper(node.left, result)
    helper(node.right, result)
    return result
