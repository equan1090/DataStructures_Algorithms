class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findLeaves(root):
    res = []

    dfs(root, res)
    return res
def dfs(root, res):
    if not root:
        return -1
    height = max(dfs(root.left, res), dfs(root.right, res)) + 1
    if height >= len(res):
        res.append([])
    res[height].append(root.val)
    return height


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.left = b
b.left = d
b.right = e
a.right = c

print(findLeaves(a))
