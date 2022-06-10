# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
		# In python, use a deque for a queue because of popping from the beginning of a deque is O(1) 
		# while popping from the beginning of a list/array is O(n)
		
		# We want to initialize our queue with a tuple containing the current root, as well as the level the node is in
        q = deque([(root, 0)])
        res = []
        
        while q:
			# destructure the first item in our queue into node and level
            node, level = q.popleft()
            
			# Here we add an empty array in case we do not have a corresponding level. (We cannot append to nothing)
            if len(res) == level:
                res.append([])
            
			# Append the node value to the approriate level
            res[level].append(node.val)
            
			# Checks if our current node has a left or right node. 
			# If it does, we add it to our queue while also incrementing our level by 1, indicating we are on a new level
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        
        return res[::-1]