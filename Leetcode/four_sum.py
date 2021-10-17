
class Solution:
  def fourSum(self, nums, target):
    nums.sort()
    ret = set()
    i = 0
    while i < len(nums) - 3:
      value = nums[i]
      missing = target - value
      triples = self.threeSum(nums, i+1, len(nums), missing)
      for t in triples:
        fourple = [value, *t]
        fourple.sort()
        ret.add(tuple(fourple))
      while i < len(nums) - 3 and nums[i] == value:
        i += 1
    return [list(fourple) for fourple in ret]

  def threeSum(self, nums, startI, endI, missing): # len(nums) < 3000, so O(n^2) may be possible.
    # Return all triples s.t. nums[i] + nums[j] + nums[k] = 0 and i,j,k are all distinct
    buckets = {}
    for ind in range(startI, endI):
      num = nums[ind]
      if num in buckets:
        buckets[num] += 1
      else:
        buckets[num] = 1
    ret = set()
    for numI in buckets:
      for numJ in buckets:
        if missing-(numI + numJ) in buckets:
          numK = missing-(numI + numJ)
          flag = True
          if numI == numK and numI == numJ and buckets[numI] < 3:
            flag = False
          elif numI == numJ and buckets[numI] < 2:
            flag = False
          elif numI == numK and buckets[numI] < 2:
            flag = False
          elif numJ == numK and buckets[numJ] < 2:
            flag = False
          if flag:
            triplet = [numI, numJ, numK]
            triplet.sort()
            ret.add(tuple(triplet))
    return [list(triplet) for triplet in ret]