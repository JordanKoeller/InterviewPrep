
def print_debug(matrix, nums):
  for i in range(len(nums)):
    for l in range(1, len(nums) - i + 1):
      print(f"{nums[i:i+l]} => {matrix[i][l]}")

def mcs_n2(nums, left, right):
  matrix = [[0 for _ in range(len(nums) + 1)] for _ in range(len(nums))]
  counter = 0
  for i in range(0, len(nums)):
    for l in range(1, len(nums) - i + 1):
      if l == 1:
        print("setting", i, 1, nums[i])
        matrix[i][1] = nums[i]
      else:
        matrix[i][l] = max(nums[i + l - 1], matrix[i][l - 1])
      if matrix[i][l] <= right and matrix[i][l] >= left:
        counter += 1
  print_debug(matrix, nums)
  return counter

def local_max(i, nums): # TODO: consider the plateau case.
  if i > 0 and i < len(nums) - 1:
    return nums[i] > nums[i - 1] and nums[i] > nums[i + 1]
  if i == 0 and len(nums) == 1:
    return True
  if i == 0 and len(nums) > 1:
    return nums[i] > nums[i + 1]
  if i == len(nums) - 1 and len(nums) > 1:
    return nums[i] > nums[i - 1]

def num_subarrays(cnt):
  # An array of 4 can be: one array of 4 + 2 arrays of 3 + 3 arrays of 2 + 4 arrays of 1
  if cnt % 1 == 0:
    # Even
    return (cnt + 1) * (cnt / 2) #1 + 4 | + 2 + 3
  else:
    return (cnt + 1) * (cnt // 2) + (cnt + 1) / 2   # 1 + 5 || 2 + 4 || + 3

def mcs_n(nums, left, right):
  # If i only had to consider "right" -> subarrays with a max <= some value:
  # for-loop through with 2 indices and a value.
  # sliceStart = 0 | last seen relative maximum
  # I for-loop to the next relative maximum (or the end of the array).
  #  Every time a see a value that is > right, I add to numExcluded
  # conter += ((i - sliceStart) ** 2 - 1) - 
  counter = 0
  lastPeak = 0
  overCounts = 0
  for i in range(len(nums)):
    if nums[i] > right and local_max(i, nums):
      counter += num_subarrays(i - lastPeak)
      counter -= overCounts
      overCounts = 0
      lastPeak = i
    elif nums[i] > right:
      overCounts += i - lastPeak
  return int(counter)
      # We have reached the next "peak"
def test_mcs():
  print(mcs_n([2, 1, 4, 3], 2, 3))

test_mcs()