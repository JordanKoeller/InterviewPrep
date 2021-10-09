"""
        0
   1          2
 3   4     5     6
7 8 9 10 11 12 13 14
  
"""

class BinaryHeap:

    def __init__(self):
        self.values = []

    def parentIndex(self, index):
        return (len(self.values) - 1) // 2

    def swap(self, i, j):
        tmp = self.values[i]
        self.values[i] = self.values[j]
        self.values[j] = tmp


    def add(self, value):
        if len(self.values) == 0:
            self.values.append(value)
            return
        self.values.append(value)
        i = len(self.values) - 1
        while i >= 0 and self.values[i] < self.values[self.parentIndex(i)]:
            self.swap(i, self.parentIndex(i))
            i = self.parentIndex(i)

    def remove(self):
        if len(self.values) == 0:
            raise ValueError("Cannot pop a min value")
        ret = self.values[0]
        i = 0
        while i < len(self.values):
            l = i * 2 + 1
            r = i * 2 + 2
            if l < len(self.values) and r < len(self.values):
                if self.values[l] < self.values[r]:
                    self.swap(i, l)
                    i = l
                else:
                    self.swap(i, r)
                    i = r
            elif l < len(self.values):
                self.swap(i, l)
                i = l
            elif r < len(self.values):
                self.swap(i, r)
                i = r
            else:
                break
        if i >= len(self.values):
            i = self.parentIndex(i)
        self.swap(i, len(self.values) - 1)
        return ret

def testBinaryHeap():
    values = [2, 5, 3, 1, 6, 7, 4, 5, 3, 7, 8, 9,6, 4,3,2, 1, 0]
    sorts = sorted(values)
    heap = BinaryHeap()
    for v in values:
        heap.add(v)
    print(heap.values)
    for v in values:
        vv = heap.remove()
        print(vv)

testBinaryHeap()

