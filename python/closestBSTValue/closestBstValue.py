def findClosest(tree, target):

    return bstHelper(tree, target, tree.value)

def bstHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target > tree.value:
        return bstHelper(tree.right, target, closest)
    elif target < tree.value:
        return bstHelper(tree.left, target, closest)
    else:
        return closest


#Given Tree
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
