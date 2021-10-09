def can_split_equally(arr):
  if len(arr) == 0:
    return 0
  total = sum(arr)
  if total % 2 == 1:
    return -1
  target = total // 2
  matrix = [[0 for _ in range(target + 1)] for _ in range(len(arr) + 1)]
  for value in range(1, target + 1):
    if arr[0] <= value:
      matrix[0][value] = arr[0]
  for max_index in range(1, len(arr)):
    for target_value in range(1, target + 1):
      matrix[max_index][target_value] = matrix[max_index - 1][target_value] # Don't add current element
      if arr[max_index] <= target_value:
        best_including = matrix[max_index - 1][target_value - arr[max_index]] + arr[max_index]
        if best_including <= target_value and matrix[max_index][target_value] < best_including:
          matrix[max_index][target_value] = best_including
  return matrix[len(arr) - 1][target]

def test_helper(*data):
  result = can_split_equally(data)
  print(data, " => ", result, " Sum=", sum(data), sum(data) // 2 == result)

test_helper(1, 1, 3, 4, 5)
test_helper(1, 1, 1)
test_helper(1, 2)
test_helper(1, 2, 3)
test_helper(1)
test_helper(0)
test_helper(1, 5, 2, 2, 3, 4, 3)
test_helper(5,100 ,3, 1, 1)
test_helper()