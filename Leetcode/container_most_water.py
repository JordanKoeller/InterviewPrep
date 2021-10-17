
"""
Given n non-negative integers, find the two lines that make the walls of the larges volume of water.

Other words: Find two numbers i, j
 where (j - i) * min(arr[i], arr[j]) is maximized.
"""

class Solution:
  def maxArea(self, height):
    valueMinMaxInds = {}
    for ind, h in enumerate(height):
      if h in valueMinMaxInds:
        valueMinMaxInds[h][1] = ind
      else:
        valueMinMaxInds[h] = [ind, ind]
    valuesSorted = list(valueMinMaxInds)
    valuesSorted.sort()
    globalBigDifferences = {}
    maxIndexSeen = -1
    minIndexSeen = len(height) + 1
    for i in range(len(valuesSorted) - 1, -1, -1):
      value = valuesSorted[i]
      minAtV, maxAtV = valueMinMaxInds[value]
      minIndexSeen = min(minIndexSeen, minAtV)
      maxIndexSeen = max(maxIndexSeen, maxAtV)
      globalBigDifferences[value] = [minIndexSeen, maxIndexSeen]
    answer = 0
    for value in globalBigDifferences:
      i, j = globalBigDifferences[value]
      tempBest =  abs(j - i) * min(height[i], height[j])
      if tempBest > answer:
        answer = tempBest
    return answer

def testCode(heights):
  solver = Solution()
  print(solver.maxArea(heights))

testCode([1, 8, 6, 2, 5, 4, 8, 3, 7])
testCode([1, 1])
testCode([4, 3, 2, 1, 4])
testCode([1, 2, 1])
      
