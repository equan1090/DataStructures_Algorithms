"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        n_0, n_1 = root, root.left if root else None
        # n_0 is our pointer to the current layer
        # n_1 is our pointer to next layer
        # We use n_0 to connect all the nodes belonging to next layer, meaning the layer n_1 belongs to.
        
        while n_1: # while there is a next layer to connect, we continue
            
            n_0.left.next = n_0.right # 1st action we can always do if there is a next layer after n_0
            
            if n_0.next: # 2nd action we might be able to do if we are not all the way to the right
                
                n_0.right.next = n_0.next.left
                
                n_0 = n_0.next 
                
                continue # we keep going to the "right" until the layer is all connected
                
            n_0, n_1  = n_1, n_1.left # "Recursive call" to handle the next layer
        return root