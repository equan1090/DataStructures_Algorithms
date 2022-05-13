class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return True
        
        graph = {i:[] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        visited = set()
        return self.dfs(graph, 0, -1, visited) and len(visited) == n
    
        
    def dfs(self, graph, i, prev, visited):
        if i in visited:
            return False
        visited.add(i)
        
        for neighbor in graph[i]:
            if neighbor == prev:
                continue
            
            if not self.dfs(graph, neighbor, i, visited):
                return False
        return True
    
    
        