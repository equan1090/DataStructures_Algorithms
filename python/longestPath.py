def longest_path(graph):
  distance = {}
  for node in graph:
    if len(graph[node]) == 0:
      distance[node] = 0

  for node in graph:
    traverse_distance(graph, node, distance)

  return max(distance.values())

def traverse_distance(graph, node, distance):
  if node in distance:
    return distance[node]

  largest = 0
  for neighbor in graph[node]:
    attempt = traverse_distance(graph, neighbor, distance)
    if attempt > largest:
      largest = attempt

  distance[node] = 1 + largest
  return distance[node]

graph = {
  'a': ['c', 'b'],
  'b': ['c'],
  'c': [],
  'q': ['r'],
  'r': ['s', 'u', 't'],
  's': ['t'],
  't': ['u'],
  'u': []
}
print(longest_path(graph))
