'''
Write a function, best_bridge, that takes in a grid as an argument. 
The grid contains water (W) and land (L). There are exactly two islands 
in the grid. An island is a vertically or horizontally connected region of land.
Return the minimum length bridge needed to connect the two islands. 
A bridge does not need to form a straight line.
'''

from collections import deque


def best_bridge(grid):
  island = None
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      potential = findIsland(grid, row, col, set())
      if len(potential) > 0:
        island = potential
        break

  visited = set(island)
  queue = deque([])
  for pos in island:
    row, col = pos
    queue.append((row, col, 0))

  while queue:
    row, col, distance = queue.popleft()
    if grid[row][col] == 'L' and (row, col) not in island:
      return distance - 1

    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for delta in deltas:
      delta_row, delta_col = delta
      neighborRow = delta_row + row
      neighborCol = delta_col + col
      neighborPos = (neighborRow, neighborCol)
      rowBounds = 0 <= neighborRow < len(grid)
      colBounds = 0 <= neighborCol < len(grid[0])
      if (colBounds and rowBounds) and neighborPos not in visited:
        visited.add(neighborPos)
        queue.append((neighborRow, neighborCol, distance + 1))


def inbounds(grid, row, col):
  row_inbounds = 0 <= row < len(grid)
  col_inbounds = 0 <= col < len(grid[0])
  return row_inbounds and col_inbounds


def findIsland(grid, row, col, visited):

  if not inbounds(grid, row, col):
    return visited
  if grid[row][col] == 'W':
    return visited

  pos = (row, col)
  if pos in visited:
    return visited
  visited.add(pos)
  deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]

  for delta in deltas:
    delta_row, delta_col = delta
    neighborRow = delta_row + row
    neighborCol = delta_col + col
    findIsland(grid, neighborRow, neighborCol, visited)
  return visited
