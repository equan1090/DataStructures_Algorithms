# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        graph = defaultdict(list)
        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                graph[node.val].append((node.left.val, 'L'))
                graph[node.left.val].append((node.val, 'U'))
                q.append(node.left)
            
            if node.right:
                graph[node.val].append((node.right.val, 'R'))
                graph[node.right.val].append((node.val, 'U'))
                q.append(node.right)
        
        q = deque([(startValue, '')])
        visited = set()
        visited.add(startValue)
        while q:
            node, path = q.popleft()
            
            if node == destValue:
                return path
            
            for child, direction in graph[node]:
                if child not in visited:
                    visited.add(child)
                    q.append((child, path + direction))
        return 'NOT FOUND'
            
                
        