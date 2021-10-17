

"""
Given an array of nums and k, determine if can form k many subsets with equal sums.

numbers are all zero or positive integers
"""

def power_series(numbers, k):
  total = sum(numbers)
  if len(numbers) < k:
    return False
  if (total // k) * k != total:
    return False # Had some remainder
  target_sum = total // k
  used = [False for _ in range(len(numbers))]

def set_of_k(numbers, used, target_sum, sets_remaining, start_idx, current_sum, current_size):
  if sets_remaining == 1: return True
  if current_sum == target_sum and current_size > 0:
    return set_of_k(numbers, used, target_sum, sets_remaining-1, 0, 0, 0)
  for i in range(start_idx, len(numbers)):
    if current_sum + used[i] <= target_sum:
      used[i] = True
      recursion = set_of_k(numbers, used, target_sum, sets_remaining, start_idx+1, current_sum+used[i], current_size + 1)
      if recursion:
        return True
      used[i] = False
  return False

