'''

'''

class BinaryHeap: # Min-first heap

  def __init__(self):
    self.values = []
  
  def add(self, value):
    if self.count == 0:
      self.values.append(value)
    else:
      i = len(self.values)
      self.values.append(value)
      while i > 0:
        parentIndex = self.parentIndex(i)
        if self.values[parentIndex] > self.values[i]:
          self.swap(parentIndex, i)
          i = parentIndex
        else:
          return
  
  def remove(self):
    if self.count == 0:
      raise ValueError()
    ret = self.values[0]
    i = 0
    flag = True
    while i * 2 + 1 < self.count:
      l = i * 2 + 1
      r = i * 2 + 2
      if l < self.count and r < self.count:
        if self.values[l] < self.values[r]:
          self.values[i] = self.values[l]
          i = l
        else:
          self.values[i] = self.values[r]
          i = r
      elif l < self.count:
        self.values[i] = self.values[l]
        i = l
    self.values[i] = self.values[self.count - 1]
    self.values.pop(-1)
    return ret 

  @property
  def count(self):
    return len(self.values)

  def swap(self, i, j):
    tmp = self.values[i]
    self.values[i] = self.values[j]
    self.values[j] = tmp

  def parentIndex(self, index):
    return (index - 1) // 2

def test1():
  data = [8, 6, 7, 7, 5, 3, 0, 9, 1, 2, 4, 3, 5, 4, 7, 9, 0, 7, 8, 5, 3, 6, 2, 4, -5, 2, -1, -12]
  heap = BinaryHeap()
  for d in data:
    heap.add(d)
  ret = []
  while heap.count:
    ret.append(heap.remove())
  print(ret)

test1()