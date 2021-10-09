
"""
1. Turn the matrix into some type of graph.
2. Sort the matrix to have min values first.
3. Perform a bfs algorithm.
"""

from collections import deque

class Solution:

  def longestPathLength(self, startTuple, matrix, visited):
    queue = deque()
    queue.append((*startTuple, 1))
    bestDist = 0
    while queue:
      tI, tJ, dist = queue.popleft()
      if dist > bestDist:
        bestDist = dist
      visited[tI][tJ] = dist
      neightbors = [(tI, tJ + 1), (tI, tJ - 1), (tI - 1, tJ), (tI + 1, tJ)]
      for i, j in neightbors:
        if i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0]) and matrix[i][j] > matrix[tI][tJ] and visited[i][j] < dist:
          queue.append((i, j, dist + 1))
    return bestDist

      

  def longestIncreasingPath(self, matrix):
    indices = []
    visited = []
    for i in range(len(matrix)):
      tmpArr = [0 for _ in range(len(matrix[0]))]
      for j in range(len(matrix[0])):
        indices.append((i, j))
      visited.append(tmpArr)
    indices.sort(key=lambda elem: matrix[elem[0]][elem[1]])
    best = 1
    for i, j in indices:
      if visited[i][j] == 0:
        pathLength = self.longestPathLength((i, j), matrix, visited)
        if pathLength > best:
          best = pathLength
    return best


def test():
  soln = Solution()
  print(soln.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))
  
test()