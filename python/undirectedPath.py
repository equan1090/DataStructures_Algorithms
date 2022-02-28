'''
Write a function, undirected_path, that takes in a list of edges for an undirected graph
and two nodes (node_A, node_B). The function should return a boolean indicating whether or not
there exists a path between node_A and node_B.
'''


def undirected_path(edges, node_a, node_b):
    graph = create_graph(edges)
    return has_path(graph, node_a, node_b, set())


def has_path(graph, node_a, node_b, visited):
    if node_a == node_b:
        return True

    if node_a in visited:
        return False

    visited.add(node_a)

    for neighbor in graph[node_a]:
        if has_path(graph, neighbor, node_b, visited):
            return True
    return False


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
