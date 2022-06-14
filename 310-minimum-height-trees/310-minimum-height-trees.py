class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1: return [0] 
        graph = {i:[] for i in range(n)}
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        leaves = [i for i in range(n) if len(graph[i]) == 1]

        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for i in leaves:
                j = graph[i].pop()
                graph[j].remove(i)
                if len(graph[j]) == 1: newLeaves.append(j)
            leaves = newLeaves
        return leaves