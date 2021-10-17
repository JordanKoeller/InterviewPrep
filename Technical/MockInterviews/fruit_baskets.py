"""
2 baskets - so two types of fruit to pick from
can't skip trees in the sequence.

I want to grab the maximum number of fruit.


Problem:
  Return the length of the longest subsequence of only 2 elements.


Brute Force: 
  Iterate through the array:
    bestFound = 0
    For each elem in the array:
      length = GetLongestSubstrOf2(pos)
      if length > bestFound:
        bestFound = length
    return bestFound

  O(n^2)

A B A A B B C C C C C C

6 chars -> first substr (A, B) -> backtrack to the start of the last contig B's
8 chars -> first substr (B, C)

GetLongestSubstr -> length, (lastChar, firstInd of lastChar's contig space)

GetLongestSubstr -> length, lastChar, firstInd of lastChar, lastInd

one-pass solution (constant space)
"""
def get_substr(fruits, startIdx, char1=None, seed_length=None):
  char2 = None
  char1 = char1 or fruits[0]
  length = seed_length or 0
  last_seen_char = char1
  last_contig_start = startIdx
  i = startIdx
  while i < len(fruits):
    if fruits[i] == char1 or char2 is None or fruits[i] == char2:
      pass
    else:
      return length, last_seen_char, last_contig_start, i
    if fruits[i] != char1 and char2 == None:
      char2 = fruits[i]
      last_seen_char = fruits[i]
      last_contig_start = i
    elif fruits[i] != last_seen_char:
      last_contig_start = i
      last_seen_char = fruits[i]
    length += 1
    i += 1
  return length, last_seen_char, last_contig_start, i


def fruit_baskets(fruits):
  best_found = 0
  i = 0
  last_seen_char = None
  last_contig_start = 0
  while i < len(fruits):
    sub_length, last_seen_char, last_contig_start, next_i = get_substr(fruits, i, last_seen_char, i - last_contig_start)
    if sub_length > best_found:
      best_found = sub_length
    i = next_i
    if i - last_contig_start + len(fruits) - i < best_found:
      return best_found
  return best_found

def test_fruit(fruits):
  ret = fruit_baskets(fruits)
  print(fruits, " =>", ret)
    
# test_fruit(['A', 'B', 'O', 'A', 'B', 'A'])
# test_fruit(['A', 'B', 'A', 'A', 'B', 'B', 'C', 'C', 'C', 'C', 'C'])
# test_fruit(['C', 'C', 'C', 'C', 'A', 'B', 'A', 'A' 'C', 'C'])
# test_fruit([])
# test_fruit(['A', 'A', 'A'])
# test_fruit(['A', 'B', 'A', 'C', 'A', 'A', 'A', 'A', 'A', 'A'])


"""
Given a matrix of 0s and 1s
0 => water
1 => land
An island -> 4 or more land blocks adjacent
Return largest island, if you are allowed to change 1 water to be land

Brute Force: O(n^2)
  bestFound = 0
  for each water block:
    convert it to land
    maxIsland = getMaxIsland(matrix) // BFS
    if maxIsland > bestFound:
      bestFound = maxIsland
  return bestFound


Question: How much can convering one block actually do?

  Case 1: I take a block on the shore and convert it to land -> +1 to island's area
          Would work for converting a block in an interior lake.
  Case 2: Converting a block connects two islands.

Cleaner approach:
  Compute all islands. Lookup from block on the island => size of island.
    Search for any water blocks that separate two disjoint islands => area_combined = area(island1) + area(island2) + 1

islands = [(area)] -> BFS
blocksToIslands [matrix of indices to islands that that block is a part of.]

for elem in matrix:
  neighborsIslands = [island(nieghor) for neight of elem]
  pull pairs out of neighors, calc combined height, update best found if necessary


"""
from collections import deque

def get_neighbors(matrix, i, j):
  seeds = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
  ret = []
  for nI, nJ in seeds:
    if nI >= 0 and nJ >= 0 and nI < len(matrix) and nJ < len(matrix[0]):
      ret.append((nI, nJ))
  return ret

def get_island(matrix, island_ownership, i, j, island_id):
  queue = deque()
  queue.append((i, j))
  area = 0
  while queue:
    c_i, c_j = queue.popleft()
    island_ownership[c_i][c_j] = island_id 
    area += 1
    for n_i, n_j in get_neighbors(matrix, c_i, c_j):
      if matrix[n_i][n_j] == 1 and island_ownership[n_i][n_j] == None:
        queue.append((n_i, n_j))
  return area

def make_islands(matrix):
  island_ownership = [[None for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
  islands = []
  all_water = True
  all_land = True
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if island_ownership[i][j] == None: # Has not been visited yet
        if matrix[i][j] == 0:
          island_ownership[i][j] = -1
          all_land = False
        else:
          all_water = False
          islands.append(get_island(matrix, island_ownership, i, j, len(islands)))
  if all_water:
    return 1
  if all_land:
    return len(matrix[0]) * len(matrix)
  return islands, island_ownership


def largest_island(matrix):
  ret = make_islands(matrix)
  if isinstance(ret, int):
    return ret
  islands, ownership = ret

  best_area = 0
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if matrix[i][j] == 0:
        neighbors = get_neighbors(matrix, i, j)
        unique_islands = [ownership[n_i][n_j] for n_i, n_j in neighbors if ownership[n_i][n_j] != -1]
        for island1 in unique_islands:
          for island2 in unique_islands:
            if island1 != island2:
              combined_area = islands[island1] + islands[island2] + 1
              if combined_area > best_area:
                best_area = combined_area
            else:
              sz = islands[island1] + 1
              if sz > best_area:
                best_area = sz
  return best_area

def test_make_islands(matrix):
  best = largest_island(matrix)
  print(best)

test_make_islands([[0]]) # 1
test_make_islands([[1]]) # 1
test_make_islands([[0, 1], [0, 0]]) # 2
test_make_islands([[0, 1, 0], [0, 1, 0], [0, 0, 1]]) # 4
test_make_islands([[0, 1, 0], [0, 1, 0], [0, 0, 0]]) # 3