'''
Write a function, has_path, that takes in a dictionary representing the adjacency list of a directed
acyclic graph and two nodes (src, dst). The function should return a boolean indicating whether or
not there exists a directed path between the source and destination nodes.
'''


from collections import deque


def has_path(graph, src, dst):
    if src == dst:
        return True

    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst):
            return True
    return False


# def has_path(graph, src, dst):
#     queue = deque([src])

#     while queue:
#         current = queue.popleft()

#         if current == dst:
#             return True

#         for neighbor in graph[current]:
#             queue.append(neighbor)

#     return False
