#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxRegion' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
class SetNode:

  def __init__(self, index, representative=None):
    self.index = index
    self.representative = self
    self.elements = set()
    self.elements.add(self.index)

  @property
  def setSize(self):
    return len(self.elements)

  def mergeSet(self, incoming):
    self.representative.elements = self.representative.elements.union(incoming.representative.elements)
    incoming.representative = self.representative
  def __str__(self):
    return f'SET [id={self.index} Size={self.setSize} Representative={self.representative.index}] children={self.elements}'

class DisjointSets:

  def __init__(self):
    self.roots = {}
    self.elements = {}

  def hasIndex(self, index):
    return index in self.elements

  def upsertIndex(self, index):
    if self.hasIndex(index):
      return self.elements[index]
    else:
      node = SetNode(index)
      self.elements[index] = node
      self.roots[index] = node
      return node

  def getNode(self, index):
    if self.hasIndex(index):
      return self.elements[index]
    return None
  
  def mergeSets(self, set1, set2):
    if set1 and set2:
      set1.mergeSet(set2)
      if set2.index in self.roots:
        del self.roots[set2.index]
  
  def getMaxSet(self):
    return max(self.roots.items(), key=lambda elem: elem[1].setSize)[1].setSize

  def __str__(self):
    return "ROOTS\n" +\
      "\n".join([str(root) for root in self.roots.values()]) + "\n"+\
      "ELEMS\n" +\
      "\n".join([str(elem) for elem in self.elements.values()])




            

def maxRegion(grid):
    # Write your code here
    sets = DisjointSets()
    for i in range(0, len(grid)-1):
      for j in range(0, len(grid[i])-1):
        if grid[i+1][j+1]:
          newNode = sets.upsertIndex((i+1, j+1))
        if grid[i][j]:
          baseNode = sets.upsertIndex((i,j))
          sets.mergeSets(newNode, baseNode)
        if grid[i+1][j]:
          baseNode = sets.upsertIndex((i+1,j))
          sets.mergeSets(newNode, baseNode)
        if grid[i][j+1]:
          baseNode = sets.upsertIndex((i,j+1))
          sets.mergeSets(newNode, baseNode)
    # print(sets)
    return sets.getMaxSet()

if __name__ == '__main__':
    fptr = open(os.environ.get('OUTPUT_PATH', '/dev/stdout'), 'w')

    n = int(input().strip())

    m = int(input().strip())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()
