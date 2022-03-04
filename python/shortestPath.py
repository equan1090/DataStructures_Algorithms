from collections import deque
def shortest_path(edges, node_a, node_b):
    graph = create_graph(edges)
    visited = set([node_a])
    queue = deque([(node_a, 0)])

    while queue:
        current, distance = queue.popleft()
        if current == node_b:
            return distance
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, distance  + 1))
    return -1

def create_graph(edges):
    graph = {}
    for edge in edges:
        a, b = edge

        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph
