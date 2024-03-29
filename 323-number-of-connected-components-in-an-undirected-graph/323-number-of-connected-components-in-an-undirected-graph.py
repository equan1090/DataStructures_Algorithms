class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        count = 0
        visited = set()
        
        for node in graph:
            if self.dfs(graph, node, visited):
                count += 1
        return count
    
    def dfs(self, graph, node, visited):
        if node in visited:
            return False
        
        visited.add(node)
        
        for nei in graph[node]:
            self.dfs(graph, nei, visited)
        
        return True