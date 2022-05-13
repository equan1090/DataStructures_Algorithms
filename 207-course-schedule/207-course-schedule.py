class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            graph[crs].append(pre)
        
        visited = set()
        visiting = set()
        for node in graph:
            if self.hasCycle(graph, node, visited, visiting):
                return False
        return True
        
    def hasCycle(self, graph, node, visited, visiting):
        if node in visiting:
            return True
        if node in visited:
            return False
        
        visiting.add(node)
        for neighbor in graph[node]:
            if self.hasCycle(graph, neighbor, visited, visiting):
                return True
        
        visiting.remove(node)
        visited.add(node)
        return False
        