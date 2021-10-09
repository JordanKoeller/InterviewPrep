 #!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

# Problem notes:
#  This definitely relates to spanning graphs and disjoint graphs.
# Based on the ratio of cost for a road to cost for a library,
#  This is going to decide our "budget" for road-building.
# If the cost of a road is cheaper than a library:
#  I want to have as few libraries as possible, which implies as many roads as possible that 
#  Does not have any redundant connections between nodes that are already connected.

# Algorithm:
#  1. "Pave" all the roads.
#  2. Identify the redundant roads, and remove them.
#         this is done by finding and breaking cycles in a way that does not produce any more disjoint graphs.

ROAD_POTENTIAL = 0
ROAD_PAVED = 1


class Node:
  def __init__(self, index):
    self.index = index
    self.visitIndex = None
    self.edges = {}

  def addPotentialRoad(self, destination):
    self.edges[destination.index] = destination
    destination.edges[self.index] = self
  def paveRoad(self, destination):
    self.edges[destination.index] = destination
    destination.edges[self.index] = self

class Graph:
  def __init__(self, numCities, roadCandidates):
    self.nodes = [Node(index) for index in range(numCities)]
    for start, end in roadCandidates:
      self.nodes[start-1].addPotentialRoad(self.nodes[end-1])

  def computeLibrariesAndRoads(self):
    # 1. Identify disjoint sets of nodes
    # 2. Remove roads to break cycles.
    # For this algorithm I will do a depth-first search
    disjointSets = {n.index for n in self.nodes}
    numTraversedEdges = 0
    for node in self.nodes:
      bfsIndex = node.index
      stack = deque()
      if node.visitIndex != None:
        disjointSets.remove(node.index)
        continue
      node.visitIndex = node.index
      stack.append(node)
      while len(stack) > 0:
        currNode = stack.pop()
        if currNode.visitIndex == bfsIndex:
          for adjId in currNode.edges:
            if currNode.edges[adjId].visitIndex == None:
              numTraversedEdges += 1
              currNode.edges[adjId].visitIndex = currNode.visitIndex
              stack.append(currNode.edges[adjId])
            elif currNode.edges[adjId].visitIndex != currNode.visitIndex and currNode.visitIndex in disjointSets:
              # We have found a bridge to what was assumed disjoint
              disjointSets.remove(currNode.visitIndex)
              numTraversedEdges += 1
            # The else statement represents backtracking back up the DFS search I am currently doing
    return (len(disjointSets), numTraversedEdges)



def roadsAndLibraries(n, c_lib, c_road, cities):
  if c_lib <= c_road:
    # It is cheaper to build a library than a road, so libraries for everyone!
    # print("All libraries")
    return n * c_lib
  graph = Graph(n, cities)
  n_lib, n_road = graph.computeLibrariesAndRoads()
  # print(f"Found Libs = {n_lib} roads = {n_road}")
  return n_lib * c_lib + n_road * c_road
  
  

if __name__ == '__main__':
    fptr = open(os.environ.get('OUTPUT_PATH', '/dev/stdout'), 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
