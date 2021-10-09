"""
Binary tree - given the root.

root at level 0
For it to be even-odd, at every level of the tree,
  children in even-index levels must be odd and strictly increasing
  children in odd-index levels must be even and strictly decreasing
"""

import collections

class Node:
  def __init__(self, left, right, value):
    self.left = left
    self.right = right
    self.value = value

def evenOddTree(node):
  queue = collections.deque()
  queue.append((node, 0))
  prevLevel = -1
  prevValue = None
  while queue:
    head, currLevel = queue.popleft()
    if currLevel != prevLevel:
      prevLevel = currLevel
      prevValue = head.value
    else:
      if currLevel % 2 == 0 and prevValue > head.value: # Even lvl
        return False
      if currLevel % 2 == 1 and prevValue < head.value: # odd lvl
        return False
    if currLevel % 2 == 0 and head.value % 2 == 0:
      return False
    if currLevel % 2 == 1 and head.value % 2 == 1:
      return False
    prevValue = head.value
    if head.left:
      queue.append((head.left, currLevel + 1))
    if head.right:
      queue.append((head.right, currLevel + 1))
  return True

r = evenOddTree(
  Node(
    Node(
      Node(None, None, 3),
      None,
      10
    ),
    Node(
      Node(None, None, 7),
      Node(None, None, 9),
      -2
    ),
    1
  )
)
print(r)