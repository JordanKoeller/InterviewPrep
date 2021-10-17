"""
Bucket by height, similar to last problem

I need a lookup for i, j to know how much "volume" is interior and occupied between "i, j"

Make a lookup table of value -> [min index of at least value, max index of at least value]
Lookup (i, j) -> volume of walls between i, j
"""

"""
i, j = 0, 1
total = 0
walVolume = 0
startInd = 0
for i in range(0, len(height)):


"""

class Solution:
  def trap(self, height):
    waterColumns = [0 for _ in range(len(height))]
    highestSeen = height[0]
    for i in range(len(height)):
      waterColumns[i] = max(highestSeen, height[i])
      highestSeen = max(highestSeen, height[i])
    highestSeen = 0
    for i in range(len(height) - 1, -1, -1):
      waterColumns[i] = min(max(highestSeen, height[i]), waterColumns[i])
      highestSeen = max(highestSeen, height[i])
    total = 0
    for i in range(len(height)):
      waterInColumn = waterColumns[i] - height[i]
      if waterInColumn > 0:
        total += waterInColumn
    return total

def test(heights):
  solver = Solution()
  print(solver.trap(heights))

test([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
test([4, 2, 0, 3, 2, 5])