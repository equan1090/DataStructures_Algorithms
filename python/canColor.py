'''
Write a function, can_color, that takes in a dictionary representing the adjacency list of an undirected graph.
The function should return a boolean indicating whether or not it is possible to color nodes of the graph using
two colors in such a way that adjacent nodes are always different colors.

For example, given this graph:

x-y-z

It is possible to color the nodes by using red for x and z,
then use blue for y. So the answer is True.

For example, given this graph:

    q
   / \
  s - r

It is not possible to color the nodes without making two
adjacent nodes the same color. So the answer is False.
'''


def can_color(graph):
    coloring = {}
    for node in graph:
        if node not in coloring and not _can_color(graph, node, coloring, False):
            return False
    return True


def _can_color(graph, node, coloring, color):
    if node in coloring:
        return coloring[node] == color

    coloring[node] = color

    for neighbor in graph[node]:
        if not _can_color(graph, neighbor, coloring, not color):
            return False
    return True
