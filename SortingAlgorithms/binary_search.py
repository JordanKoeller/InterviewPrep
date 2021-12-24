"""
Binary Search:
  I don't need to describe this. Find a particular element in a sorted array in O(logn) time. 

"""

def index_of(target, values):
  start, end = 0, len(values)
  while True:
    if end - start < 2:
      if values[start] == target:
        return start
      return None
    if end - start == 2:
      if values[start] == target:
        return i
      if values[start + 1] == target:
        return start + 1
      return None
    midpt = (end - start) // 2
    if values[midpt] == target:
      return midpt
    if target > values[midpt]:
      start = midpt
    if target < values[midpt]:
      end = midpt

def test_binary_search(values, target):
  values.sort()
  ret = index_of(target, values)
  if ret is not None:
    print(f"Found {values[ret]} at I={ret}")
  else:
    print(f"Could not find {target}")

test_binary_search([8, 6, 7, 5, 3, 0, 9], 5)
test_binary_search([8, 6, 7, 5, 3, 0, 9], 0)
test_binary_search([8, 6, 7, 5, 3, 0, 9], 1)