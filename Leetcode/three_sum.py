
"""
  1. Make a table value -> [index].
  2. Make an empty set of the tuples (i, j, k)
  3. For-loop through array. Pick two random elements. Test set for a third that completes the triplet (N^2)
  4. Confirm i != j !=k, add to ret set. convert ret set to list and return it.
"""

class Solution:
  def threeSum(self, nums): # len(nums) < 3000, so O(n^2) may be possible.
    # Return all triples s.t. nums[i] + nums[j] + nums[k] = 0 and i,j,k are all distinct
    valueToIndex = {}
    for ind, number in enumerate(nums):
      if number in valueToIndex:
        valueToIndex[number].append(ind)
      else:
        valueToIndex[number] = [ind]
    retSet = set()
    for iV in valueToIndex:
      for jV in valueToIndex:
        if iV != jV:
          lookingFor = -(iV + jV)
          if lookingFor in valueToIndex:
            for k in valueToIndex[lookingFor]:
              if i != j and i != k and j != k:
                numbers = [nums[i], nums[j], nums[k]]
                numbers.sort()
                retSet.add(tuple(numbers))
    return [list(tup) for tup in retSet]

soln = Solution()
print(soln.threeSum([-1, 0, 1, 2, -1, -4]))