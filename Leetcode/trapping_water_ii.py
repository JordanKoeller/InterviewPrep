""" orig
4 4 4 4
3 1 1 4
4 1 1 4
4 4 4 4

Board: 200 x 200
40,000 cells (max) O(n^2) is too slow

This is a graph-based solution.

Observations:

  1. Any block on the exterior must be a drain
  2. Any block that can be connected to a drain by blocks of equal or lower height must also drain.
  3. Any blocks that do not drain are a lake.
  4. The water level is the minimum height of blocks that border a lake

Algorithm:
  1. Perform a BFS starting at the edges of the map and label all blocks that drain.
  2. Any blocks that do not drain are a lake.
  3. For each lake block, find all other lake blocks as well as its border blocks (bfs).
      The water level of all found lake blocks is equal to the min height of a bordering drain block

"""
import copy
from collections import deque
import heapq
class Solution:
  def trapRainWater(self, heights):
    drains, visited = self.getDrainingBlocks(heights)
    # for row in drains:
    #   print(row)
    totalVolume = self.getTotalVolume(heights, drains)
    return totalVolume

  def getDrainingBlocks(self, heights):
    drains = [[False for _ in range(len(heights[0]))] for _ in range(len(heights))]
    visited = [[False for _ in range(len(heights[0]))] for _ in range(len(heights))]
    maxI = len(heights) - 1
    maxJ = len(heights[0]) - 1
    queue =  deque()
    queue.append((0, 0))
    drains[0][0] = True
    while queue:
      i, j = queue.popleft()
      visited[i][j] = True
      neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
      if i == 0 or j == 0 or i == maxI or j == maxJ:
        drains[i][j] = True
      if drains[i][j]:
        for nI, nJ in neighbors:
          if nI >= 0 and nI <= maxI and nJ >= 0 and nJ <= maxJ and (nI == 0 or nJ == 0 or nI == maxI or nJ == maxJ):
            drains[nI][nJ] = True
            if not visited[nI][nJ]:
              queue.append((nI, nJ))
          elif nI > 0 and nJ > 0 and nI < maxI and nJ < maxJ:
            if heights[nI][nJ] >= heights[i][j]:
              drains[nI][nJ] = True
              if not visited[nI][nJ]:
                queue.append((nI, nJ))
    return drains, visited

  def inBounds(self, i, j, heights):
    return i >= 0 and j >= 0 and i < len(heights) and j < len(heights[0])

  def getInBoundsNeighbors(self, i, j, heights, extraConstraints=None):
    neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    ret = []
    for nI, nJ in neighbors:
      if nI >= 0 and nJ >= 0 and nI < len(heights) and nJ < len(heights[0]):
        if extraConstraints == None or (extraConstraints and extraConstraints(nI, nJ)):
          ret.append((nI, nJ))
    return ret

  def getVolumeOfLake(self, waterLevel, startPt, heights, drains, visitedWater, waterVolume):
    queue = deque()
    queue.append(startPt)
    volume = 0
    newShores = []
    while queue:
      i, j = queue.popleft()
      if (i, j) in visitedWater:
        continue
      if waterLevel > heights[i][j]:
        volume += waterLevel - heights[i][j]
        waterVolume[i][j] = waterLevel - heights[i][j]
      visitedWater.add((i, j))
      for nI, nJ in self.getInBoundsNeighbors(i, j, heights):
        if (nI, nJ) not in visitedWater and not drains[nI][nJ]:
          if heights[nI][nJ] < waterLevel:
            queue.append((nI, nJ))
          else:
            drains[nI][nJ] = True
            newShores.append((nI, nJ))
    return volume, newShores
      

  def getTotalVolume(self, heights, drains):
    waterVolume = [[0 for _ in range(len(heights[0]))] for _ in range(len(heights))]
    lakeShores = []
    for i in range(len(heights)):
      for j in range(len(heights[0])):
        if drains[i][j]:
          neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
          for nI, nJ in neighbors:
            if self.inBounds(nI, nJ, heights) and not drains[nI][nJ]:
              heapq.heappush(lakeShores, (heights[i][j], (i, j)))
    volume = 0
    visitedLake = set()
    while lakeShores:
      waterLevel, (i, j) = heapq.heappop(lakeShores)
      for waterBlock in self.getInBoundsNeighbors(i, j, heights):
        if waterBlock not in visitedLake \
          and not drains[waterBlock[0]][waterBlock[1]] \
          and heights[waterBlock[0]][waterBlock[1]] < waterLevel:
          lakeVolume, newShores =  self.getVolumeOfLake(waterLevel, waterBlock, heights, drains, visitedLake, waterVolume)
          volume += lakeVolume
          for sI, sJ in newShores:
            heapq.heappush(lakeShores, (heights[sI][sJ], (sI, sJ)))
          # print("Volumes")
          # for row in waterVolume:
          #   print(row)
    return volume





def test(heights):
  solver = Solution()
  ret = solver.trapRainWater(heights)
  print(ret)

test([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]])
test([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]])

test([[5,8,7,7],[5,2,1,5],[7,1,7,1],[8,9,6,9],[9,8,9,9]])
test([[14,17,18,16,14,16],[17,3,10,2,3,8],[11,10,4,7,1,7],[13,7,2,9,8,10],[13,1,3,4,8,6],[20,3,3,9,10,8]])

"""
14 17 18 16 14 16
17  3 10  2  3  8
11 10  4  7  1  7
13  7  2  9  8  10
13  1  3  4  8  6
20  3  3  9  10 8


3 + 4 + 4 + 1
"""