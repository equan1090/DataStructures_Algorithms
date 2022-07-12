# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        
        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                graph[node.left].append(node)
                graph[node].append(node.left)
                q.append(node.left)
            
            if node.right:
                graph[node.right].append(node)
                graph[node].append(node.right)
                q.append(node.right)
        
        q = deque([(target, 0)])
        res = []
        visited = set([target])
        while q:
            node, distance = q.popleft()
            
            if distance == k:
                res.append(node.val)
            
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei, distance + 1))
        return res        
        