"""
Given a binary tree with 0 or 2 children, every right node is a leaf,

flip it upside down s.t. every left node is a leaf.
"""

"""
Input:
      1
    2    3
  4   5



Output:
    4
  5   2
    3    1 


    A               B
  /   \    =>     /   \
 B     C         C     A
f  g         

Rotation:
  
Lowest unit of recursion:
rotate_subtree(superParent):
  a = superParent.left
  b = a.left
  c = a.right

  superParent.right = b
  b.left = c
  b.right = a

root => comes from the furthest-left node.

do a dfs -> make a stack:
  while popping up the stack:
    subtree = stack.pop()
    stack.peek().right = rotate_subtree(subtree)

stack = []

  

"""

def rotate_subtree(parent):
  a = parent
  if not a:
    return None
  b = a.left
  c = a.right
  if b:
    a.left = b.right
    a.right = b.left
    b.left = c
    b.right = a
  return b

class Node:

  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __str__(self):
    return str(self.value)
  
  def print(self):
    print(f"Node({self.value}) => [{self.left}, {self.right}]")
    if self.left:
      self.left.print()
    if self.right:
      self.right.print()  

"""

    A               B
  /   \    =>     /   \
 B     C         C     A
f  g         

"""

def flip_tree(tree):
  stack = [tree]
  while stack[-1].left != None:
    stack.append(stack[-1].left)
  root = stack[-1]
  while len(stack) > 1:
    b = stack.pop()
    b.right = stack[-1]
    b.left = stack[-1].right
  stack[-1].left = None
  stack[-1].right = None
  return root

def test_flip():
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)
  root.left.left = Node(4)
  root.left.right = Node(5)
  root.print()
  new_tree = flip_tree(root)
  print("Print flipped")
  new_tree.print()


test_flip()