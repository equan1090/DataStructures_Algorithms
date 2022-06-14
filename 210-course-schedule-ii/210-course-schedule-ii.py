class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}
        
        for a, b in prerequisites:
            graph[a].append(b)
        
        visited = set()
        visiting = set()
        res = []
        for node in graph:
            if self.hasCycle(graph, node, visited, visiting, res):
                return []
        return res
    
    def hasCycle(self, graph, node, visited, visiting, res):
        if node in visited:
            return False
        
        if node in visiting:
            return True
        
        visiting.add(node)
        
        for neighbor in graph[node]:
            if self.hasCycle(graph, neighbor, visited, visiting, res):
                return True
        
        visiting.remove(node)
        
        visited.add(node)
        res.append(node)
        return False