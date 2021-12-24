from collections import deque
import heapq

def dijkstras(matrix, start, end):
  queue = []
  visited = set()
  distances = [None for _ in range(len(matrix))]
  distances[start] = 0
  heapq.heappush(queue, (0, start))
  while queue:
    distance, i = heapq.heappop(queue)
    if i in visited:
      continue
    visited.add(i)
    if distances[i] == None or distance < distances[i]:
      distances[i] = distance
    if len(visited) == len(matrix) - 1:
      return distances
    for neighbor_i in range(len(matrix[i])):
      if i != neighbor_i and matrix[i][neighbor_i] != None and neighbor_i not in visited:
        heapq.heappush(queue, (distances[i] + matrix[i][neighbor_i], neighbor_i))
  return distances


        
def hrank_problem(n, edges, start):
  matrix = [[None for _ in range(n + 1)] for _ in range(n + 1)]
  for edgeStart, edgeEnd, dist in edges:
    if matrix[edgeStart][edgeEnd] is None or dist < matrix[edgeStart][edgeEnd]:
      matrix[edgeStart][edgeEnd] = dist
      matrix[edgeEnd][edgeStart] = dist
  distances = dijkstras(matrix, start, -1)
  ret = []
  for i in range(1, len(distances)):
    if i != start:
      if distances[i] is None:
        ret.append(-1)
      else:
        ret.append(distances[i])
  return ret 

def trace_path(start, end, distances, best_parents):
  total_distance = distances[end]
  path = [end]
  rover = end
  while rover != start:
    rover_parent = best_parents[rover]
    path.append(rover_parent)
    rover = rover_parent
  path.append(start)
  return path[::-1]

def test_dijkstra():
  ret = hrank_problem(4, [
    (1, 2, 24),
    (1, 4, 20),
    (3, 1, 3),
    (4, 3, 12)
  ], 1)
  print(ret)

test_dijkstra()