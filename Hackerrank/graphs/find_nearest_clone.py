#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque
# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
# Breadth-first search algorithm
#
class BFSState:
  def __init__(self, startPoint, graph, searchingFor):
    # self.startPoint = startPoint
    self.graph = graph
    self.searchingFor = searchingFor
    self.crumbs = set()
    self.queue = deque()
    self.queue.append((startPoint, 0))


  @property
  def stillGoing(self):
    return len(self.queue)> 0

  def iterate(self):
    # Run one cycle of the BFS.
    # Returns the path length if the destination was found.
    # Otherwise, returns None
    top, numSteps = self.queue.popleft()
    self.crumbs.add(top.index)
    for edgeIndex in top.edges:
      if edgeIndex not in self.crumbs:
        if top.edges[edgeIndex].color == self.searchingFor:
          return numSteps + 1
        else:
          self.queue.append((top.edges[edgeIndex], numSteps + 1))
    return None



class Node:
  def __init__(self, index, color):
    self.index = index
    self.color = color
    self.edges = {}

  def addEdge(self, destination):
    self.edges[destination.index] = destination
    destination.edges[self.index] = self

class Graph:
  def __init__(self, nodeColors, edges):
    self.nodes = [Node(index, color) for index, color in enumerate(nodeColors)]
    for s, e in edges:
      self.nodes[s-1].addEdge(self.nodes[e-1])

  def findShortest(self, color):
    nodesWithColor = [node for node in self.nodes if node.color == color]
    searches = [BFSState(node, self, color) for node in nodesWithColor]
    stillSearching = True
    while stillSearching:
      stillSearching = False
      for search in searches:
        if search.stillGoing:
          stillSearching = True
          searchResult = search.iterate()
          if searchResult is not None:
            return searchResult
    return -1



def findShortest(graph_nodes, graph_from, graph_to, ids, val):
  # solve here
  edges = zip(graph_from, graph_to)
  graph = Graph(ids, edges)
  return graph.findShortest(val)


if __name__ == '__main__':
    fptr = open(os.environ.get('OUTPUT_PATH', '/dev/stdout'), 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()
