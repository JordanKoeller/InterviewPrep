"""
Quicksort:

Properties:
  In-place sorting algorithm.
  Quicksort is NOT stable

Complexity:
  Space complexity is O(1) (in-place)
  Average time complexity O(nlogn)
  Worst-case time complexity (On^2)



Design:
  Select a pivot value, then sort and shift according to values above and below the pivot, swapping elements.
  Repeat unil there are no more swaps to do.

"""
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

def rand_partition(array, start, end):
  return random.randint(start, end - 1)

def quicksort(array, start=0, end=None, get_partition=rand_partition):
  if end == None:
    end = len(array)
  if end - start < 2:
    return
  if end - start == 2:
    if compare(array[end-1], array[start]):
      swap(array, start, end-1)
    return
  partition_idx = partition(array, start, end, get_partition)
  if start < partition_idx:
    quicksort(array, start, partition_idx, get_partition)
  if partition_idx < end:
    quicksort(array, partition_idx, end, get_partition)
  return
  
def partition(array, start, end, get_partition):
  partition_idx = get_partition(array, start, end)
  left, right = start, end - 1
  partition_value = array[partition_idx]
  while left <= right:
    while compare(array[left], partition_value): left += 1
    while compare(partition_value, array[right]): right -= 1
    if left <= right:
      swap(array, left, right)
      left += 1
      right -= 1
  return left


def test_quicksort(values):
  global num_swaps
  global num_compares
  num_compares = 0
  num_swaps = 0
  quicksort(values)
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

test_quicksort(get_test_case(10))
test_quicksort(get_test_case(100))
test_quicksort(get_test_case(500))
test_quicksort(get_test_case(1000))
test_quicksort(get_test_case(5000))
test_quicksort(get_test_case(10000))
test_quicksort(get_test_case(100000))
test_quicksort(get_test_case(500000))