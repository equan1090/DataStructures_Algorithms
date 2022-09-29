class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        visited = set()
        visiting = set()
        for a, b in prerequisites:
            graph[a].append(b)

        for node in graph:
            if self.hasCycle(graph, node, visited, visiting):
                return False
        return True
        
        
    def hasCycle(self, graph, node, visited, visiting):
        if node in visited:
            return False
        
        if node in visiting:
            return True
        
        visiting.add(node)
        
        for nei in graph[node]:
            if self.hasCycle(graph, nei, visited, visiting):
                return True
        
        visited.add(node)
        visiting.remove(node)
        return False