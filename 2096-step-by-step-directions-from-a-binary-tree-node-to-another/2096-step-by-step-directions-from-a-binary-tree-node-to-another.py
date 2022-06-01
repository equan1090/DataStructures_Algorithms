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
                graph[node.left.val].append((node.val, 'U')) 
                graph[node.val].append((node.left.val, 'L'))
                
                q.append(node.left)
            if node.right:
                graph[node.right.val].append((node.val, 'U'))
                graph[node.val].append((node.right.val, 'R'))
                q.append(node.right)
        
        q = deque([(startValue, '')])
        visited = set()
        
        while q:
            curVal, curPath = q.popleft()
            
            if curVal in visited:
                continue
            visited.add(curVal)
            if curVal == destValue:
                return curPath
            
            for child, direction in graph[curVal]:
                if child not in visited:
                    
                    q.append((child, curPath + direction))
                