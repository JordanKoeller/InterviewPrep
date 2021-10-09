import math
import heapq

class Node:
  def __init__(self, index):
    self.index = index
    self.edges = {}
    self.hopsFromS = math.inf
  
  def addEdge(self, destinationNode):
    self.edges[destinationNode.index] = destinationNode
    destinationNode.edges[self.index] = self

class Graph:

  def __init__(self, numNodes):
    self.nodes = [Node(i) for i in range(0, numNodes)]
    self.edges = []

  def connect(self, i, j):
    self.nodes[i].addEdge(self.nodes[j])
  
  # I use a Breadth-first-search
  def find_all_distances(self, s):
    start = self.nodes[s]
    start.hopsFromS = 0
    pq = [start]
    while pq:
      top = pq.pop(0)
      for edgeK in top.edges:
        if top.edges[edgeK].hopsFromS > top.hopsFromS + 6:
          top.edges[edgeK].hopsFromS = top.hopsFromS + 6
          pq.append(top.edges[edgeK])
    print(" ".join([str(n.hopsFromS) if math.isfinite(n.hopsFromS) else '-1' for n in self.nodes if n.index != s]))
      
      
        



t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1) 
    s = int(input())
    graph.find_all_distances(s-1)