import random
import math

num_swaps = 0
num_compares = 0

def swap(array, i, j):
  global num_swaps
  num_swaps += 1
  tmp = array[i]
  array[i] = array[j]
  array[j] = tmp

def compare(a, b):
  global num_compares
  num_compares += 1
  return a < b

def mergesort(array):
  if len(array) < 2:
    return array
  if len(array) == 2:
    if array[0] > array[1]:
      swap(array, 0, 1)
    return array
  midpt = len(array) // 2
  left, right = mergesort(array[0:midpt]), mergesort(array[midpt:])
  lI, rI = 0, 0
  while lI + rI < len(array):
    if lI < len(left) and (rI >= len(right) or compare(left[lI], right[rI])):
      array[lI + rI] = left[lI]
      lI += 1
    elif rI < len(right) and (lI >= len(left) or compare(right[rI], left[lI])):
      array[lI + rI] = right[rI]
      rI += 1
  return array

def test_mergesort(values):
  global num_swaps
  global num_compares
  num_compares = 0
  num_swaps = 0
  mergesort(values)
  if confirm_sorted(values):
    print(f"SORT PASS, N={len(values)} S/NlogN={num_compares/len(values)/math.log2(len(values))}")
  else:
    print("SORT FAILURE", values)


def confirm_sorted(values):
  data_copy = [*values]
  data_copy.sort()
  for i, j in zip(data_copy, values):
    if i != j:
      return False
  return True

def get_test_case(n):
  values = [i for i in range(n)]
  random.shuffle(values)
  return values

test_mergesort(get_test_case(10))
test_mergesort(get_test_case(100))
test_mergesort(get_test_case(500))
test_mergesort(get_test_case(1000))
test_mergesort(get_test_case(5000))
test_mergesort(get_test_case(10000))
test_mergesort(get_test_case(100000))
test_mergesort(get_test_case(500000))