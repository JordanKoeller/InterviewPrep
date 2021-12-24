"""

list a: 7 -> 1 -> 2 -> 3 -> 4 -> 7 -> 9 -> None
list b:              100  / 

Want to find the first node that is common to both lists.

Note: The two lists may never intersect.

I want the node with a COMMON memory location
"""

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

def find_intersection(l1, l2):
  "Design: Make a lookup table for one of the lists from its location to its node"
  if l1 is None or l2 is None:
    return None
  node_refs = {}
  rover = l1
  while rover != None:
    node_refs[id(rover)] = rover
    rover = rover.next
  rover = l2
  while rover != None:
    if id(rover) in node_refs:
      return node_refs[id(rover)]
    rover = rover.next
  return None