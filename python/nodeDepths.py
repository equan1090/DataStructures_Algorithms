'''
The distance between a node in a Binary Tree and the tree's root is called the node's depth.
Write a function that takes in a Binary tree and returns the sum of its nodes' depths
'''

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def nodeDepths(root, depth = 0):
    if root is None:
        return 0
    return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)
    
# def nodeDepths(root):
#     sumDepths = 0
#     stack = [{'node': root, 'depth': 0}]
#     while len(stack) > 0:
#         nodeInfo = stack.pop()
#         node, depth = nodeInfo['node'], nodeInfo['depth']

#         if node is None:
#             continue
#         sumDepths += depth
#         stack.append({'node': node.left, 'depth': depth + 1})
#         stack.append({'node': node.right, 'depth': depth + 1})
#     return sumDepths
