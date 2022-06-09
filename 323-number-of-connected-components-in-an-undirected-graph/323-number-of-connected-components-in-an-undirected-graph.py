class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        visited = set()
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        count = 0
        for node in graph:
            if self.traverse(graph, node, visited):
                count += 1
        return count
    
    def traverse(self, graph, node, visited):
        if node in visited:
            return False
        
        visited.add(node)
        
        for neighbor in graph[node]:
            self.traverse(graph, neighbor, visited)
        return True