"""
Number: 16891
Number as an image. And you want to rotate by N degrees

If you rotate by 180 degrees around the center, is it a valid number

Positive, integer


1 -> 1
2 -> NO
3 -> NO
4 -> 6?
5 -> NO
6 -> 9
7 -> NO
8 -> 8
9 -> 6
0 -> 0

number -> convert to string
"rotate" that string -> reverse it, and do my character mapping
if I can convert taht string back to a number, return True. Else return False
"""

ROT_CHARS = {
  '1': '1',
  '2': None,
  '3': None,
  '4': None,
  '5': None,
  '6': '9',
  '7': None,
  '8': '8',
  '9': '6',
  '0': '0'
}


def canRotate(strNum) -> bool:
  if len(strNum) % 2 == 1 and strNum[(len(strNum) // 2)] not in ['1', '0', '8']:
      return False
  for i, _ in enumerate(strNum[:len(strNum) // 2]):
    rI = len(strNum) - 1 - i
    if ROT_CHARS[strNum[rI]] != strNum[i]:
      return False
  return True




print(canRotate('16891'))
print(canRotate('16591'))
print(canRotate('1691'))
print(canRotate('100'))
print(canRotate('010'))
# print(canRotate(16891))
# print(canRotate(16891))
# print(canRotate(16891))
# print(canRotate(16891))

#PROBLEM 2
"""
PROBLEM 2
Given a list of Product ID paris, group them according to their categories
and return the new list containing categorized Product Ids

Input: ((1,2), (2,5), (3,4), (4,6), (6,8), (5,7), (5,2), (5,2))
Output: ((1,2,5,7), (3,4,6,8))
"""

def findCategory(elem, categories):
  # Find the index in the categories array that contains a set with elem in it
  for  i, mySet in enumerate(categories):
    if elem in mySet:
      return i
  return None

def findCategoryFast(elem, elemToCategory):
  if elem in elemToCategory:
    return elemToCategory[elem]
  return None

#N := number of pairs (len(prodPairs))
#O(N^2) if all are in distinct categories before we start merging things.
# 
def categorize(prodPairs):
  categories = []
  elemToCategory = {}
  for a, b in prodPairs:
    aCat = findCategoryFast(a, elemToCategory)
    bCat = findCategoryFast(b, elemToCategory)
    if aCat is not None and bCat is not None and aCat != bCat:
      # Merge sets:
      categories[aCat] = categories[aCat].union(categories[bCat])
      categories.pop(bCat)
      for elem in categories[bCat]:
        elemToCategory[elem] = aCat
    elif aCat is None and bCat is not None:
      categories[bCat].add(a)
      elemToCategory[a] = bCat
    elif aCat is not None and bCat is None:
      categories[aCat].add(b)
      elemToCategory[b] = aCat
    elif aCat is None and bCat is None:
      elemToCategory[a] = len(categories)
      elemToCategory[b] = len(categories)
      categories.append(set([a, b]))
  return [list(category) for category in categories]

print(categorize(((1,2), (2,5), (3,4), (4,6), (6,8), (5,7), (5,2), (5,2))))