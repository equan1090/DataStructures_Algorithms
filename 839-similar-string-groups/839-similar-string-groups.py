class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        graph = {}
        for s in strs:
            graph[s] = []
        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                differences = 0
                for k in range(len(strs[0])):
                    if strs[i][k] != strs[j][k]:
                        differences += 1
                        
                        if differences > 2:
                            break
                    
                if differences == 2:
                    graph[strs[i]].append(strs[j])
                    graph[strs[j]].append(strs[i])
        
        
        visited = set()
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