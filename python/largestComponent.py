'''
Write a function, largest_component, that takes in the adjacency list of an undirected graph.
The function should return the size of the largest connected component in the graph.
'''


def largest_component(graph):
    visited = set()
    largest = 0

    for node in graph:
        size = explore(graph, node, visited)
        if size > largest:
            largest = size
    return largest


def explore(graph, current, visited):
    if current in visited:
        return 0

    visited.add(current)
    size = 1
    for neighbor in graph[current]:
        size += explore(graph, neighbor, visited)
    return size
