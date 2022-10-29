class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        
        for a, b in prerequisites:
            graph[a].append(b)
            
        visited = set()
        visiting = set()
        
        for node in graph:
            if self.dfs(graph, node, visited, visiting):
                return False
        return True
    
    def dfs(self, graph, node, visited, visiting):
        if node in visiting:
            return True
        if node in visited:
            return False
        
        visiting.add(node)
        
        for nei in graph[node]:
            if self.dfs(graph, nei, visited, visiting):
                return True
        
        visiting.remove(node)
        visited.add(node)
        return False