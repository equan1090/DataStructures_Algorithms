'''
Write a function, has_cycle, that takes in an object representing the adjacency list of a directed graph.
 The function should return a boolean indicating whether or not the graph contains a cycle.
 
has_cycle({
  "a": ["b"],
  "b": ["c"],
  "c": ["a"],
}) # -> True
'''


def has_cycle(graph):
    visiting = set()
    visited = set()
    for node in graph:
        if _has_cycle(graph, node, visited, visiting):
            return True
    return False

def _has_cycle(graph, node, visited, visiting):
    if node in visiting:
        return True
    if node in visited:
        return False
    
    visiting.add(node)
    for neighbor in graph[node]:
        if _has_cycle(graph, neighbor, visited, visiting):
            return True
    
    visiting.remove(node)
    visited.add(node)
    return False


print(has_cycle({
    "a": ["b"],
    "b": ["c"],
    "c": ["a"],
}))  # -> True

print(has_cycle({
    "q": ["r", "s"],
    "r": ["t", "u"],
    "s": [],
    "t": [],
    "u": [],
    "v": ["w"],
    "w": [],
    "x": ["w"],
}))  # -> False)
