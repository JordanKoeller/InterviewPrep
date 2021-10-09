

class Node:
  def __init__(self, value, height=0):
    self.value = value
    self.left = None
    self.right = None
    self.height = height

  def isLeaf(self):
    return self.left == None and self.right == None

  def isBranch(self):
    return not self.isLeaf()

class BinarySearchTree:
  def __init__(self):
    self.root = None
    self.size = 0
  
  def addChild(self, value):
    if self.root:
      rover = self.root
      height = 1
      flag = True
      while flag:
        if value < rover.value:
          if rover.left:
            rover = rover.left
            height += 1
          else:
            rover.left = Node(value, height=height)
            flag = False
            self.size += 1
        elif value > rover.value:
          if rover.right:
            rover = rover.right
            height += 1
          else:
            rover.right = Node(value, height=height)
            flag = False
            self.size += 1
        else:
          print("Found a duplicate value", v)
          flag = False
    else:
      self.root = Node(value)
      self.size += 1

  def height(self):
    if self.root.isLeaf():
      return 0
    nodesToVisit = [self.root]
    maxHeight = 0
    while nodesToVisit:
      currNode = nodesToVisit.pop()
      if currNode.left:
        nodesToVisit.append(currNode.left)
      if currNode.right:
        nodesToVisit.append(currNode.right)
      if currNode.height > maxHeight:
        maxHeight = currNode.height
    return maxHeight


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.addChild(arr[i])

print(tree.height())

def height(root):
  if root.left == None and root.right == None:
    return 0
  nodesToVisit = [self.root]
  maxHeight = 0
  while nodesToVisit:
    currNode = nodesToVisit.pop()
    if currNode.left:
      nodesToVisit.append(currNode.left)
    if currNode.right:
      nodesToVisit.append(currNode.right)
    if currNode.height > maxHeight:
      maxHeight = currNode.height
  return maxHeight


  