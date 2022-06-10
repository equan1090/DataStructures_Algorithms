# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not k:
            return [target.val]
        
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
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append((neighbor, distance + 1))
        return res
            
            
        '''
        graph = {
        0: []
        1: [0, 8],
        2: [7, 4]
        3: [5, 1]
        4: []
        6: []
        7: []
        8: []
        }
        '''
            