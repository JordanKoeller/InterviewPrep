#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedForest' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY c
#  2. 2D_INTEGER_ARRAY edges
#

# Brute force implenentation:
  # Pick two edges, and cut them!
  # Construct the three trees, and compute their total
  # If two trees have an equal sum, compute the value needed to add to the third.
  # Repeat for all pairs of edges, and return the lowest diference found.
# Runtimes:
  # Say have N many nodes
  # and E many edges
  
  # Initial tree construction time: N*E

  # Tree total runtime: O(N_tree), so computing all three trees is O(N)
  # E^2 Pairs of edges to try cutting
  # Total: E^2 * N

# Optimized solution:

class Node:
  def __init__(self, value, index):
    self.value = value
    self.index = index
    self.edges = {}
    self.treeTotal = 0
    self.height = None
    self.parent = None
    self.enqueued = False

  def addEdge(self, child):
    self.edges.update({child.index: child})
    child.edges.update({self.index: self})

  def rmEdge(self, to):
    self.edges.pop(to)

  def replaceEdge(self, to):
    self.edges.update({to.index: to})
    to.parent = self

  def exciseChild(self, childIndex):
    """
    Cut off a child and return the root of the resultant tree.
    """
    if childIndex in self.edges:
      ret = self.edges[childIndex]
      self.edges.pop(childIndex)
      ret.parent = None
      return ret

  def hasParent(self, parent):
    cnt = 0
    rover = self.parent
    while rover != None:
      cnt += 1
      if rover.index == parent.index:
        return True
      rover = rover.parent
    return False


  @property
  def totalsAndUid(self):
    crumbs = set()
    total = 0
    toCount = [self]
    while toCount:
      top = toCount.pop(0)
      crumbs.add(top.index)
      total += top.value
      for index in top.edges:
        if index not in crumbs:
          toCount.append(top.edges[index])
    uid = list(crumbs)
    uid.sort()
    return total, tuple(uid)

  def __str__(self):
    fmt = f"Node {self.index} [value={self.value}, total={self.treeTotal} children={set(self.edges.keys())}]"
    return fmt



class ArrayTree:
  def __init__(self, values, edges):
    self.root = None
    self.values = values
    self.edges = edges
    edgeTuples = {tuple(e) for e in edges}
    self.nodes = [None] + [Node(v, i+1) for i, v in enumerate(values)]
    for s, e in edges:
      self.nodes[s].addEdge(self.nodes[e])
    self.preComputeAll()
    self.nodePerTreeTotal = {}
    for node in self.nodes[1:]:
      if node.treeTotal in self.nodePerTreeTotal:
        self.nodePerTreeTotal[node.treeTotal].append(node)
      else:
        self.nodePerTreeTotal[node.treeTotal] = [node]


  def preComputeAll(self):
    queue = []
    top = None
    for node in self.nodes[1:]:
      if len(node.edges) == 1:
        node.height = 1
        node.enqueued = True
        queue.append(node)
    while queue:
      top = queue.pop(0)
      top.enqueued = False
      # print("Pop", top.index)
      if len(top.edges) == 1:
        top.height = 1
        top.treeTotal = top.value
        parent = None
        for c in top.edges:
          parent = top.edges[c]
        top.rmEdge(parent.index)
        top.parent = parent
        if not parent.enqueued:
          parent.enqueued = True
          queue.append(parent)
        # print("Enqueue", parent.index)
      else:
        children = [top.edges[c] for c in top.edges if top.edges[c].height != None]
        parent = [top.edges[c] for c in top.edges if top.edges[c].height == None]
        if len(parent) > 1:
          top.enqueued = True
          queue.append(top)
        else:
          if children:
            top.height = max([child.height for child in children]) + 1
            top.treeTotal = top.value + sum([c.treeTotal for c in children])
          if parent:
            parent = parent[0]            
            top.rmEdge(parent.index)
            top.parent = parent
            if not parent.enqueued:
              parent.enqueue = True
              queue.append(parent)
            # print("Enqueue", parent.index)
    self.root = top

  def print(self):
    sortByDepth = sorted(self.nodes[1:], key=lambda node: -node.height)
    for node in sortByDepth:
      print(node)

  def betterBalancedValue(self, root, subtreeRoot, ceiling=None):
    # print("Checking balance of ", root.index, subtreeRoot.index)
    subtreeTotal = subtreeRoot.treeTotal
    rootTreeTotal = root.treeTotal - subtreeTotal
    rootToSubdivide = root if rootTreeTotal > subtreeTotal else subtreeRoot
    balancedForestValue = min(subtreeTotal, rootTreeTotal)
    treeToSubdivideValue = max(subtreeTotal, rootTreeTotal)
    amountToRemove = treeToSubdivideValue - balancedForestValue
    amountNeedingAdded = balancedForestValue * 2 - treeToSubdivideValue
    if subtreeTotal == rootTreeTotal and (ceiling is None or subtreeTotal < ceiling):
      return subtreeTotal
    # print(f"Even = {balancedForestValue} Excess = {treeToSubdivideValue} ToRemove= {amountToRemove} ToAdd={amountNeedingAdded}")
    if amountNeedingAdded > 0 and (ceiling is None or ceiling > amountNeedingAdded):
      cands = self.nodePerTreeTotal.get(amountToRemove, []) + self.nodePerTreeTotal.get(balancedForestValue, [])
      for candidate in cands:
        if candidate.hasParent(rootToSubdivide):
          return amountNeedingAdded
    return None
      
    

  def tryEdges(self):
    treeTotalValue = self.root.treeTotal
    queue = [self.root]
    best = None
    while queue:
      top = queue.pop(0)
      for edgeDestination in list(top.edges.keys()):
        # print("Edge loo")
        edgeDestNode = top.edges[edgeDestination]
        subtreeRoot = top.exciseChild(edgeDestination)
        balancedTreeValue = min(treeTotalValue-subtreeRoot.treeTotal, subtreeRoot.treeTotal)
        if balancedTreeValue >= treeTotalValue/3 and balancedTreeValue <= 2*treeTotalValue / 3:
          minAddition = self.betterBalancedValue(self.root, subtreeRoot, best)
          if minAddition:
            best = minAddition
          top.replaceEdge(edgeDestNode)
          queue.append(edgeDestNode)
        else:
          top.replaceEdge(edgeDestNode)
    return best



def getMinAddition(a,b,c):
  if a == b and c <= b:
    return b - c
  if a == c and b <= c:
    return c - b
  if b == c and a <= b:
    return b - a
  return None



# Greedy algorithm
# 1. Start at root, cut an edge, forming a subtree and supertree.
# 2. Descend supertree, looking for a subtree to cut away s.t. the remaining supertree
    # and the original subtree have equal value
# 3. Add the remainder to the last subtree, return.
# Repeat until have exhausted viable cuts and return minimum???

# Constraints:
  # Cuts can only range from 1/3 of total tree value to 1/2 of total tree value.

def balancedForest(c, edges):
  tree = ArrayTree(c, edges)
  best = tree.tryEdges()
  if best:
    return best
  return -1


    

if __name__ == '__main__':
    fptr = open(os.environ.get('OUTPUT_PATH', '/dev/stdout'), 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        c = list(map(int, input().rstrip().split()))

        edges = []

        for _ in range(n - 1):
            edges.append(list(map(int, input().rstrip().split())))
        result = balancedForest(c, edges)
        fptr.write(str(result) + '\n')

    fptr.close()
