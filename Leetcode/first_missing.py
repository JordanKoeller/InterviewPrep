"""
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.
"""

"""
1. Find min and max values (first pass)
2. Xor all the numbers in that range
3. Xor all the elements
4. Whatever is remaining is what is missing

Xor: xoring the same number twice is a NOOP
     Xor is commutative and associative so order does not matter.

If one number not duplicated, then xor-ing through the entire thing will return that number
  issue: if missing multiple numbers, I have no way to detangle them

Associative and commutative operations:
  xor
  multiply
  addition
  bitwise and
  bitwise or

Steps:
  1. xor everything between min_value and max_value
  2. xor everything in the array
  xor 1 & 2 gives xor of all things that ARE NOT in the array
  xor result in descending order until result of xor is 0. There's the answer!

  iterate through range. xor as i go to get the xor of all values in range to the right of current value
"""

def first_missing(nums):
  for i in range(len(nums)):
    if nums[i] < 0:
      nums[i] = 0
  for i in range(len(nums)):
    if nums[i] > 0 and nums[i] < len(nums):
      nums[nums[i] - 1] = -1
  for i in range(0, len(nums)):
    if nums[i] != -1:
      return i + 1
  return len(nums)